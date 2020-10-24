console.log("All good!")

$(document).ready(function() {
    $('.html').css({'opacity' : '1'});

    // Função para transição entre páginas
    $("a").click(function(e) {
        e.preventDefault();
        var link = $(this).attr("href");
        fadeOutHTML(link);
    });

    var fadeOutHTML = function(link) {
        $('.html').css({'opacity' : '0'});
        setTimeout(function() {
            window.location = link;
        }, 800);
    }

    $('input').attr('autocomplete', 'off');
 });