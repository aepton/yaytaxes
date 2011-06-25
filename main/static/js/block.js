$(document).ready(function(){
	
	$(".block").bind("load",function(event){
		block = $(this);
		
		block.html("");
		
		block.append('<div class="buildings"></div>');
		for(var i=0;i<5;i++){
			$(".buildings",block).append('<div class="building"></div>');
		}
		$(".building:random",block).addClass("bad");
		$(".building:not(.bad):random",block).addClass("worse");
		$(".building:not(.bad,.worse):random",block).addClass("mcdonalds");
		
		
		block.append('<div class="sidewalk"></div>');
		
		block.append('<div class="road"></div>');
		
		switch(event.block.infrastructure){
			case "bus":
				$(".road",block).append('<div class="bus"></div>');
			case "road":
				$(".road",block).addClass("asfault");
				$(".sidewalk",block).addClass("concrete");
				break;
			case "cobblestone":
				$(".road",block).addClass("cobblestone");
				$(".sidewalk",block).addClass("cobblestone");
				break;
		}
		
		
		if(event.block.goverment == "bad"){
			$(".sidewalk",block).addClass("bad");
		}
		
		if(event.block.environment == "trees"){
			// sidewalk sq is 64px
			num_trees = Math.floor($(".sidewalk",block).width()/(64*3));
			for(var i=0;i<num_trees;i++){
				$(".sidewalk",block).append('<div class="tree"></div>');
			}
		}
		if(event.block.environment == "shrub"){
			// sidewalk sq is 64px
			num_trees = Math.floor($(".sidewalk",block).width()/(64*3));
			for(var i=0;i<num_trees;i++){
				$(".sidewalk",block).append('<div class="shrub"></div>');
			}
		}
		
		if(event.block.environment == "bad"){
			$(".building:not(.bad.worse):random",block).addClass("worse");
			// sidewalk sq is 64px
			num_trees = Math.floor($(".sidewalk",block).width()/(64*6));
			for(var i=0;i<num_trees;i++){
				$(".sidewalk",block).append('<div class="trash"></div>');
			}
		}
		
	});
	
	
});

var my_block = {
	infastructure:"bus",
	environment:"bad",
	goverment:"bad",
	
}