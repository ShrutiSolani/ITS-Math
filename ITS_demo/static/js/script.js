document.querySelector('.img-btn').addEventListener("click", myfunction);
function myfunction() {
	document.querySelector('.cont').classList.toggle('s-signup')
}

function myalertsignup() {
	alert("Sign Up Successful");
}

function myalertlogin() {
	alert("Login Successful");
}

 $(document).ready(function(){
	$("#teacher").click(function(){
	  $("#teacher1").hide();
	});
	$("#teacher").click(function(){
	  $("#student1").show();
	});
  });

  $(document).ready(function(){
	$("#student").click(function(){
	  $("#student1").hide();
	});
	$("#student").click(function(){
	  $("#teacher1").show();
	});
  });