//menubar background color when scroll
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 600) {
        $(".menu-wrapper.top").addClass("bg");
        $(".logo").addClass("small");
        $(".menu-button").addClass("color");
        $(".menu-bar").addClass("color");
        $(".hamburger-inner").addClass("accent");
    } else {
        $(".menu-wrapper.top").removeClass("bg");
        $(".logo").removeClass("small");
        $(".menu-button").removeClass("color");
        $(".menu-bar").removeClass("color");
        $(".hamburger-inner").removeClass("accent");
    }
});

//Slider Animate Multiple Background Images
setInterval(() => {
	var current = $(".js-fv-bg:visible");
	var next = $(".js-fv-bg").eq($(".js-fv-bg").index($(current)) + 1);
	if( !next.length )
		next = $(".js-fv-bg").first();

	current.fadeOut();
	next.fadeIn();

}, 3000);

//impressum popup
$(window).on('load', function() {
	//Hamburge
   	$(".hamburger").on("click", function(e) {
        $(".hamburger").toggleClass("is-active");
        $(".mobilemenu-wrapper").toggleClass("is-active");
    });

	// Popup
    $(".trigger_popup_fricc").click(function(){
       $('.hover_bkgr_fricc').show();
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });

    // Scroll to entry
	$("a.js-scroll").click((event) => {
		var a = $(event.target);
		document.getElementById(a.attr("href").substr(1)).scrollIntoView({behavior: 'smooth'});
		a.blur();
		return false;
	});
});

