$(document).ready(function(){
	
	$("form#taxes").delegate(".slider","slidechange",function(event,ui){
		slider = $(this)
		formRow = slider.parent(".formRow");
		try{
			$("input",formRow).val(ui.value);
			$(".precent",formRow).html("$"+$().number_format(ui.value,{numberOfDecimals:0,thousandSeparator: ','}));
		}catch(e){}
		$("#taxes").trigger("update");
	});
	
	
	
	$("form#taxes").submit(function(event){
		event.preventDefault();
		
		settings = {};
		
		infrastructure = $("input[name=infrastructure]").val();
		if(infrastructure > 15){
			settings['infrastructure'] = 'bus';
		}else if(infrastructure > 10){
			settings['infrastructure'] = 'road';
		}else if(infrastructure > 3){
			settings['infrastructure'] = 'cobblestone';
		}else{
			settings['infrastructure'] = 'bad';
		}
		
		
		$(".block").trigger({
			type:"load",
			block:settings,
		})
		
	}).bind("load",function(event){
		event.stopPropagation();
		
		total_budget = 0;
		total_budget += $("#income input[name=25k]").val()*3500000;
		total_budget += $("#income input[name=60k]").val()*3700000;
		total_budget += $("#income input[name=100k]").val()*2500000;
		total_budget += $("#income input[name=200k]").val()*750000;
		
		$(this).data("total_budget",total_budget);
		
		$("form#taxes .slider").slider({
			max:total_budget,
			min:0
			}).parents(".formRow").append('<span class="precent"></span>');
		
		$(".formRow",$(this)).each(function(){
			$("input:not([type=submit])").val("0");
			$(".slider").slider("option","value",$("input").val()).trigger("slidechange")
		});
		$(this).trigger("update");
		
	}).bind("update",function(event){
		total_budget = $(this).data("total_budget");
		
		total_spent = 0;
		inputs = $("#taxes input:not([type=submit])")
		for(var i=0;i<inputs.length;i++){
			total_spent += parseInt($(inputs[i]).val())
		}
		
		$(".total",$(this)).html("$"+$().number_format(total_budget,{numberOfDecimals:0,thousandSeparator: ','}));
		$(".left",$(this)).html("$"+$().number_format(total_budget - total_spent,{numberOfDecimals:0,thousandSeparator: ','}));
	});
});