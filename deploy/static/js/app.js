//impressum popup
$(window).on('load', function() {
    $(".trigger_popup_fricc").click(function(){
       $('.hover_bkgr_fricc').show();
    });
    $('.hover_bkgr_fricc').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
    $('.popupCloseButton').click(function(){
        $('.hover_bkgr_fricc').hide();
    });
});

//menubar background color when scroll
$(window).scroll(function() {
    var height = $(window).scrollTop();
    if (height > 600) {
        $(".menu-wrapper.top").addClass("bg");
        $(".logo").addClass("small");
        $(".menu-button").addClass("color");
        $(".menu-bar").addClass("color"); 
    } else {
        $(".menu-wrapper.top").removeClass("bg");
        $(".logo").removeClass("small");
        $(".menu-button").removeClass("color");
        $(".menu-bar").removeClass("color");
    }
});

//Slider Animate Multiple Background Images
if (typeof bgImageArray !== 'undefined'){

    secs = 5;
    bgImageArray.forEach(function(img){
        new Image().src = img; // caches images, avoiding white flash between background replacements
    });
    
    function backgroundSequence() {
        window.clearTimeout();
        var k = 0;
        for (i = 0; i < bgImageArray.length; i++) {
            setTimeout(function(){ 
            document.getElementById('fv').style.background = "url(" + bgImageArray[k] + ") no-repeat center center";
            document.getElementById('fv').style.backgroundSize ="cover";
            if ((k + 1) === bgImageArray.length) { 
                setTimeout(function() { backgroundSequence() }, (secs * 3000))} else { k++; }            
            }, (secs * 1000) * i)   
        }
    }
    
    backgroundSequence();
    }
