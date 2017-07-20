$(document).ready(function(){
    $('#delete_confirm_modal').modal('show');
    
    $("#class_id").change(function(){
        $("#get_props_form").submit();
    })

    var props_to_name = []

    $("body #prop_name").hover(function(){
        var prop = this.innerText;
        var found = 0;
        $(this).children('#selected_prop').click(function(){
            if (this.checked == true){
                for(i=0;i<props_to_name.length; i++){
                    if (prop == props_to_name[i]){
                        found ++
                    } 
                }
                if (found == 0){
                    props_to_name.push(prop);
                    $('#props_to_name').val(props_to_name);
                }
            }
            else{
                for(i=0;i<props_to_name.length; i++){
                    if (prop == props_to_name[i]){
                        props_to_name.splice(i,1);
                        $('#props_to_name').val(props_to_name);
                    } 
                }
            }
        });
    });
    $('#left_menu').mouseenter(function(){
            $('#left-well').css('box-shadow', '-7px -1px 33px 2px #444');
            $('#center-well').css('box-shadow', '0px 0px 0px 0px #444');


    });
    $('#left_menu').mouseleave(function(){
            $('#left-well').css('box-shadow', '0px 0px 0px 0px #444');
            $('#center-well').css('box-shadow','-7px -1px 33px 2px #444');
    });

    $('#right-menu').mouseenter(function(){
            $('#rigth-well').css('box-shadow', '-7px -1px 33px 2px #444');
            $('#center-well').css('box-shadow', '0px 0px 0px 0px #444');
    });
    $('#right-menu').mouseleave(function(){
            $('#rigth-well').css('box-shadow', '0px 0px 0px 0px #444');
            $('#center-well').css('box-shadow','-7px -1px 33px 2px #444');
    });


})
