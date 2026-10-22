(() => {
'use strict';
const data = JSON.parse(document.getElementById('cookbook-data').textContent);
const locales = data.locales, recipes = data.recipes;
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
const requested = recipes.findIndex(recipe => recipe.id === location.hash.slice(1));
if (requested >= 0) selected = requested;
function icon(name) { const svg=document.createElementNS('http://www.w3.org/2000/svg','svg'); svg.setAttribute('aria-hidden','true');const use=document.createElementNS(svg.namespaceURI,'use');use.setAttribute('href','#'+name);svg.append(use);return svg; }
function animate(target, options) {
 if (reduced.matches || !window.anime) return null;
 return window.anime.animate(target, options);
}
function syncText() {
 const t=locales[language];
 document.documentElement.lang=language;
 document.documentElement.dir=language==='ar'?'rtl':'ltr';
 document.querySelectorAll('[data-i18n]').forEach(node => node.textContent=t[node.dataset.i18n]);
 $('current-language').textContent=t.name;
 document.querySelector('.edition').textContent=naming==='kitchen'?'Kitchen edition':t.plainNames;
 document.querySelectorAll('[data-naming]').forEach(button=>button.setAttribute('aria-pressed',String(button.dataset.naming===naming)));
 document.querySelectorAll('.recipe-label').forEach((label,index)=>label.textContent=recipeName(recipes[index]));
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
 const recipe=recipes[selected], t=locales[language];
 const number=String(selected+1).padStart(2,'0');
 $('recipe-number').textContent=number; $('page-number').textContent=number;
 $('recipe-title').textContent=recipeName(recipe);
 $('recipe-emblem').setAttribute('href','#recipe-'+recipe.icon);
 $('recipe-total').textContent=String(recipes.length).padStart(2,'0');
 $('alternate-name').textContent=(naming==='kitchen'?t.plainNames:'Kitchen')+': '+recipe.names[naming==='kitchen'?'plain':'kitchen'];
 $('installed-invocation').textContent=t.installedInvocation+' · '+(data.variant==='kitchen'?'Kitchen':t.plainNames);
 const accent=document.documentElement.dataset.theme==='dark'?recipe.accentDark:recipe.accent;
 document.querySelector('.pages').style.setProperty('--recipe-accent',accent);
 document.querySelector('.cover').style.setProperty('--recipe-accent',accent);
 $('pan-art').src=recipe.art;
 $('pan-art').dataset.recipe=recipe.id;
 $('recipe-announcement').textContent=t.recipe+' '+number+': '+recipeName(recipe);
 $('recipe-summary').textContent=t.summaries.split('|')[selected];
 $('recipe-intro').textContent=t.intros.split('|')[selected];
 $('recipe-when').textContent=t.whenList.split('|')[selected];
 const ingredients=t.ingredientLists[selected];
 $('ingredient-list').replaceChildren(...ingredients.map(text=>{const li=document.createElement('li');li.textContent=text;return li;}));
 const steps=t['steps'+selected].split('|');
 $('method-list').replaceChildren(...steps.map((title,index)=>{
   const li=document.createElement('li'), copy=document.createElement('div'),h3=document.createElement('h3'),p=document.createElement('p'),art=document.createElement('span');
   h3.textContent=title; p.textContent=(t['stepNotes'+selected]||t.stepNotes)[index]; copy.append(h3,p);
   art.className='step-art art'+index; art.setAttribute('aria-hidden','true');li.append(copy,art);return li;
 }));
 $('invocation').textContent='$'+recipe.id;
 $('limits-copy').textContent=t.verifications[selected]+' '+t.limitText+' '+t.recipeLimits[selected];
 $('copy-status').textContent=t.languageNote;
 $('copy-command').setAttribute('aria-label',t.copy+' '+recipeName(recipe));
 clearTimeout(copyTimer);
 $('previous-recipe').disabled=selected===0;
 $('next-recipe').disabled=selected===recipes.length-1;
 document.querySelectorAll('.recipe-tab').forEach((button,index)=>button.setAttribute('aria-current',String(index===selected)));
 const nav=$('recipe-index'),active=nav.children[selected];
 if(innerWidth>850 && active){const box=active.getBoundingClientRect(),viewport=nav.getBoundingClientRect();if(box.bottom>viewport.bottom)nav.scrollTop+=box.bottom-viewport.bottom;if(box.top<viewport.top)nav.scrollTop-=viewport.top-box.top;}
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
 try {history.replaceState(null,'','#'+recipe.id);} catch { /* Host iframe can disallow history access. */ }
}
function chooseRecipe(index,focus=false) {
 if(index<0 || index>=recipes.length || index===selected) return;
 selected=index; displayRecipe();
 if(focus) $('recipe-title').focus({preventScroll:true});
 if(innerWidth<=560) document.querySelector('.recipe-tab[aria-current=true]').scrollIntoView({block:'nearest',inline:'nearest',behavior:reduced.matches?'instant':'smooth'});
}
recipes.forEach((recipe,index)=>{
 const button=document.createElement('button');button.type='button';button.className='recipe-tab';
 const number=document.createElement('span');number.className='index-number';number.textContent=String(index+1).padStart(2,'0');number.setAttribute('aria-hidden','true');
 const label=document.createElement('span');label.dir='ltr';label.className='recipe-label';label.textContent=recipeName(recipe);button.append(number,icon('recipe-'+recipe.icon),label);
 button.addEventListener('click',()=>chooseRecipe(index));
 button.addEventListener('keydown',event=>{let next=null;if(event.key==='ArrowDown') next=Math.min(recipes.length-1,index+1);if(event.key==='ArrowUp') next=Math.max(0,index-1);if(event.key==='Home')next=0;if(event.key==='End')next=recipes.length-1;if(next!==null){event.preventDefault();chooseRecipe(next);$('recipe-index').children[next].focus();}});
 $('recipe-index').append(button);
});
document.querySelectorAll('[data-naming]').forEach(button=>button.addEventListener('click',()=>{naming=button.dataset.naming;try{localStorage.setItem('cookbook-naming',naming);}catch{}syncText();displayRecipe(false);}));
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
 button.addEventListener('click',()=>{language=code;try{localStorage.setItem('cookbook-language',code);}catch{}syncText();displayRecipe(false);closeLanguages(true);});$('language-options').append(button);
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
  animate($('copy-command'),{scale:[1,.83,1],duration:280,ease:'outCubic'});
 } catch {
  const selection=window.getSelection(),range=document.createRange();range.selectNodeContents($('invocation'));selection.removeAllRanges();selection.addRange(range);$('copy-status').textContent=t.copyManual;
 }
 clearTimeout(copyTimer);copyTimer=setTimeout(()=>$('copy-status').textContent=locales[language].languageNote,3000);
});
reduced.addEventListener('change',()=>{if(reduced.matches){if(animation){animation.revert();animation=null;}if(pageTurn){pageTurn.pause();pageTurn=null;}document.querySelectorAll('.page-turn-leaf').forEach(node=>node.remove());}});
syncText();displayRecipe(false);
// A single restrained book-opening gesture; never a looping decoration.
animate(document.querySelector('.pages'),{opacity:[0,1],rotateY:[-2,0],duration:600,ease:'outCubic'});
if(parent!==window){
 const id='cookbook-init';
 addEventListener('message',event=>{if(event.source===parent&&event.data?.jsonrpc==='2.0'&&event.data.id===id&&event.data.result)parent.postMessage({jsonrpc:'2.0',method:'ui/notifications/initialized'},'*');});
 parent.postMessage({jsonrpc:'2.0',id,method:'ui/initialize',params:{protocolVersion:'2026-01-26',appInfo:{name:'cookbook-sidebar',version:data.version},appCapabilities:{}}},'*');
}
})();
