$(document).ready(function(){
       $('[rel="tooltip"]').tooltip();

                        // fancybox gallery
                        $("a.js-fancybox").fancybox({
                                'transitionIn'  :   'elastic',
                                'transitionOut' :   'elastic',
                                'speedIn'       :   600,
                                'speedOut'      :   200,
                                'overlayShow'   :   true
                        });

});
window.onload = function(){
	var $container = $(".portfolio");
	$container.isotope({
		filter: "*",
		animationOptions: {
			duration: 750,
			easing: 'linear',
			queue: false,
		}
	});
	// isotope filter button
	$(".filter a").click(function() {
		var selector = $(this).attr('data-filter');
		$container.isotope({
			filter: selector,
			animationOptions: {
				duration: 750,
				easing: 'linear',
				queue: false,
			}
		});
		return false;
	});
	// filter button behavior
	var $optionSets = $('.filter'), 
	$optionLinks = $optionSets.find('a');
	$optionLinks.click(function() {
		var $this = $(this);
		// don't proceed if already selected
		if ($this.hasClass('active')) {
			return false;
		}
		// add active class to selected filter button
		var $optionSet = $this.parents('.filter');
		$optionSet.find('.active').removeClass('active');
		$this.addClass('active');
	});
	$(".portfolio a").click(function(){
		var url = $(this).attr("data-url");
		window.open(url);
		event.preventDefault();
	});
};
	
