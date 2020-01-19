window.onload = function() {
  document.getElementById("form1").onsubmit = function () {
    var numdrive = document.getElementById("a");
    var nummiles = document.getElementById("b");
    var numdays = document.getElementById("c");
    var numyears = document.getElementById("d");
	document.write =(numdrive*nummiles*numdays*numyears*2*404 + "acres of trees")
  };
};