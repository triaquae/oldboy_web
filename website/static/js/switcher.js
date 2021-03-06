/*-----------------------------------------------------------------------------------
/* Styles Switcher
-----------------------------------------------------------------------------------*/

window.console = window.console || (function(){
	var c = {}; c.log = c.warn = c.debug = c.info = c.error = c.time = c.dir = c.profile = c.clear = c.exception = c.trace = c.assert = function(){};
	return c;
})();


jQuery(document).ready(function($) {
	
        // Style Switcher	
		$('#style-switcher').animate({
	//		right: '-300px'
		});
		
		$('#style-switcher h2 a').click(function(e){
			e.preventDefault();
			var div = $('#style-switcher');
			console.log(div.css('right'));
			if (div.css('right') === '-200px') {
				$('#style-switcher').animate({
					right: '0px'
				}); 
			} else {
				$('#style-switcher').animate({
					right: '-200px'
				});
			}
		})
                
		// Color Changer

		$("#layout-switcher").on('change', function() {
			$('#layout').attr('href', $(this).val() + '.css');
		});;
		$('.colors li a').click(function(e){
			e.preventDefault();
			$(this).parent().parent().find('a').removeClass('active');
			$(this).addClass('active');
		})
		
	
		$('.bg li a').click(function(e){
			e.preventDefault();
			$(this).parent().parent().find('a').removeClass('active');
			$(this).addClass('active');
			var bg = $(this).css('backgroundImage');
			$('body').css('backgroundImage',bg)
		})
                
		
		$('.bgsolid li a').click(function(e){
			e.preventDefault();
			$(this).parent().parent().find('a').removeClass('active');
			$(this).addClass('active');
			var bg = $(this).css('backgroundColor');
			$('body').css('backgroundColor',bg).css('backgroundImage','none')
		})
                
		$('.navcolor li a').click(function(e){
			e.preventDefault();
			$(this).parent().parent().find('a').removeClass('active');
			$(this).addClass('active');
			var bg = $(this).css('backgroundColor');
			$('#navigation').css('backgroundColor',bg).css('backgroundImage','none');
			$('#navigation ul ul').css('backgroundColor',bg).css('backgroundImage','none');
                        
		})
		
		
		$('#reset a').click(function(e){
			var bg = $(this).css('backgroundImage');
			$('body').css('backgroundImage','url(./images/bg/noise.png)');
                        $('#navigation').css('backgroundColor','#333');
			$('#navigation ul ul').css('backgroundColor','#333');
                        $("#layout" ).attr("href", "css/wide.css" );
		})
			

	});
