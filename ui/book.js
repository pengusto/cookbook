(() => {
'use strict';
/*COOKBOOK_SCROLL_GESTURE*/
const data = JSON.parse(document.getElementById('cookbook-data').textContent);
const locales = data.locales, recipes = data.recipes;
const publicBook = document.body.classList.contains('public-book');
const $ = id => document.getElementById(id);
const reduced = window.matchMedia('(prefers-reduced-motion: reduce)');
const systemColors=window.matchMedia('(prefers-color-scheme: dark)');
let appearance='system';try{const saved=localStorage.getItem('cookbook-appearance');if(['system','light','dark'].includes(saved))appearance=saved;}catch{}
let naming=data.variant;try{const saved=localStorage.getItem('cookbook-naming');if(['plain','kitchen'].includes(saved))naming=saved;}catch{}
const recipeName=recipe=>recipe.names[naming];
let selected = 0, animation = null, pageTurn = null, copyTimer = null;
let language = 'de';
const languages = Object.keys(locales);
function storedLanguage() { try { return localStorage.getItem('cookbook-language'); } catch { return null; } }
function matchLanguage(value) {
 if (!value) return null;
 if (locales[value]) return value;
 return languages.find(key => key.split('-')[0] === value.split('-')[0]) || null;
}
const query = new URLSearchParams(location.search);
language = matchLanguage(query.get('lang')) || matchLanguage(storedLanguage()) || matchLanguage(navigator.language) || 'en';
const requested = recipes.findIndex(recipe => recipe.id === location.hash.slice(1) || (publicBook && Object.values(recipe.installIds).includes(location.hash.slice(1))));
let bookPage = publicBook && requested < 0 ? (['welcome','install','about'].includes(location.hash.slice(1)) ? location.hash.slice(1) : 'welcome') : 'recipe';
let installHost = 'codex';
if (requested >= 0) {selected = requested;if(publicBook)naming=recipes[requested].installIds.plain===location.hash.slice(1)?'plain':'kitchen';}
function icon(name) { const svg=document.createElementNS('http://www.w3.org/2000/svg','svg'); svg.setAttribute('aria-hidden','true');const use=document.createElementNS(svg.namespaceURI,'use');use.setAttribute('href','#'+name);svg.append(use);return svg; }
function animate(target, options) {
 if (reduced.matches || !window.anime) return null;
 return window.anime.animate(target, options);
}
function currentBookLanguage(){
 return publicBook&&bookPage!=='recipe'?document.body.dataset.publicLanguage:language;
}
function skillInvocation(id){
 return (publicBook&&installHost==='claude'?'/cookbook-by-pengusto:':'$')+id;
}
function syncText() {
 const t=locales[language];
 const pageLanguage=currentBookLanguage();
 document.documentElement.lang=pageLanguage;
 document.documentElement.dir=pageLanguage==='ar'?'rtl':'ltr';
 document.querySelectorAll('[data-i18n]').forEach(node => node.textContent=t[node.dataset.i18n]);
 $('current-language').textContent=t.name;
 document.querySelector('.edition').textContent=naming==='kitchen'?'Kitchen edition':t.plainNames;
 document.querySelectorAll('[data-naming]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.naming===naming)));
 document.querySelectorAll('.recipe-label').forEach((label,index)=>label.textContent=recipeName(recipes[index]));
 document.querySelectorAll('[data-chapter-label]').forEach(label=>label.textContent=t.chapterTitles[label.dataset.chapterLabel]);
 $('language-toggle').setAttribute('aria-label',t.language+': '+t.name);
 $('language-heading').textContent=t.language;
 syncAppearance();
 $('language-close').setAttribute('aria-label',t.close);
 $('previous-recipe').setAttribute('aria-label',t.previous);
 $('next-recipe').setAttribute('aria-label',t.next);
 $('recipe-index').setAttribute('aria-label',t.recipe);
 document.querySelectorAll('[data-language]').forEach(button => button.setAttribute('aria-pressed',String(button.dataset.language===language)));
}
function displayRecipe(motion=true) {
 stopScrollTurn();
 resetPaperScroll();
 if(publicBook){bookPage='recipe';syncText();setBookVisibility();syncPublicInstall();}
 const recipe=recipes[selected], t=locales[language];
 $('recipe-chapter-context').textContent=t.chapter+' · '+t.chapterTitles[recipe.chapter];
 const number=String(selected+1).padStart(2,'0');
 $('recipe-number').textContent=number; $('page-number').textContent=number;
 $('recipe-title').textContent=recipeName(recipe);
 $('recipe-emblem').setAttribute('href','#recipe-'+recipe.icon);
 $('recipe-total').textContent=String(recipes.length).padStart(2,'0');
 $('alternate-name').textContent=(naming==='kitchen'?t.plainNames:'Kitchen')+': '+recipe.names[naming==='kitchen'?'plain':'kitchen'];
 $('installed-invocation').textContent=t.installedInvocation+' · '+((publicBook?naming:data.variant)==='kitchen'?'Kitchen':t.plainNames);
 const accent=document.documentElement.dataset.theme==='dark'?recipe.accentDark:recipe.accent;
 document.querySelector('.pages').style.setProperty('--recipe-accent',accent);
 document.querySelector('.cover').style.setProperty('--recipe-accent',accent);
 for(const [name,value] of Object.entries(recipe.artwork))document.querySelector('.pages').style.setProperty(name,value);
 $('dish-name').textContent=recipe.dishNames[language]||recipe.dishNames.en;
 $('pan-art').dataset.recipe=recipe.id;
 $('recipe-announcement').textContent=t.recipe+' '+number+': '+recipeName(recipe);
 $('recipe-summary').textContent=t.summaries.split('|')[selected];
 $('recipe-intro').textContent=t.intros.split('|')[selected];
 $('recipe-when').textContent=t.whenList.split('|')[selected];
 const ingredients=t.ingredientLists[selected];
 $('ingredient-list').replaceChildren(...ingredients.map((text,index)=>{const li=document.createElement('li'),art=document.createElement('span'),label=document.createElement('span');art.className='ingredient-food food-cell'+index;art.setAttribute('aria-hidden','true');label.textContent=text;li.append(art,label);return li;}));
 const steps=t['steps'+selected].split('|');
 $('method-list').replaceChildren(...steps.map((title,index)=>{
   const li=document.createElement('li'), copy=document.createElement('div'),h3=document.createElement('h3'),p=document.createElement('p'),art=document.createElement('span');
   const number=document.createElement('span');number.className='method-number';number.textContent=String(index+1);number.setAttribute('aria-hidden','true');
   h3.textContent=title; p.textContent=(t['stepNotes'+selected]||t.stepNotes)[index]; copy.append(h3,p);
   art.className='step-art food-cell'+index; art.setAttribute('aria-hidden','true');li.append(number,copy,art);return li;
 }));
 $('invocation').textContent=skillInvocation(publicBook?recipe.installIds[naming]:recipe.id);
 $('limits-copy').textContent=t.verifications[selected]+' '+t.limitText+' '+t.recipeLimits[selected];
 $('copy-status').textContent=t.languageNote;
 $('copy-command').setAttribute('aria-label',t.copyInvocation+': '+recipeName(recipe));
 $('copy-command-label').textContent=t.copyInvocation;
 delete $('copy-command').dataset.copied;
 clearTimeout(copyTimer);
 $('previous-recipe').disabled=selected===0;
 $('next-recipe').disabled=selected===recipes.length-1;
 document.querySelectorAll('.recipe-tab').forEach((button,index)=>button.setAttribute('aria-current',String(index===selected)));
 keepSelectedRecipeVisible();
 document.title=recipeName(recipe)+' · Cookbook by Pengusto';
 if (animation) { animation.revert(); animation=null; }
 if(pageTurn) { pageTurn.pause(); pageTurn=null; }
 document.querySelectorAll('.page-turn-leaf').forEach(node=>node.remove());
 if (motion) {
  animation=animate($('recipe-content'),{opacity:[.45,1],x:[8,0],duration:420,ease:'outCubic'});
  if(!reduced.matches && window.anime && innerWidth>850) {
   const leaf=document.createElement('div');leaf.className='page-turn-leaf';leaf.setAttribute('aria-hidden','true');document.querySelector('.pages').append(leaf);
   pageTurn=animate(leaf,{rotateY:language==='ar'?[0,155]:[0,-155],opacity:[.7,0],duration:620,ease:'inOutCubic',onComplete:()=>leaf.remove()});
  }
 }
 try {history.replaceState(null,'','#'+(publicBook?recipe.installIds[naming]:recipe.id));} catch { /* Host iframe can disallow history access. */ }
 if(data.remote)document.dispatchEvent(new CustomEvent('cookbook:recipe',{detail:{id:recipe.id}}));
}
function chooseRecipe(index,focus=false,motion=true) {
 if(index<0 || index>=recipes.length || (index===selected && bookPage==='recipe')) return;
 selected=index; displayRecipe(motion);
 if(focus) $('recipe-title').focus({preventScroll:true});
 if(innerWidth<=560) document.querySelector('.recipe-tab[aria-current=true]').scrollIntoView({block:'nearest',inline:'nearest',behavior:reduced.matches?'instant':'smooth'});
}
$('recipe-index').replaceChildren();
let chapterRecipes;
recipes.forEach((recipe,index)=>{
 if(index===0 || recipe.chapter!==recipes[index-1].chapter){
  const section=document.createElement('section');section.className='recipe-chapter';section.dataset.chapter=recipe.chapter;
  const heading=document.createElement('h2');heading.className='chapter-heading';heading.id='chapter-'+recipe.chapter;
  section.setAttribute('aria-labelledby',heading.id);
  const label=document.createElement('span');label.dataset.chapterLabel=recipe.chapter;
  const chapterIcons={orientation:'book',planning:'basket',build:'chef',review:'recipe-sieve',release:'serve',closing:'clock'};
  heading.append(icon(chapterIcons[recipe.chapter]),label);
  chapterRecipes=document.createElement('div');chapterRecipes.className='chapter-recipes';
  section.append(heading,chapterRecipes);$('recipe-index').append(section);
 }
 const button=document.createElement('button');button.type='button';button.className='recipe-tab';
 const label=document.createElement('span');label.dir='ltr';label.className='recipe-label';label.textContent=recipeName(recipe);button.append(icon('recipe-'+recipe.icon),label);
 button.addEventListener('click',()=>chooseRecipe(index));
 button.addEventListener('keydown',event=>{let next=null;if(event.key==='ArrowDown') next=Math.min(recipes.length-1,index+1);if(event.key==='ArrowUp') next=Math.max(0,index-1);if(event.key==='Home')next=0;if(event.key==='End')next=recipes.length-1;if(next!==null){event.preventDefault();chooseRecipe(next);document.querySelectorAll('.recipe-tab')[next].focus();}});
 chapterRecipes.append(button);
});
document.querySelectorAll('[data-naming]').forEach(button=>button.addEventListener('click',()=>{naming=button.dataset.naming;try{localStorage.setItem('cookbook-naming',naming);}catch{}syncText();if(publicBook){syncPublicInstall();if(bookPage==='recipe')displayRecipe(false);}else displayRecipe(false);}));
function closeLanguages(restore=false) {
 $('language-panel').hidden=true;$('language-toggle').setAttribute('aria-expanded','false');if(restore)$('language-toggle').focus();
}
function openLanguages() {
 closeAppearance();
 const panel=$('language-panel');panel.hidden=false;$('language-toggle').setAttribute('aria-expanded','true');
 animate(panel,{opacity:[0,1],y:[7,0],scale:[.98,1],duration:220,ease:'outCubic'});
 panel.querySelector('[aria-pressed=true]').focus({preventScroll:true});
}
languages.forEach(code=>{
 const button=document.createElement('button');button.type='button';button.dataset.language=code;button.lang=code;button.textContent=locales[code].name;button.dir=code==='ar'?'rtl':'ltr';
 button.addEventListener('click',()=>{language=code;try{localStorage.setItem('cookbook-language',code);}catch{}syncText();if(!publicBook||bookPage==='recipe')displayRecipe(false);else syncPublicInstall();closeLanguages(true);});$('language-options').append(button);
});
function syncAppearance(){
 const actual=appearance==='system'?(systemColors.matches?'dark':'light'):appearance;
 document.documentElement.dataset.theme=actual;
 document.documentElement.dataset.appearance=appearance;
 $('appearance-label').textContent=locales[language][appearance];
 $('appearance-toggle').setAttribute('aria-label',locales[language].appearance+': '+locales[language][appearance]);
 document.querySelectorAll('[data-appearance]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.appearance===appearance)));
 const recipe=recipes[selected],accent=actual==='dark'?recipe.accentDark:recipe.accent;
 document.querySelector('.pages').style.setProperty('--recipe-accent',accent);
 document.querySelector('.cover').style.setProperty('--recipe-accent',accent);
}
function closeAppearance(restore=false){$('appearance-panel').hidden=true;$('appearance-toggle').setAttribute('aria-expanded','false');if(restore)$('appearance-toggle').focus();}
$('appearance-toggle').addEventListener('click',()=>{
 if(!$('appearance-panel').hidden){closeAppearance();return;}
 closeLanguages();$('appearance-panel').hidden=false;$('appearance-toggle').setAttribute('aria-expanded','true');
 animate($('appearance-panel'),{opacity:[0,1],y:[6,0],duration:200,ease:'outCubic'});
 $('appearance-panel').querySelector('[aria-pressed=true]').focus({preventScroll:true});
});
document.querySelectorAll('[data-appearance]').forEach(button=>button.addEventListener('click',()=>{
 appearance=button.dataset.appearance;try{localStorage.setItem('cookbook-appearance',appearance);}catch{}syncAppearance();closeAppearance(true);
}));
systemColors.addEventListener('change',()=>{if(appearance==='system')syncAppearance();});
document.addEventListener('click',event=>{if(!event.target.closest('.appearance-picker'))closeAppearance();});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!$('appearance-panel').hidden){event.preventDefault();closeAppearance(true);}});
$('appearance-panel').addEventListener('keydown',event=>{if(event.key!=='Tab')return;const buttons=Array.from($('appearance-panel').querySelectorAll('button'));if(event.shiftKey&&document.activeElement===buttons[0]){event.preventDefault();buttons[buttons.length-1].focus();}else if(!event.shiftKey&&document.activeElement===buttons[buttons.length-1]){event.preventDefault();buttons[0].focus();}});
$('language-toggle').addEventListener('click',()=>$('language-panel').hidden?openLanguages():closeLanguages());
$('language-close').addEventListener('click',()=>closeLanguages(true));
document.addEventListener('click',event=>{if(!event.target.closest('.language-picker'))closeLanguages();});
document.addEventListener('keydown',event=>{if(event.key==='Escape'&&!$('language-panel').hidden){event.preventDefault();closeLanguages(true);}});
$('language-panel').addEventListener('keydown',event=>{if(event.key!=='Tab')return;const controls=Array.from($('language-panel').querySelectorAll('button'));const first=controls[0],last=controls[controls.length-1];if(event.shiftKey&&document.activeElement===first){event.preventDefault();last.focus();}else if(!event.shiftKey&&document.activeElement===last){event.preventDefault();first.focus();}});
$('previous-recipe').addEventListener('click',()=>chooseRecipe(selected-1,true));
$('next-recipe').addEventListener('click',()=>chooseRecipe(selected+1,true));
$('copy-command').addEventListener('click',async()=>{
 const t=locales[language];
 try {
  await navigator.clipboard.writeText($('invocation').textContent);
  $('copy-status').textContent=t.copied;
  $('copy-command-label').textContent=t.copied;
  $('copy-command').dataset.copied='true';
  animate($('copy-command'),{scale:[1,.83,1],duration:280,ease:'outCubic'});
 } catch {
  const selection=window.getSelection(),range=document.createRange();range.selectNodeContents($('invocation'));selection.removeAllRanges();selection.addRange(range);$('copy-status').textContent=t.copyManual;
 }
 clearTimeout(copyTimer);copyTimer=setTimeout(()=>{const current=locales[language];$('copy-status').textContent=current.languageNote;$('copy-command-label').textContent=current.copyInvocation;delete $('copy-command').dataset.copied;},3000);
});
reduced.addEventListener('change',()=>{if(reduced.matches){if(animation){animation.revert();animation=null;}if(pageTurn){pageTurn.pause();pageTurn=null;}document.querySelectorAll('.page-turn-leaf').forEach(node=>node.remove());}});
function setBookVisibility(){
 if(bookPage!=='recipe'){document.documentElement.lang=document.body.dataset.publicLanguage;document.documentElement.dir='ltr';}
 document.querySelectorAll('[data-book-page]').forEach(node=>node.hidden=node.dataset.bookPage!==bookPage);
 $('recipe-content').hidden=bookPage!=='recipe';
 document.querySelectorAll('[data-open-page]').forEach(link=>{
  if(link.dataset.openPage===bookPage)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');
 });
 if(bookPage!=='recipe')document.querySelectorAll('.recipe-tab').forEach(button=>button.setAttribute('aria-current','false'));
}
function showBookPage(name,focus=false,write=true){
 stopScrollTurn();
 if(!['welcome','install','about'].includes(name))return;
 bookPage=name;setBookVisibility();syncPublicInstall();resetPaperScroll();
 const heading=document.querySelector('[data-book-page="'+name+'"] h1');
 document.title=heading.textContent+' · Cookbook by Pengusto';
 if(write)try{history.pushState(null,'','#'+name);}catch{}
 if(focus){heading.focus({preventScroll:true});if(innerWidth<=850)heading.scrollIntoView({block:'start',behavior:reduced.matches?'instant':'smooth'});}
}
function updateBookSchema(value){
 value.inLanguage=currentBookLanguage();
 value.mainEntity.itemListElement.forEach((entry,i)=>{
  entry.item.name=recipeName(recipes[i]);
  entry.item.description=locales[value.inLanguage].summaries.split('|')[i];
 });
 value.hasPart.forEach(chapter=>{
  chapter.name=locales[value.inLanguage].chapterTitles[chapter.identifier];
  chapter.hasPart=value.mainEntity.itemListElement.filter((entry,i)=>recipes[i].chapter===chapter.identifier).map(entry=>entry.item);
 });
 return value;
}
function syncPublicInstall(){
 if(!publicBook)return;
 document.querySelectorAll('[data-public-variant]').forEach(node=>node.textContent=naming==='kitchen'?'Kitchen':'Plain');
 $('codex-install-command').textContent='codex plugin marketplace add pengusto/cookbook --ref '+naming+'\ncodex plugin add cookbook-by-pengusto@cookbook-by-pengusto-local';
 document.querySelector('[data-install-overview]').href=(naming==='kitchen'?'install':'install-plain')+(document.body.dataset.publicLanguage==='de'?'':'-en')+'.html';
 document.querySelectorAll('[data-download-host]').forEach(a=>a.href='downloads/cookbook-by-pengusto-'+naming+'-'+a.dataset.downloadHost+'.zip');
 const guide=recipes.find(recipe=>recipe.installIds.plain==='explain-the-cookbook').installIds[naming];
 const first=$('first-invocation');
 if(!first.dataset.prompt)first.dataset.prompt=first.textContent.slice(first.textContent.indexOf(' ')+1);
 first.textContent=skillInvocation(guide)+' '+first.dataset.prompt;
 $('invocation').textContent=skillInvocation(recipes[selected].installIds[naming]);
 document.querySelectorAll('[data-install-host]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.installHost===installHost)));
 document.querySelectorAll('[data-host-panel]').forEach(panel=>panel.hidden=panel.dataset.hostPanel!==installHost);
 // Keep machine-readable names and summaries aligned with the recipe interface.
 const schema=$('book-schema');
 if(schema){const value=updateBookSchema(JSON.parse(schema.textContent));schema.textContent=JSON.stringify(value).replace(/</g,'\\u003c');}
}
if(publicBook){
 document.querySelectorAll('[data-open-page]').forEach(link=>link.addEventListener('click',event=>{event.preventDefault();showBookPage(link.dataset.openPage,true);}));
 document.querySelectorAll('[data-open-recipe]').forEach(button=>button.addEventListener('click',()=>{chooseRecipe(recipes.findIndex(recipe=>recipe.sourceId===button.dataset.openRecipe),true);}));
 document.querySelectorAll('[data-install-host]').forEach(button=>button.addEventListener('click',()=>{installHost=button.dataset.installHost;syncPublicInstall();}));
 document.querySelectorAll('[data-copy-target]').forEach(button=>button.addEventListener('click',async()=>{
  const code=$(button.dataset.copyTarget),status=$('install-copy-status');
  try{await navigator.clipboard.writeText(code.textContent);status.textContent=status.dataset.copied;}
  catch{const range=document.createRange();range.selectNodeContents(code);const selection=getSelection();selection.removeAllRanges();selection.addRange(range);status.textContent=status.dataset.manual;}
 }));
 addEventListener('popstate',()=>{const name=location.hash.slice(1);const index=recipes.findIndex(r=>Object.values(r.installIds).includes(name));if(index>=0){selected=index;displayRecipe(false);}else showBookPage(name||'welcome',false,false);});
}
// Scroll changes spreads only at document boundaries, never inside the index or a control.
const scrollGesture=new BookScrollGesture();
let scrollTurn=null,scrollPaper=null;
function stopScrollTurn(){if(scrollTurn){scrollTurn.revert();scrollTurn=null;}if(scrollPaper){scrollPaper.classList.remove('scroll-paper');scrollPaper.style.removeProperty('transform-origin');scrollPaper=null;}}
function spreadPosition(){return publicBook?(bookPage==='welcome'?0:bookPage==='install'?1:bookPage==='about'?recipes.length+2:selected+2):selected;}
function changeSpread(position){
 if(publicBook && (position<2 || position===recipes.length+2))showBookPage(position===0?'welcome':position===1?'install':'about');
 else chooseRecipe(publicBook?position-2:position,false,false);
}
let smoothScroll=null;
function syncSmoothScroll(){
 if(smoothScroll){smoothScroll.destroy();smoothScroll=null;}
 if(!reduced.matches && innerWidth>850 && window.Lenis){
  smoothScroll=new window.Lenis({autoRaf:true,syncTouch:false,respectReducedMotion:true,stopInertiaOnNavigate:true,
   prevent:node=>!!node.closest?.('.cover,.page,[role="dialog"],input,textarea,select,[contenteditable="true"]')});
 }
}
function resetPaperScroll(direction=1){
 document.querySelectorAll('.recipe-spread .page').forEach(page=>{
  page.scrollTop=direction>0?0:Math.max(0,page.scrollHeight-page.clientHeight);
 });
}
function resetSpreadScroll(direction){
 resetPaperScroll(direction);
 // The desktop frame is fixed; its page scroll positions carry reading progress.
 if(smoothScroll){smoothScroll.resize();smoothScroll.scrollTo(0,{immediate:true,force:true});}
 else window.scrollTo({top:0,behavior:'instant'});
}

function paperHalf(right){
 const pages=document.querySelector('.pages'),bounds=pages.getBoundingClientRect();
 return [...pages.querySelector('.recipe-spread:not([hidden])').querySelectorAll('.page')].find(node=>(node.getBoundingClientRect().left>=bounds.left+bounds.width*.25)===right);
}
function turnFromScroll(direction){
 const position=spreadPosition()+direction;
 const change=()=>{changeSpread(position);resetSpreadScroll(direction);};
 if(reduced.matches || !window.anime){change();return;}
 const right=direction>0?document.documentElement.dir!=='rtl':document.documentElement.dir==='rtl';
 const outgoing=paperHalf(right),angle=right?-88:88;
 scrollPaper=outgoing;outgoing.classList.add('scroll-paper');outgoing.style.transformOrigin=right?'left center':'right center';
 scrollTurn=animate(outgoing,{rotateY:[0,angle],opacity:[1,.2],duration:140,ease:'inOutCubic',onComplete:()=>{
  stopScrollTurn();change();
  const incoming=paperHalf(!right);scrollPaper=incoming;incoming.classList.add('scroll-paper');incoming.style.transformOrigin=right?'right center':'left center';
  scrollTurn=animate(incoming,{rotateY:[-angle,0],opacity:[.2,1],duration:140,ease:'outCubic',onComplete:stopScrollTurn});
 }});
}
document.querySelector('.pages').addEventListener('wheel',event=>{
 const delta=event.deltaY*(event.deltaMode===1?16:event.deltaMode===2?innerHeight:1),direction=Math.sign(delta);
 const target=event.target instanceof Element?event.target:null;
 let eligible=innerWidth>850 && !event.ctrlKey && !event.metaKey && !event.altKey && !event.shiftKey && Math.abs(event.deltaY)>Math.abs(event.deltaX) && !event.defaultPrevented;
 if(target?.closest('input,textarea,select,[contenteditable="true"],[role="dialog"]'))eligible=false;
 for(let node=target;eligible && node && node!==document.querySelector('.pages');node=node.parentElement){
  if(node.scrollHeight>node.clientHeight+1 && /auto|scroll/.test(getComputedStyle(node).overflowY) && (direction>0?node.scrollTop+node.clientHeight<node.scrollHeight-2:node.scrollTop>2))eligible=false;
 }
 const root=document.scrollingElement,edge=direction>0?(root.scrollTop+innerHeight>=root.scrollHeight-3?1:0):(root.scrollTop<=3?-1:0);
 const position=spreadPosition(),last=publicBook?recipes.length+2:recipes.length-1;
 const canTurn=direction>0?position<last:position>0;
 const turn=scrollGesture.update({delta,time:event.timeStamp,edge,eligible:eligible && canTurn,busy:!!scrollTurn});
 if(eligible && canTurn && (turn||scrollGesture.locked||scrollTurn))event.preventDefault();
 if(turn){smoothScroll?.scrollTo(smoothScroll.actualScroll,{immediate:true,force:true});turnFromScroll(turn);}
},{passive:false});
reduced.addEventListener('change',()=>{if(reduced.matches)stopScrollTurn();syncSmoothScroll();});
function keepSelectedRecipeVisible(){
 const nav=$('recipe-index'),active=nav.querySelectorAll('.recipe-tab')[selected];
 if(innerWidth>850 && active){const box=active.getBoundingClientRect(),viewport=nav.getBoundingClientRect();if(box.bottom>viewport.bottom)nav.scrollTop+=box.bottom-viewport.bottom;if(box.top<viewport.top)nav.scrollTop-=viewport.top-box.top;}
}
function placeDish(){
 document.querySelectorAll('.recipe-spread .page').forEach(page=>{
  if(innerWidth>850)page.setAttribute('tabindex','0');else page.removeAttribute('tabindex');
 });
 const hero=document.querySelector('.hero-illustration');
 const anchor=document.querySelector(innerWidth>850?'.method-section':'#recipe-summary');
 anchor.before(hero);
}
placeDish();
let desktopScroll=innerWidth>850;addEventListener('resize',()=>{const desktop=innerWidth>850;if(desktop!==desktopScroll){desktopScroll=desktop;stopScrollTurn();placeDish();keepSelectedRecipeVisible();syncSmoothScroll();}});
syncSmoothScroll();
// Direct navigation can interrupt an unfinished physical page turn.
document.querySelector('.cover').addEventListener('click',stopScrollTurn);
syncText();if(publicBook && bookPage!=='recipe')showBookPage(bookPage,false,false);else displayRecipe(false);
document.documentElement.classList.add('book-ready');
// A single restrained book-opening gesture; never a looping decoration.
animate(document.querySelector('.pages'),{opacity:[0,1],rotateY:[-2,0],duration:600,ease:'outCubic'});
if(parent!==window && !data.remote){
 const id='cookbook-init';
 addEventListener('message',event=>{if(event.source===parent&&event.data?.jsonrpc==='2.0'&&event.data.id===id&&event.data.result)parent.postMessage({jsonrpc:'2.0',method:'ui/notifications/initialized'},'*');});
 parent.postMessage({jsonrpc:'2.0',id,method:'ui/initialize',params:{protocolVersion:'2026-01-26',appInfo:{name:'cookbook-sidebar',version:data.version},appCapabilities:{}}},'*');
}
/*COOKBOOK_REMOTE*/
})();
