$(document).ready(function(){
	
	$("#display,#taxes").hide();
	
	$("#income input[name=25k]").val("230")
	$("#income input[name=60k]").val("3000")
	$("#income input[name=100k]").val("20000")
	$("#income input[name=200k]").val("70000")
	$("#taxes").show().trigger("load");
	$("#display").show();
	$("#display .block").trigger({
		type:"load",
		block:my_block
	});
	
	//$("#income").trigger("start");
	$("#income").hide();
});