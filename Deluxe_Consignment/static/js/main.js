$(document).ready(() => {
    new WOW().init();
    $('#modalCookie1').modal('show')
});


$('input[type=radio]').on('change', function() {
    $(this).closest("form").submit();
});