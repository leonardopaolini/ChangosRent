$(document).ready(function () {
    $('#agreeTerms').change(function () {
        const btn = $('#signUpButton')
        if (btn.hasClass("disabled")) {
            btn.removeClass("disabled")
            btn.prop('disabled', false)
        } else {
            btn.addClass("disabled")
            btn.prop('disabled', true)
        }
    });
});