(function(){
  var $=function(s,r){return (r||document).querySelector(s)},$$=function(s,r){return [].slice.call((r||document).querySelectorAll(s))};
  var reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
  var KEY='guide-systeme-seo:v1',state={copied:{},fields:{},pos:0,sec:'',mode:'read'};
  try{var raw=localStorage.getItem(KEY);if(raw){var o=JSON.parse(raw);for(var k in o)state[k]=o[k]}}catch(e){}
  function save(){try{localStorage.setItem(KEY,JSON.stringify(state))}catch(e){}}
  var saved={pos:state.pos,sec:state.sec},hold=false;

  /* progression, section en cours, temps restant */
  var bar=$('.progress i'),cur=$('.where .cur'),startLabel=cur.textContent,timeB=$('.time b'),article=$('article');
  var links=$$('nav.toc a'),sheetLinks=$$('.sheet a'),heads=links.map(function(a){return document.getElementById(a.hash.slice(1))});
  var words=0;$$('article>p,article>ul,article>h2,article>h3,article>h4').forEach(function(n){words+=n.textContent.trim().split(/\s+/).length});
  var total=Math.max(1,Math.round(words/200)),tick=false,last=0;
  function onScroll(){
    tick=false;
    var h=document.documentElement,max=h.scrollHeight-h.clientHeight,r=max>0?Math.min(1,h.scrollTop/max):0;
    bar.style.transform='scaleX('+r+')';
    var a=article.getBoundingClientRect(),ar=Math.min(1,Math.max(0,(innerHeight*0.4-a.top)/a.height));
    timeB.textContent=Math.max(0,Math.round(total*(1-ar)));
    var idx=-1;heads.forEach(function(el,i){if(el.offsetParent!==null&&el.getBoundingClientRect().top<=140)idx=i});
    [links,sheetLinks].forEach(function(set){set.forEach(function(l,i){l.classList.toggle('on',i===idx);if(i===idx)l.setAttribute('aria-current','true');else l.removeAttribute('aria-current')})});
    cur.textContent=idx<0?startLabel:links[idx].textContent;
    var now=Date.now();if(!hold&&now-last>600){last=now;state.pos=r;state.sec=idx<0?'':links[idx].textContent;save()}
  }
  addEventListener('scroll',function(){if(!tick){tick=true;requestAnimationFrame(onScroll)}},{passive:true});

  /* apparition au premier passage */
  var revs=$$('.reveal');
  if('IntersectionObserver' in window&&!reduce){
    var io=new IntersectionObserver(function(es){es.forEach(function(en){if(en.isIntersecting){en.target.classList.add('seen');io.unobserve(en.target);if(en.target.classList.contains('scoring'))countUp(en.target);if(en.target.classList.contains('tree'))unfold()}})},{rootMargin:'0px 0px -12% 0px'});
    revs.forEach(function(el){io.observe(el)});
  }else revs.forEach(function(el){el.classList.add('seen')});
  function countUp(box){
    $$('.num[data-v]',box).forEach(function(td,i){
      var v=+td.dataset.v,t0=performance.now()+i*90,d=900;td.textContent='0';
      (function step(t){var p=Math.min(1,Math.max(0,(t-t0)/d)),q=1-Math.pow(1-p,3);td.textContent=Math.round(v*q);if(p<1)requestAnimationFrame(step)})(performance.now());
    });
  }

  /* sommaire mobile */
  var sheet=$('.sheet');
  $('.where').addEventListener('click',function(){sheet.showModal()});
  $('.sx').addEventListener('click',function(){sheet.close()});
  sheet.addEventListener('click',function(ev){if(ev.target===sheet||ev.target.closest('a'))sheet.close()});

  /* mode lecture / skills */
  var modeBtns=$$('.seg2 button');
  function setMode(m,scroll){
    state.mode=m;save();document.body.classList.toggle('tools',m==='tools');
    modeBtns.forEach(function(b){b.setAttribute('aria-pressed',b.dataset.mode===m)});
    if(scroll)$('.wrap').scrollIntoView({block:'start'});
    onScroll();
  }
  modeBtns.forEach(function(b){b.addEventListener('click',function(){setMode(b.dataset.mode,true)})});
  if(state.mode==='tools')setMode('tools',false);

  /* copie */
  function copyText(text,btn,done){
    var ok=function(){var l=$('.lbl',btn);btn.classList.add('ok');l.textContent=btn.dataset.copied;setTimeout(function(){btn.classList.remove('ok');l.textContent=btn.dataset.copy},1600);if(done)done()};
    if(navigator.clipboard&&navigator.clipboard.writeText)navigator.clipboard.writeText(text).then(ok,function(){fallback(text);ok()});else{fallback(text);ok()}
  }
  function fallback(text){var a=document.createElement('textarea');a.value=text;a.style.position='fixed';a.style.opacity='0';document.body.appendChild(a);a.select();try{document.execCommand('copy')}catch(e){}a.remove()}

  /* skills */
  var skills=$$('.skillbox'),pill=$('.pill');
  function count(){$('b',pill).textContent=skills.filter(function(s){return state.copied[s.id]}).length+' / '+skills.length}
  function filled(row){var out='';$('.cons',row).childNodes.forEach(function(n){out+=n.nodeType===3?n.textContent:(n.value.trim()||n.dataset.ph)});return out}
  function download(name,blob){var a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download=name;document.body.appendChild(a);a.click();a.remove();setTimeout(function(){URL.revokeObjectURL(a.href)},2000)}
  skills.forEach(function(s){
    var more=$('.more',s),wrap=$('.swrap',s),pre=$('pre',wrap);
    function toggle(open){
      if(open===s.classList.contains('open'))return;
      var from=wrap.offsetHeight;
      if(open){s.classList.add('open');var to=wrap.scrollHeight;wrap.style.height=from+'px';wrap.offsetHeight;wrap.style.height=to+'px'}
      else{wrap.style.height=from+'px';wrap.offsetHeight;wrap.style.height='190px'}
      var end=function(){wrap.removeEventListener('transitionend',end);if(!open)s.classList.remove('open');wrap.style.height=''};
      if(reduce)end();else wrap.addEventListener('transitionend',end);
      more.setAttribute('aria-expanded',open);more.textContent=open?more.dataset.hide:more.dataset.show;
      if(!open)s.scrollIntoView({block:'nearest'});
    }
    more.addEventListener('click',function(){toggle(!s.classList.contains('open'))});
    $('.copy',s).addEventListener('click',function(){copyText(pre.textContent,this,function(){state.copied[s.id]=1;save();count()})});
    $('.dl',s).addEventListener('click',function(){download(s.dataset.name+'.md',new Blob([pre.textContent+'\n'],{type:'text/markdown'}))});
    $$('.chipb',s).forEach(function(c){c.addEventListener('click',function(){var t=document.getElementById(c.dataset.t);t.scrollIntoView({block:'start'});t.classList.add('flash');setTimeout(function(){t.classList.remove('flash')},1200)})});
    $$('.fill',s).forEach(function(inp){
      var fit=function(){inp.size=Math.max(4,(inp.value||inp.placeholder).length)};
      if(state.fields[inp.dataset.k]){inp.value=state.fields[inp.dataset.k]}fit();
      inp.addEventListener('input',function(){state.fields[inp.dataset.k]=inp.value;save();fit()});
    });
    $$('.crow',s).forEach(function(row){$('.copyc',row).addEventListener('click',function(){copyText(filled(row),this)})});
    var play=$('.play',s),term=$('.term',s);
    if(play)play.addEventListener('click',function(){
      var out=JSON.parse(term.dataset.out),file=term.dataset.file,tp=$('pre',term),cmd='> '+filled($('.crow',s));
      term.hidden=false;tp.innerHTML='';play.disabled=true;
      var first=document.createElement('span');first.className='c caret line';tp.appendChild(first);
      var lines=out.map(function(l){return '<span class="g">✓</span> '+esc(l)});if(file)lines.push('<span class="d">→ '+esc(file)+'</span>');
      function rest(){first.classList.remove('caret');var i=0;(function next(){if(i>=lines.length){play.disabled=false;return}var sp=document.createElement('span');sp.className='line';sp.innerHTML=lines[i++];tp.appendChild(sp);setTimeout(next,reduce?0:130)})()}
      if(reduce){first.textContent=cmd;rest();return}
      var n=0,stepSize=Math.max(1,Math.ceil(cmd.length/70));
      (function type(){n=Math.min(cmd.length,n+stepSize);first.textContent=cmd.slice(0,n);if(n<cmd.length)setTimeout(type,16);else setTimeout(rest,250)})();
    });
  });
  function md(s){return esc(s).replace(/`([^`]+)`/g,'<code>$1</code>')}
  function esc(s){return s.replace(/&/g,'&amp;').replace(/</g,'&lt;')}
  pill.addEventListener('click',function(){var t=skills.filter(function(s){return !state.copied[s.id]})[0]||skills[0];if(!document.body.classList.contains('tools')&&t.offsetParent===null)setMode('tools');t.scrollIntoView({block:'start'})});
  count();

  /* zip sans dépendance (méthode « stored ») */
  var crcT=(function(){var t=[],c,n,k;for(n=0;n<256;n++){c=n;for(k=0;k<8;k++)c=c&1?0xEDB88320^(c>>>1):c>>>1;t[n]=c>>>0}return t})();
  function crc(b){var c=-1;for(var i=0;i<b.length;i++)c=crcT[(c^b[i])&255]^(c>>>8);return (c^-1)>>>0}
  function zip(files){
    var enc=new TextEncoder(),parts=[],central=[],off=0;
    files.forEach(function(f){
      var name=enc.encode(f.name),data=enc.encode(f.text),c=crc(data),h=new DataView(new ArrayBuffer(30));
      h.setUint32(0,0x04034b50,true);h.setUint16(4,20,true);h.setUint16(6,0x0800,true);h.setUint32(14,c,true);h.setUint32(18,data.length,true);h.setUint32(22,data.length,true);h.setUint16(26,name.length,true);
      parts.push(h,name,data);
      var d=new DataView(new ArrayBuffer(46));
      d.setUint32(0,0x02014b50,true);d.setUint16(4,20,true);d.setUint16(6,20,true);d.setUint16(8,0x0800,true);d.setUint32(16,c,true);d.setUint32(20,data.length,true);d.setUint32(24,data.length,true);d.setUint16(28,name.length,true);d.setUint32(42,off,true);
      central.push(d,name);off+=30+name.length+data.length;
    });
    var size=central.reduce(function(s,p){return s+p.byteLength},0),e=new DataView(new ArrayBuffer(22));
    e.setUint32(0,0x06054b50,true);e.setUint16(8,files.length,true);e.setUint16(10,files.length,true);e.setUint32(12,size,true);e.setUint32(16,off,true);
    return new Blob(parts.concat(central,[e]),{type:'application/zip'});
  }
  $('.dlall').addEventListener('click',function(){download(window.GUIDE.zip,zip(skills.map(function(s){return {name:s.dataset.name+'/SKILL.md',text:$('.swrap pre',s).textContent+'\n'}})))});

  /* arborescence */
  var nodes=$$('.node'),pick=$('.pick'),folders=$$('.node.folder'),unfolded=false;
  function setFolder(f,open){f.setAttribute('aria-expanded',open);var k=f.nextElementSibling;if(open)k.removeAttribute('inert');else k.setAttribute('inert','')}
  function select(n){nodes.forEach(function(x){if(x===n)x.setAttribute('aria-current','true');else x.removeAttribute('aria-current')});$$('.pane').forEach(function(p){p.hidden=p.id!=='p'+n.dataset.i});if(pick)pick.hidden=true}
  nodes.forEach(function(n){n.addEventListener('click',function(){
    if(n.classList.contains('folder')){var isCur=n.getAttribute('aria-current')==='true',open=n.getAttribute('aria-expanded')==='true';setFolder(n,isCur?!open:true)}
    select(n);
  })});
  if(!reduce&&'IntersectionObserver' in window)folders.forEach(function(f){setFolder(f,false)});
  function unfold(){if(unfolded)return;unfolded=true;folders.forEach(function(f,i){setTimeout(function(){setFolder(f,true)},300+i*350)})}

  /* images agrandies */
  var box=$('.lightbox'),big=$('img',box);
  $$('.zoom').forEach(function(z){z.addEventListener('click',function(){big.src=$('img',z).src;box.showModal()})});
  box.addEventListener('click',function(){box.close()});

  /* reprise de lecture */
  var res=$('.resume');
  if(saved.pos>0.08&&saved.pos<0.97&&scrollY<200){
    $('.rs',res).textContent=saved.sec||Math.round(saved.pos*100)+' %';res.hidden=false;hold=true;
    $('.go',res).addEventListener('click',function(){var h=document.documentElement;scrollTo({top:saved.pos*(h.scrollHeight-h.clientHeight)});res.hidden=true;hold=false});
    $('.rx',res).addEventListener('click',function(){res.hidden=true;hold=false});
    addEventListener('scroll',function hide(){if(scrollY>innerHeight){res.hidden=true;hold=false;removeEventListener('scroll',hide)}},{passive:true});
  }
  /* test de fin */
  var quiz=$('.quiz'),Q=window.GUIDE.quiz,ans=state.quiz||[],qi=0,endCta=$('.end .cta');
  function label(id){var el=document.getElementById(id);return el.dataset.name||el.textContent}
  function go(id){quiz.close();if(document.body.classList.contains('tools')&&id.charAt(1)!=='k')setMode('read');var el=document.getElementById(id);setTimeout(function(){el.scrollIntoView({block:'start'})},60)}
  function showQ(){
    $('.qq',quiz).hidden=false;$('.qres',quiz).hidden=true;$('.qback',quiz).hidden=qi===0;
    $('.qstep',quiz).textContent=(qi+1)+' / '+Q.length;$('.qbar i',quiz).style.transform='scaleX('+qi/Q.length+')';
    var q=$('.qq',quiz);q.style.animation='none';q.offsetHeight;q.style.animation='';$('.qtext',quiz).textContent=Q[qi][0];
  }
  function showR(){
    $('.qq',quiz).hidden=true;$('.qres',quiz).hidden=false;$('.qback',quiz).hidden=true;$('.qstep',quiz).textContent='';$('.qbar i',quiz).style.transform='scaleX(1)';
    var yes=ans.filter(Boolean).length,miss=[];Q.forEach(function(q,i){if(!ans[i]&&miss.indexOf(q[1])<0)miss.push(q[1])});
    var pct=Math.round(yes/Q.length*100),left=Q.length-yes,G=window.GUIDE,tier=G.tiers.filter(function(t){return pct<t[0]})[0];
    $('.qscore span',quiz).textContent=yes+' / '+Q.length+' '+G.inplace;
    $('.qmsg',quiz).textContent=tier[1].replace('{n}',left+' '+G.pt[left>1?1:0]);
    var sb=$('.qscore b',quiz),mt=$('.qmeter i',quiz);
    if(reduce){sb.textContent=pct+' %';mt.style.transform='scaleX('+pct/100+')'}
    else{mt.style.transform='scaleX(0)';mt.offsetHeight;mt.style.transform='scaleX('+pct/100+')';var t0=performance.now();(function st(t){var k=Math.min(1,(t-t0)/900),q=1-Math.pow(1-k,3);sb.textContent=Math.round(pct*q)+' %';if(k<1)requestAnimationFrame(st)})(t0)}
    var tu=$('.qtips ul',quiz);tu.innerHTML='';G.tips[G.tiers.indexOf(tier)].forEach(function(t,i){
      var li=document.createElement('li'),b=document.createElement('button'),d=document.createElement('div'),id='qtd'+i;
      b.className='qtip';b.type='button';b.setAttribute('aria-expanded',i===0);b.setAttribute('aria-controls',id);
      b.innerHTML='<svg class="chev" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M9 6l6 6-6 6"/></svg><span>'+md(t.c)+'</span>';
      d.className='qtd';d.id=id;d.innerHTML='<div><p class="why">'+md(t.p)+'</p><ol>'+t.s.map(function(x){return '<li>'+md(x)+'</li>'}).join('')+'</ol></div>';
      if(i!==0)d.firstChild.setAttribute('inert','');
      b.addEventListener('click',function(){var o=b.getAttribute('aria-expanded')!=='true';b.setAttribute('aria-expanded',o);if(o)d.firstChild.removeAttribute('inert');else d.firstChild.setAttribute('inert','')});
      li.appendChild(b);li.appendChild(d);tu.appendChild(li);
    });
    card(pct,yes);
    var nx=$('.qnext',quiz),al=$('.qalso',quiz),ul=$('ul',al);ul.innerHTML='';nx.hidden=!miss.length;al.hidden=miss.length<2;
    if(miss.length){var g=$('.qgo',quiz);g.textContent=label(miss[0]);g.href='#'+miss[0];g.onclick=function(ev){ev.preventDefault();go(miss[0])}}
    miss.slice(1).forEach(function(id){var li=document.createElement('li'),a=document.createElement('a');a.href='#'+id;a.textContent=label(id);a.addEventListener('click',function(ev){ev.preventDefault();go(id)});li.appendChild(a);ul.appendChild(li)});
    var c=$('.qcta',quiz);c.href=endCta.href;c.innerHTML=endCta.innerHTML;
  }
  function card(pct,yes){var n=$('.qcard .qn');n.textContent=pct===null?n.dataset.base:pct+' % · '+yes+' / '+Q.length+' '+window.GUIDE.inplace}
  if(state.quizDone&&ans.length===Q.length){var y0=ans.filter(Boolean).length;card(Math.round(y0/Q.length*100),y0)}
  function answer(v){ans[qi]=v;state.quiz=ans;save();qi++;if(qi<Q.length)showQ();else{state.quizDone=1;save();showR()}}
  $('.qopen').addEventListener('click',function(){if(state.quizDone&&ans.length===Q.length)showR();else{qi=Math.min(ans.length,Q.length-1);showQ()}quiz.showModal()});
  $('.qyes',quiz).addEventListener('click',function(){answer(true)});
  $('.qno',quiz).addEventListener('click',function(){answer(false)});
  $('.qback',quiz).addEventListener('click',function(){if(qi>0){qi--;showQ()}});
  $('.qx',quiz).addEventListener('click',function(){quiz.close()});
  $('.qagain',quiz).addEventListener('click',function(){ans=[];state.quiz=ans;state.quizDone=0;save();qi=0;showQ();card(null)});
  quiz.addEventListener('click',function(ev){if(ev.target===quiz)quiz.close()});
  onScroll();
})();
