var range_value_elements = ["No experience", "6 month", "1 year", "1.5 - 2 years", "3 - 4 years", "4 - 5 years", "6 - 7 years", "8 - 9 years", "10 years", "10+ year"];

$('#experience_id').on('input', function() {
    $(this).next('.range_value').html(range_value_elements[this.value])
});

