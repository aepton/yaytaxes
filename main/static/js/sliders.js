$(document).ready(function(){
	
	$("form#taxes").delegate(".slider","slidechange",function(event,ui){
		slider = $(this)
		formRow = slider.parent(".formRow");
		try{
			$("input",formRow).val(ui.value);
			$(".precent",formRow).html(formatNumber(ui.value));
		}catch(e){}
		$("#taxes").trigger("update");
	});
	
	
	
	$("form#taxes").submit(function(event){
		event.preventDefault();
		
		
		// get via json
		data = {"artsAndMusicAvailable": false, "healthFat": 5, "treesCount": 3, "businessLevel": 2, "fireworksAvailable": false, "awesomeGradRatesAvailable": false, "policeAvailable": true, "healthSmoker": 5, "foodStandsCount": 4, "sportsTeamAvailbale": true, "roadType": 4, "foodStandsAvailable": true, "parkAvailable": true, "treesAvailable": true, "bushesAvailable": true, "marketAvailable": true, "multiplier": 4, "schoolAvailable": true, "gangCount": 0, "peopleCount": 0, "libraryAvailable": true, "scienceFairAvailable": false, "healthGood": 5, "marketWithProduce": true}
		settings = {};
		


		
		$(".block").trigger({
			type:"load",
			block:data,
		})
		
	}).bind("load",function(event){
		event.stopPropagation();
		
		total_budget = 0;
		total_budget += parseInt($("#income input[name=25k]").val())*3500000;
		total_budget += parseInt($("#income input[name=60k]").val())*3700000;
		total_budget += parseInt($("#income input[name=100k]").val())*2500000;
		total_budget += parseInt($("#income input[name=200k]").val())*750000;
		
		$(this).data("total_budget",total_budget);
		
		$("form#taxes .slider").slider({
			max:(total_budget/2),
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
		
		$(".total",$(this)).html(formatNumber(total_budget));
		$(".left",$(this)).html(formatNumber(total_budget - total_spent));
	});
});

function formatNumber(num){
	return "$"+$().number_format(num/1000000000,{numberOfDecimals:2,thousandSeparator: ','})+" billion";
}