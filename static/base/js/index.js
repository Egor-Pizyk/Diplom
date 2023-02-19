jQuery(document).ready(function($){

$('.header-dropdown-item').hide();
$('.header-dropdown--btn').click(function() {
    $('.header-dropdown-item').slideToggle();
});

})