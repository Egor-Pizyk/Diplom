$('.auth_form input').blur(function(){
    if( $(this).val().length != 0 ) {
        $(this).addClass('non_empty_field');
    }
    else{
        $(this).removeClass('non_empty_field');
    }
});