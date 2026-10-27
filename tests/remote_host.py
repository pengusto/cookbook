"""Local MCP Apps test host; not shipped in the remote runtime.

Run after building: python3 tests/remote_host.py --port 8768
This exercises the real iframe message bridge but is not OpenAI host acceptance.
"""
import argparse
from functools import partial
from http.server import ThreadingHTTPServer
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'scripts'))
from remote_server import Cookbook, Handler


HTML = '''<!doctype html><html lang="en"><meta charset="utf-8">
<title>Cookbook local MCP Apps test host</title>
<style>body{margin:0;font:16px system-ui}header{padding:8px}iframe{width:100%;height:85vh;border:0}</style>
<header><strong>Local MCP Apps test host</strong>
<button id="select">Open release recipe</button><button id="empty">Empty selection</button>
<button id="invalid">Unknown recipe</button><button id="fail">Fail next tool call</button>
<label>Width <select id="width"><option>100%</option><option>390px</option></select></label>
<p id="status" role="status">Waiting for initialization</p></header>
<iframe id="book" title="Cookbook test app" src="/preview" allow="clipboard-write"></iframe>
<script>
const frame=document.getElementById('book'),status=document.getElementById('status');
let sequence=0,failNext=false;
async function call(name,args){
 const response=await fetch('/mcp',{method:'POST',headers:{'Content-Type':'application/json',Accept:'application/json, text/event-stream','MCP-Protocol-Version':'2025-11-25'},body:JSON.stringify({jsonrpc:'2.0',id:++sequence,method:'tools/call',params:{name,arguments:args}})});
 return (await response.json()).result;
}
function send(value){frame.contentWindow.postMessage(value,location.origin);}
addEventListener('message',async event=>{
 if(event.source!==frame.contentWindow||event.origin!==location.origin||event.data?.jsonrpc!=='2.0')return;
 const message=event.data;
 if(message.method==='ui/initialize'){
  send({jsonrpc:'2.0',id:message.id,result:{protocolVersion:'2026-01-26',hostInfo:{name:'local-test-host',version:'1'},hostCapabilities:{serverTools:{}}}});
 }else if(message.method==='ui/notifications/initialized'){status.textContent='App initialized';}
 else if(message.method==='tools/call'){
  if(failNext){failNext=false;send({jsonrpc:'2.0',id:message.id,error:{code:-32603,message:'Synthetic test failure'}});return;}
  const result=await call(message.params.name,message.params.arguments);
  send({jsonrpc:'2.0',id:message.id,result});
 }
});
document.getElementById('select').onclick=async()=>{
 const result=await call('open_cookbook',{workflow_ids:['ready-to-serve','keep-the-recipe-secret'],selected_id:'ready-to-serve',language:'en'});
 send({jsonrpc:'2.0',method:'ui/notifications/tool-result',params:result});
 status.textContent='Release selection sent';
};
document.getElementById('empty').onclick=()=>send({jsonrpc:'2.0',method:'ui/notifications/tool-result',params:{structuredContent:{workflowIds:[],selectedId:null,language:'en'}}});
document.getElementById('invalid').onclick=()=>send({jsonrpc:'2.0',method:'ui/notifications/tool-result',params:{structuredContent:{workflowIds:['not-a-recipe'],selectedId:'not-a-recipe'}}});
document.getElementById('fail').onclick=()=>{failNext=true;status.textContent='Next tool call will fail';};
document.getElementById('width').onchange=event=>frame.style.width=event.target.value;
</script></html>'''


class TestHost(Handler):
    html_csp = Handler.html_csp + "; frame-src 'self'"

    def do_GET(self):
        if self.path == '/test-host':
            if self.safe_request():
                self.respond(200, HTML, 'text/html')
        else:
            super().do_GET()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--port', type=int, default=8768)
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1] / 'dist/remote/kitchen'
    with ThreadingHTTPServer(('127.0.0.1', args.port), partial(TestHost, cookbook=Cookbook(root))) as server:
        print(f'Local test host: http://127.0.0.1:{server.server_port}/test-host', flush=True)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
