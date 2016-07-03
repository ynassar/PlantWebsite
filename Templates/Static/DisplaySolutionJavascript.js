
$(document).ready(function(){
   console.log(xList);
   console.log(yList);
   console.log("YO");
   TESTER = document.getElementById('tester');
	Plotly.plot( TESTER, [{
	x: xList,
	y: yList,
    mode: 'markers',
    type: 'scatter',
    }], {
	margin: { t: 0 } } );
});
