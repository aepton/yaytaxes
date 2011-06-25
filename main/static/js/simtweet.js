$(document).ready(function(event){
	
	$("#display").delegate(".block","get_tweet",function(event){
		block = $(this);
		// get tweet from impact
		
		// add tweet
		block.append('<div class="tweet"><span class="from">Jerry</span><span class="message">This is a really cool message.</span><span class="bear"></span></div>');
		now = new Date()
		$(".tweet:last",block).css("top","200px").animate({top:"25"},{duration:7000,complete:function(event){
			tweet = $(this);
			tweet.parent(".block").trigger("get_tweet");
			tweet.hide().remove();
		}});
	});
	
	setInterval('$(".block .tweet").trigger("update")',50);
})