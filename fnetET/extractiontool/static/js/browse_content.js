$(document).ready(function(){
    $("body #subtree").click(function(){
        alert('ok');
        $(this).append('<ul><li>YAY</li></ul>');
    });

});

