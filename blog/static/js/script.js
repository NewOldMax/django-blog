$(document).ready(function() {
    $('.add-post').click(function(){
        $(this).toggleClass('active');
        $('.add-post-form, #dark-back').toggleClass('active');
    });
    // $('#background1').mouseParallax({ moveFactor: 5 });
    // $('#background2').mouseParallax({ moveFactor: 7 });
    // $('#background3').mouseParallax({ moveFactor: 3 });
    // $('#background4').mouseParallax({ moveFactor: 10 });
});