import { mkdir, readFile, rm, rmdir, writeFile } from "node:fs/promises";
import { afterAll, beforeAll, expect, test, vi } from "vitest";
import { BANNER_CID, bannerCid, presentEmail } from "../src/core/email-presentation";
import { resendMailer } from "../src/net/resend";

const { send } = vi.hoisted(() => ({ send: vi.fn().mockResolvedValue({ data: { id: "test-id" }, error: null }) }));
vi.mock("resend", () => ({ Resend: class { emails = { send }; } }));

// PNG de 1 px, déposé le temps du test dans public/email/ puis retiré.
const PNG = Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNkYPhfDwAChwGA60e6kgAAAABJRU5ErkJggg==", "base64");
const FILE = "public/email/banniere-test.png";
beforeAll(async () => { await mkdir("public/email", { recursive: true }); await writeFile(FILE, PNG); });
// Ne retire que le fichier de test : un bandeau réel déposé dans public/email/ reste intact.
afterAll(async () => { await rm(FILE, { force: true }); for (const dir of ["public/email", "public"]) await rmdir(dir).catch(() => {}); });

test("Resend reçoit le bandeau configuré, lié au HTML par CID", async () => {
  const body = "Bonjour <Maître>,\n\nCamille Test\nCabinet Test\nhttps://exemple.test";
  const email = presentEmail(body, bannerCid());
  await resendMailer("test").send({ from: "camille@exemple.test", replyTo: "reponses@exemple.test", to: "prospect@example.test", subject: "Test", ...email, headers: {}, idempotencyKey: "test" });
  const [payload, options] = send.mock.calls[0];
  const banner = payload.attachments[0];
  expect(banner.content.equals(await readFile(FILE))).toBe(true);
  expect(banner.filename).toBe("banniere-test.png");
  expect(banner.contentId).toBe(BANNER_CID);
  expect(banner.contentType).toBe("image/png");
  expect(payload.html).toContain(`src="cid:${banner.contentId}"`);
  expect(payload.html).toContain("&lt;Maître&gt;");
  expect(payload.text).not.toMatch(/^Cabinet Test$/m);
  expect(options.idempotencyKey).toBe("test");
});

test("sans EMAIL_BANNER_FILE, ni bandeau ni pièce jointe", async () => {
  const saved = process.env.EMAIL_BANNER_FILE;
  process.env.EMAIL_BANNER_FILE = "";
  try {
    send.mockClear();
    const email = presentEmail("Bonjour,\n\nCamille Test");
    expect(email.html).not.toContain("<img");
    expect(bannerCid()).toBeNull();
    await resendMailer("test").send({ from: "camille@exemple.test", replyTo: "reponses@exemple.test", to: "prospect@example.test", subject: "Test", ...email, headers: {}, idempotencyKey: "test2" });
    expect(send.mock.calls[0][0].attachments).toBeUndefined();
  } finally {
    process.env.EMAIL_BANNER_FILE = saved;
  }
});
