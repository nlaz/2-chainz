$(document).ready(function() {
   initClicks(); 
});

function initClicks() {

    $("#about").click(function() {
        $('html, body').animate({
            scrollTop: $(".about").offset().top - 100
        }, 500);
    });

    $("#faq").click(function() {
        $('html, body').animate({
            scrollTop: $(".faq-section").offset().top - 50
        }, 500);
    });

    $("#sponsors").click(function() {
        $('html, body').animate({
            scrollTop: $(".main-sponsor").offset().top - 100
        }, 500);
    });

    $("#contact").click(function() {
        $('html, body').animate({
            scrollTop: $(".contact").offset().top - 100
        }, 500);
    });
}
