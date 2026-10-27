// Included inside the shared book closure only in the separate remote runtime.
if(data.remote){
 const words={en:{search:'Find a workflow',submit:'Search',all:'All recipes',matches:'Matching recipes',empty:'No matching workflows.',loading:'Loading…',error:'Could not load Cookbook. Try again.',instructions:'Full workflow instructions',copy:'Copy instructions',copied:'Copied',source:'Instructions are provided in their source language. Execution needs your host tools and authorization.'},de:{search:'Workflow finden',submit:'Suchen',all:'Alle Rezepte',matches:'Passende Rezepte',empty:'Keine passenden Workflows.',loading:'Wird geladen…',error:'Cookbook konnte nicht geladen werden. Versuche es erneut.',instructions:'Vollständige Workflow-Anleitung',copy:'Anleitung kopieren',copied:'Kopiert',source:'Die Anleitung wird in ihrer Ausgangssprache bereitgestellt. Die Ausführung benötigt deine Host-Werkzeuge und Autorisierung.'}};
 const text=()=>words[language]||words.en;
 const apiLanguage=()=>language==='de'?'de':'en';
 const form=document.createElement('form');form.className='remote-search';
 const label=document.createElement('label');label.htmlFor='remote-query';
 const input=document.createElement('input');input.id='remote-query';input.type='search';input.maxLength=500;
 const submit=document.createElement('button');submit.type='submit';
 const reset=document.createElement('button');reset.type='button';
 const status=document.createElement('p');status.setAttribute('role','status');
 const results=document.createElement('div');results.className='remote-results';
 let resultIds=[];
 form.append(label,input,submit,reset,status,results);$('recipe-index').before(form);
 const panel=document.createElement('section');panel.className='remote-instructions';
 const heading=document.createElement('h2'),note=document.createElement('p'),copy=document.createElement('button');copy.type='button';copy.disabled=true;
 const instructionStatus=document.createElement('p');instructionStatus.setAttribute('role','status');
 const instructions=document.createElement('pre');instructions.tabIndex=0;
 panel.append(heading,note,copy,instructionStatus,instructions);
 document.querySelector('.invocation-card').hidden=true;
 document.querySelector('.invocation-card').before(panel);
 const style=document.createElement('style');
 style.textContent='.remote-search{display:grid;grid-template-columns:1fr 1fr;gap:.5rem;padding:1rem;flex-shrink:0}.remote-search label,.remote-search input,.remote-search p,.remote-results{grid-column:1/-1}.remote-search p:empty{display:none}.remote-search input{min-width:0;width:100%;padding:.5rem;font:inherit;color:inherit;background:transparent;border:1px solid currentColor;border-radius:.3rem}.remote-search button,.remote-instructions button{font:inherit;color:inherit;background:transparent;border:1px solid currentColor;border-radius:.3rem;padding:.4rem;cursor:pointer}.remote-results{display:grid;gap:.35rem;max-height:9rem;overflow:auto}.remote-instructions pre{white-space:pre-wrap;overflow-wrap:anywhere;max-height:24rem;overflow:auto;font-size:.8rem;line-height:1.5}.remote-instructions h2{font-size:1.2rem}.remote-instructions p{font-size:.85rem}.invocation-card[hidden]{display:none}';
 document.head.append(style);
 function labels(){label.textContent=text().search;submit.textContent=text().submit;reset.textContent=text().all;heading.textContent=text().instructions;instructions.setAttribute('aria-label',text().instructions);note.textContent=text().source;copy.textContent=text().copy;results.setAttribute('aria-label',text().matches);}
 const pending=new Map();let nextId=0, selectionRequest=0, searchRequest=0, currentWorkflow=null;
 let ready=parent===window;
 function request(method,params){
  if(parent===window){
   // Standalone preview uses only this local server, never a URL supplied by a result.
   return fetch('/mcp',{method:'POST',headers:{'Content-Type':'application/json','Accept':'application/json, text/event-stream','MCP-Protocol-Version':'2025-11-25'},body:JSON.stringify({jsonrpc:'2.0',id:++nextId,method,params})})
    .then(async response=>{if(!response.ok)throw Error('MCP request failed');const reply=await response.json();if(reply.error)throw Error('MCP protocol error');return reply.result;});
  }
  return new Promise((resolve,reject)=>{
   const id='cookbook-remote-'+(++nextId);
   const timer=setTimeout(()=>{pending.delete(id);reject(Error('Host did not respond'));},10000);
   pending.set(id,{resolve,reject,timer});parent.postMessage({jsonrpc:'2.0',id,method,params},'*');
  });
 }
 async function tool(name,args){const result=await request('tools/call',{name,arguments:args});if(result?.isError||!result?.structuredContent)throw Error('Tool failed');return result.structuredContent;}
 function showResults(rows){
  resultIds=rows.map(row=>row.id).filter(id=>recipes.some(recipe=>recipe.id===id));
  results.replaceChildren();
  resultIds.forEach(id=>{const index=recipes.findIndex(recipe=>recipe.id===id);
   const button=document.createElement('button');button.type='button';button.dataset.recipeId=id;button.textContent=recipeName(recipes[index]);button.addEventListener('click',()=>{if(index===selected)loadWorkflow(id);else chooseRecipe(index,false);});results.append(button);
  });
  status.textContent=resultIds.length?'':text().empty;
 }
 async function loadWorkflow(id){
  const generation=++selectionRequest;currentWorkflow=null;copy.disabled=true;instructions.textContent='';instructionStatus.textContent=text().loading;
  try{const result=await tool('get_workflow',{id,language:apiLanguage()});
   if(generation!==selectionRequest)return;
   if(result.workflow?.id!==id||typeof result.workflow.instructions!=='string')throw Error('Unexpected workflow');
   currentWorkflow=result.workflow;instructions.textContent=currentWorkflow.instructions;instructionStatus.textContent='';copy.disabled=false;
  }catch{if(generation===selectionRequest)instructionStatus.textContent=text().error;}
 }
 function applySelection(value){
  if(!value||!Array.isArray(value.workflowIds))return;
  if(value.language==='en'||value.language==='de'){language=value.language;syncText();labels();}
  const ids=value.workflowIds.filter(id=>typeof id==='string'&&recipes.some(recipe=>recipe.id===id));
  showResults(ids.map(id=>({id})));
  const index=recipes.findIndex(recipe=>recipe.id===value.selectedId&&ids.includes(recipe.id));
  if(index>=0){if(index===selected)loadWorkflow(recipes[index].id);else chooseRecipe(index,false);}
 }
 form.addEventListener('submit',async event=>{
  event.preventDefault();const generation=++searchRequest;submit.disabled=true;status.textContent=text().loading;
  try{const result=await tool('search_workflows',{query:input.value,limit:18,language:apiLanguage()});if(generation===searchRequest)showResults(result.workflows);}
  catch{if(generation===searchRequest)status.textContent=text().error;}
  finally{if(generation===searchRequest)submit.disabled=false;}
 });
 reset.addEventListener('click',()=>{input.value='';form.requestSubmit();});
 copy.addEventListener('click',async()=>{
  if(!currentWorkflow)return;
  try{await navigator.clipboard.writeText(currentWorkflow.instructions);instructionStatus.textContent=text().copied;}catch{instructionStatus.textContent=text().error;}
 });
 document.addEventListener('cookbook:recipe',event=>{
  results.querySelectorAll('button').forEach(button=>{const recipe=recipes.find(recipe=>recipe.id===button.dataset.recipeId);if(recipe)button.textContent=recipeName(recipe);});
  if(ready)loadWorkflow(event.detail.id);
 });
 $('language-options').addEventListener('click',()=>{labels();if(ready)loadWorkflow(recipes[selected].id);});
 addEventListener('message',event=>{
  if(parent===window||event.source!==parent||event.data?.jsonrpc!=='2.0')return;
  const message=event.data;
  if(pending.has(message.id)){const item=pending.get(message.id);pending.delete(message.id);clearTimeout(item.timer);if(message.error)item.reject(Error('Host error'));else item.resolve(message.result);return;}
  if(message.method==='ui/notifications/tool-result')applySelection(message.params?.structuredContent);
 });
 labels();
 if(parent!==window){
  request('ui/initialize',{protocolVersion:'2026-01-26',appInfo:{name:'cookbook-remote',version:data.version},appCapabilities:{}})
   .then(()=>{ready=true;parent.postMessage({jsonrpc:'2.0',method:'ui/notifications/initialized'},'*');if(!currentWorkflow)loadWorkflow(recipes[selected].id);})
   .catch(()=>{instructionStatus.textContent=text().error;});
 }else loadWorkflow(recipes[selected].id);
}
