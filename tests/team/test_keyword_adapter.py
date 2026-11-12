"""Concurrent method loading must not mix one agent's instructions with another's."""
import _env  # noqa: F401  (coffre de test installé, chemins de scripts/team)
from concurrent.futures import ThreadPoolExecutor
import contextlib
import io
import time
import unittest
from unittest.mock import patch
import keyword_adapter


class MethodCaptureTest(unittest.TestCase):
    def test_parallel_captures_are_isolated(self):
        def fake_load(state, phase):
            print('start-' + state['keyword'])
            time.sleep(0.01)
            print('end-' + state['keyword'])
            state['loaded_methods'][str(phase)] = {'test':state['keyword']}
        def task(i):
            return {'project':{'brief':{'vault':str(keyword_adapter.KB)}},
                    'mission':{'phase':'intentions','subject':{'keyword':str(i)}}, 'upstream':[]}
        outer = io.StringIO()
        with patch.object(keyword_adapter.workflow, 'load_method', fake_load), contextlib.redirect_stdout(outer):
            with ThreadPoolExecutor(max_workers=3) as pool:
                outputs = list(pool.map(keyword_adapter.load_methods, [task(i) for i in range(10)]))
        self.assertEqual(outer.getvalue(), '')
        for i, (text, hashes) in enumerate(outputs):
            self.assertEqual(text, f'start-{i}\nend-{i}\n')
            self.assertEqual(hashes, {'test':str(i)})

if __name__ == '__main__': unittest.main()
