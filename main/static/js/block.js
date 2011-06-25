$(document).ready(function(){
	
	$(".block").bind("load",function(event){
		block = $(this);
		
		block.html("");
		
		block.append('<div class="buildings"></div>');
		while($(".buildings").width()<$(".block").width()){
			$(".buildings",block).append('<div class="building"></div>');
		}
		
		$(".buildings").width($(".buildings").width()+250);
		if(event.block.multiplier <= 1){
			$(".buildings").each(function(){
				if(Math.random()*10>5){
					$(".building:not(.bad.worse):random",block).addClass("worse");
				}else{
					$(".building:not(.bad.worse):random",block).addClass("bad");
				}
			});
		}
		
		
		if(event.block.businessLevel>4){
			$(".building:not(.market):random",block).addClass("brownstone");
		}else if(event.block.businessLevel>2){
			
		}else if(event.block.businessLevel<1){
			$(".building:not(.bad):random",block).addClass("worse");
		}
		
		if(event.block.schoolAvailable){
			$(".building:random",block).addClass("school");
		}
		
		block.append('<div class="sidewalk"></div>');
		
		block.append('<div class="road"></div>');
		
		infrastructure = event.block.roadType;
		if(infrastructure >4){
			$(".sidewalk",block).append('<div class="metro"></div>');
		}
		if(infrastructure > 3){
			$(".road",block).append('<div class="bus"></div>');
			$(".road .bus:last").css({left:$(".road").width()}).animate({left:-200},{duration:15000,complete:function(){$(this).hide()}});
		}
		if(infrastructure > 2 ){
			$(".road",block).addClass("asfault");
			$(".sidewalk",block).addClass("concrete");
		}
		if(infrastructure > 1 && infrastructure <= 2){
			$(".road",block).addClass("cobblestone");
			$(".sidewalk",block).addClass("cobblestone");
		}
		
		if(infrastructure < 2 && event.block.multiplier <= 1){
			$(".building.worse:random",block).addClass("onfire");
		}
		
		if(event.block.foodStandsAvailable){
			$(".building:random",block).addClass("market-w-veggies");
		}else if(event.block.markeyAvailable){
			$(".building:random",block).addClass("market");
		}else if(event.block.multiplier >= 1){
			$(".building:random",block).addClass("mcdonalds");
		}
		
		if(event.block.policeAvailable){
			$(".sidewalk",block).append('<div class="firehydrent"></div>');
		}
		
		if(event.block.multiplier <= 1){
			$(".sidewalk",block).addClass("bad");
		}
		
		if(event.block.treesCount > 0){
			for(var i=0;i<event.block.treesCount;i++){
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
		
		if(event.block.multiplier <= 1){
			$(".building:not(.bad.worse):random",block).addClass("worse");
			// sidewalk sq is 64px
			num_trees = Math.floor($(".sidewalk",block).width()/(64*6));
			for(var i=0;i<num_trees;i++){
				$(".sidewalk",block).append('<div class="trash"></div>');
				$(".trash:last",block).css("left",i*2*64+194);
			}
		}
		
	});
	
	
});

var my_block = {
	infastructure:"bus",
	environment:"bad",
	goverment:"bad",
	
}