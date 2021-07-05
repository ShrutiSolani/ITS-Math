$(function() {
    var canvas = $('canvas')[0];
    var ctx = canvas.getContext('2d');
  
    var w = canvas.width = 700;
    var h = canvas.height = 400;
    var x0 = w/2;
    var starti=0;
    var endi=1;
    var interval = 200;
    // var step = 0.1;
    // var steps = 10;
   
    
    function drawOperation(x){
      drawPoint(x);
      // for(var i = 0; i < steps; i++){
      //   drawCurve(x+i*step*interval,x+(i+1)*step*interval);
      // }
      // drawPoint(x+steps*step*interval);
    }
   
    canvas.addEventListener("mousedown", getPosition, false);
    function drawPoint(x1){
        ctx.beginPath();
        ctx.arc(x1,h/2,2,0,2*Math.PI);
        ctx.fill();
        ctx.stroke();
    }
    // function drawArc(p1,dir){
     
    // }
    function getPosition(e){
      var x = e.clientX;
      console.log("x"+ x);
      var xe = x-(x%20) + 10;
      console.log("xe" + xe);
      // console.log("% "+ (x%interval));
      if(x0===0){  
        drawPoint(xe);
        x0=xe;
      }
      else{
        drawPoint(xe);
        // drawCurve(x0,xe);
        x0=xe;
      }
      
    }
    // function getPosition(e){
    //   var x = e.clientX;
    //   console.log(x);
    //   var xe = (x-x%interval);
    //   // drawPoint(xe);
    //   if(x0===0){  
    //     drawPoint(xe);
    //     x0=xe;
    //   }
    //   else{
    //     drawPoint(xe);
    //     drawCurve(x0,xe);
    //     x0=xe;
    //   }
      
    // }
    // function drawCurve(x1,x2){
    //   ctx.moveTo(x1,h/2);
    //   ctx.quadraticCurveTo(x1+(x2-x1)/2,h/2-Math.abs(x2-x1),x2,h/2);
    //   var text;
    //   var s = (x2 - x1)/interval;
    //   if(s>0){
    //     text="+" +s.toString();
    //   }
    //   else {
    //     text = (x2 - x1)/interval;
    //   }
    //   ctx.fillText(text,x1+(x2-x1)/2,h/2-Math.abs(x2-x1)*0.5-10);
      
    //   ctx.stroke();
    // }
    with(ctx) {
      
      fillStyle = '#FFFFFF';
      fillRect(0, 0, w, h);
      fill();
      beginPath();
      lineWidth = 2;
      strokeStyle = '#71C9CE';
      moveTo(w/7, h/2);
      lineTo(6*w/7, h/2);
      stroke();  
      moveTo(w/7, h/2);
      lineTo(w/7+10, h/2+10);
      stroke();
      moveTo(w/7, h/2);
      lineTo(w/7+10, h/2-10);
      stroke();
      moveTo(6*w/7, h/2);
      lineTo(6*w/7-10, h/2+10);
      stroke();
      moveTo(6*w/7, h/2);
      lineTo(6*w/7-10, h/2-10);
      stroke();
   
      for(var i = starti;i <= endi; i=i+0.1) {
        beginPath();
        strokeStyle = '#CE1212';
        lineWidth = 2;
        moveTo(w/2 + i * interval, h/2 - 10);
        lineTo(w/2 + i * interval, h/2 + 10);
        fillStyle = '#71C9CE';
        fillText(Math.round( i * 10 ) / 10, (w/2 + i * interval )- 5, h/2 + 25);
        if(!i) {
      
          strokeStyle = '#CE1212';
        }
        fill();
        stroke();
      }
      
    }
    drawOperation(x0);
  });