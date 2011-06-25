$(document).ready(function(){
	
	$("form#income").bind("start",function(event){
		form = $(this);
		$(".page input",form).val("");
		$(".page",form).hide();
		$(".page:first").show();
	}).bind("next",function(event){
		if($(".page:visible",$(this)).length>0){
			if($(".page:visible",$(this))[0]==$(".page:last",$(this))[0]){
				
				// show blocks and sliders
				$("#taxes").show().trigger("load");
				$("#display").show();
				$("#display .block").trigger({
					type:"load",
					block:my_block
				});
			}
			$(".page:visible",$(this)).hide().next(".page").show();
		}
	});
	
	$("form#income .page .next").click(function(event){
		event.preventDefault()
		$("form#income").trigger("next");
	})
	
});