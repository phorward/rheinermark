//Slider Animate Multiple Background Images
setInterval(() => {
	var visible = $(".js-diashow:visible");

	visible.each(
		(idx) => {
			var current = $(visible[idx]);
			var group = current.data("group");

			if( !group )
			{
				console.error("js-diashow element has no group set!");
				return;
			}

			var images = $(".js-diashow[data-group=" + group + "]");
			if( images.length < 2 )
				return;

			var next = images.eq(images.index($(current)) + 1);

			if( !next.length )
				next = images.first();

			current.fadeOut("slow");
			next.fadeIn("slow");
		});

}, 10000);


$(window).ready(function() {
	//menubar background color when scroll
	if( $("#fv").length )
	{
		function checkScrollState() {
			var height = $(window).scrollTop();
			if (height > 600) {
				$(".menu-wrapper").addClass("steady");
			} else {
				$(".menu-wrapper").removeClass("steady");
			}
		}

		$(window).scroll(checkScrollState);
		checkScrollState();
	}

	//Hamburger
   	$(".hamburger").on("click", function(e) {
        $(".hamburger").toggleClass("is-active");
        $(".mobilemenu-wrapper").toggleClass("is-active");
    });

    // Scroll to entry
	$("a.js-scroll").click((event) => {
		var a = $(event.target);
		document.getElementById(a.attr("href").substr(1)).scrollIntoView({behavior: 'smooth'});
		a.blur();
		return false;
	});

	$(".mobilemenu .js-scroll").click(() => {
        $(".hamburger").toggleClass("is-active");
        $(".mobilemenu-wrapper").toggleClass("is-active");
	});

    // View a popup
	$("a.js-popup").click((event) => {
		var a = $(event.target);
		var popup = a.attr("href");

		a.blur();
		$(popup).show();

		return false;
	});

	// Forms
	$("form.js-form").submit((event) => {
		var form = $(event.target);
		form.find(".js-form-form").fadeOut();
		form.find(".js-form-loading").fadeIn();

		var formData = new FormData(event.target);

		$.ajax({
			url: "/json/skey",
			dataType: "json"}).done(
				function( skey )
				{
					formData.set("skey", skey);

					$.ajax({
						url: "/json/contact/add",
						type: "POST",
						data: formData,
						cache: false,
						dataType: "json",
						processData: false,
						contentType: false,
						success: function (data, textStatus, jqXHR) {
							form.find(".js-form-loading").fadeOut();

							if (typeof data.error === 'undefined')
							{
								if( data.action == "addSuccess" )
								{
									form.find(".js-form-success").fadeIn();
								}
								else
								{
									alert("Es trat ein Fehler auf.");
								}
							}
							else
								console.log('ERRORS: ' + data.error);
						}
					});
				});

		return false;
	});

  	// Cookie consent
	if (document.cookie.indexOf("cookie-consent=confirmed") < 0 ) {
		$("#cookieConsent").fadeIn(200);

		$("#cookieConsentOK").click(function() {
			var expires = new Date();
			expires.setFullYear(expires.getFullYear() + 1);

			document.cookie = "cookie-consent=confirmed; expires=" + expires.toUTCString() + "; path=/";

			$("#cookieConsent").fadeOut(200);
		});
	}

	// Focus a js-focus
	$(".js-focus").focus();
});

