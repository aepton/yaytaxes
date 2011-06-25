$(document).ready(function(){
	
	$("#display,#taxes").hide();
	
	$("#income").trigger("start");
	
	$(window).resize(function(){
		$("#display").css("padding-top",$(window).height()-$("#display").height());
	}).resize();
});