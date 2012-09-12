// ******************************************************************************************
// Contact Form Start
// ******************************************************************************************
		$(document).ready(function(){
		$("#form").validate({
			debug: false,
			rules: {
				name: "required",
				phone:"digits",
				message: "required",
				email: {
					required: true,
					email: true
				}
			},
			messages: {
				name: "Please let us know who you are.",
				email: "A valid email will help us get in touch with you."
				
			},
			submitHandler: function(form) {
				// do other stuff for a valid form
				$.post('email_process.php', $("#form").serialize(), function(data) {
					$('#post_message').html(data);
				});
			}
		});

//Contact Form END


/***************************************************
		  			Latest Tweets 
***************************************************/
$('.twitter').livetweet({
		'username' : 'jQuery',
		'limit' : 1,
		'html_before': '<ul>',
		'html_tweets': '<li>{text}<br>{date}</li><br />',
		'html_after': '</ul>'
		
	});

//Latest Tweets END

/***************************************************
		  		   // Portfolio on mouseover opactiy
***************************************************/	

				if( jQuery.hasOwnProperty("prettyPhoto") ){
			
				$(".lightbox").prettyPhoto({
					animation_speed	: 'normal',
					theme			: 'pp_default',
					social_tools	: ''
				});
			
			}

});

//prettyPhoto END


/***************************************************
		  			Isotope Portfolio
***************************************************/
jQuery(document).ready(function(){ 

// Needed variables
	var $container	 	= $('#portfolio-list');
	var $filter 		= $('#portfolio-filter');
		
// Run Isotope  
	$container.isotope({
		filter				: '*',
		layoutMode   		: 'masonry',
		animationOptions	: {
		duration			: 750,
		easing				: 'linear'
	   }
	});	
	
// Isotope Filter 
	$filter.find('a').click(function(){
	  var selector = $(this).attr('data-filter');
		$container.isotope({ 
		filter				: selector,
		animationOptions	: {
		duration			: 750,
		easing				: 'linear',
		queue				: false,
	   }
	  });
	  return false;
	});	

// Adding Class to current selected items
$filter.find('a').click(function() {
		var currentOption = $(this).attr('data-filter');
		$filter.find('a').removeClass('current');
		$(this).addClass('current');
	});	




// Portfolio on mouse over image animation 
	var $container	 	= $('#portfolio-list');
	$container.find('img').adipoli({
		'hoverEffect' 	: 'boxRainGrowReverse',
		'startEffect' : 'transparent',
		'animSpeed' 	: 200,
	});


// Services on mouse over image animation 
	var $container3	 	= $('#service-box');
	$container3.find('img').adipoli({
		'hoverEffect' 	: 'boxRainGrowReverse',
		'startEffect' : 'transparent',
		'animSpeed' 	: 200,
	});
	
// Home page mouse over image animation 
	var $container1	 	= $('#home');
	$container1.find('img').adipoli({
  'startEffect' : 'transparent',
    'hoverEffect' : 'boxRainGrowReverse'
});

});	


// Isotope Portfolio END

/***************************************************
		  			Card Slides start
***************************************************/

            $(function() {
          
				// on  click logo	ul.list li
				$('ul.arrowunderline li,.menu > .item > .item_content >h2,.logo').hover(
				)
	
	
	// on  click navigation	
				.click(function(){
					var $this = $(this);
					var name = this.className;
					$('#content').animate({marginTop:-900}, 500,function(){ // upside slide animation 
					var $this = $(this);
		
		switch (name)
			{
			case 'home':
			$('#home').show();
			$('#about,#resume,#services,#portfolio,#contact').hide();
			
			break;
			
			case 'logo':
			$('#home').show();
			$('#about,#resume,#services,#portfolio,#contact').hide();
			break;
			
			case 'about':
			$('#about').show();
			$('#resume,#home,#services,#portfolio,#contact').hide();
			break;
			
			case 'resume':	 
			$('#resume').show();
			$('#about,#home,#services,#portfolio,#contact').hide();
			break;
			
			case 'services':	 
			$('#services').show();
			$('#about,#home,#resume,#portfolio,#contact').hide();
			break;
			
			case 'portfolio':
			$('#portfolio').show();
			$('#about,#home,#services,#resume,#contact').hide();
			break;

			
			case 'contact':
			$('#contact').show();
			$('#about,#home,#services,#resume,#portfolio').hide();
			break;
			
		} // end switch 
					
				$this.animate({marginTop:108}, 500);  // Downside slide animation 
				$this.animate({marginTop:96}, 500); //  slight animation 
				$this.animate({marginTop:108}, 500); // reset to normal
		
					})	 

				});

            });

  // Card Slides END
  
  
  jQuery(document).ready(function(){ 
 $("ul.arrowunderline li").click(function () {
			$('ul.arrowunderline  li').removeAttr('id');
		//	$('ul.arrowunderline  li').css('color', '#b6b6b6')
			$(this).attr('id', 'selected'  );
		//	$(this).css('color', '#71be6f');
    });
     });
 
 jQuery(document).ready(function($){

	/* prepend menu icon */
	$('#nav-wrap').prepend('<div id="menu-icon">Menu</div>');
	
	/* toggle nav */
	$("#menu-icon").on("click", function(){
		$("#nav").slideToggle();
		$(this).toggleClass("active");
	});

});

/***************************************************
		  			Nivo Slider start
***************************************************/

 $(window).load(function() {

   jQuery("#Slider").nivoSlider({
	effect:"boxRandom", //Specify sets like: 'fold,fade,sliceDown'
        slices:15,
        boxCols:8,
        boxRows:4,
        animSpeed:500, //Slide transition speed
        pauseTime:3000,
        startSlide:0,//Set starting Slide (0 index)

        directionNav:false,//Next & Prev
        directionNavHide:false, //Only show on hover
		controlNav:false,	//1,2,3...
        controlNavThumbs:false,//Use thumbnails for Control Nav
        controlNavThumbsFromRel:false,//Use image rel for thumbs

		keyboardNav:false,//Use left & right arrows

        pauseOnHover:false,//Stop animation while hovering
        manualAdvance:false//Force manual transitions

   });
});
 
  // Nivo Slider END
  



/***************************************************
		  		//	Preloader Script
***************************************************/

$(window).load(function() {
  $('#preloader').fadeOut(300, function() {
    $('body').css('overflow','visible');
    $(this).remove();
  });
});

//	//	Preloader Script
