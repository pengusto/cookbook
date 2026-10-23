// Sustained scrolling can keep turning, at a readable pace. Decaying momentum cannot.
class BookScrollGesture {
 constructor(){this.total=0;this.last=-Infinity;this.turnedAt=-Infinity;this.locked=false;}
 update({delta,time,edge,eligible=true,busy=false}){
  if(time-this.last>220){this.total=0;this.locked=false;}
  this.last=time;
  if(!eligible||!edge||Math.sign(delta)!==edge){this.total=0;this.locked=false;return 0;}
  if(busy||time-this.turnedAt<650){this.total=0;return 0;}
  // Ignore the low-amplitude tail of a trackpad fling after its first turn.
  if(this.locked&&Math.abs(delta)<12){this.total=0;return 0;}
  if(Math.sign(this.total)!==Math.sign(delta))this.total=0;
  this.total+=delta;
  if(Math.abs(this.total)<(this.locked?160:80))return 0;
  this.total=0;this.locked=true;this.turnedAt=time;return edge;
 }
}
