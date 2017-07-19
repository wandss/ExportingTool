$(document).ready(function(){
        $('#delete_confirm_modal').modal('show');
        
        $('#class_id').change(function(){
            var request = new XMLHttpRequest();
            request.open("GET", "http://google.com", true);
            
            alert($('#class_id').val());
        });

	$('#available_servers').change(function(){
		var server = document.getElementById('available_servers').value;
		$("#myform").submit();
	});

	$("#available_classes").change(function(){
		var chosen_class = document.getElementById('available_classes').value;
		$("#myform").submit();
	});
	$("#class_properties").click(function(){
		var property = $(this).val();
		$("#chosen_props").val(property);
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
	$("#username, #passwd").change(function(){
		username = document.getElementById('username').value;
		passwd = document.getElementById('passwd').value;

		if (username !== '' & passwd !== '' ){
			$("#available_servers").removeAttr('disabled');
		}
		else{
			$("#available_servers").attr('disabled', 'true');
		}
	});
	$("#server, #delete_server").mouseenter(function(){
		$(this).css('background-color', '#ee403c');
		$(this).css('text-shadow', '-6px 8px 2px black');

	});
	$("#server, #delete_server").mouseleave(function(){
		$(this).css('background-color', '');
		$(this).css('text-shadow', '');
	});

	$(".list-group-item, btn ").click(function(){
		var server_address = $(this).attr('address');
		var server_name =  $(this).attr('serverName');
		var server_pk = $(this).attr('serverPk');
		$("#server_name").val(server_name);
		$("#server_address").val(server_address);
		$('#edit').val(server_pk);
	});
	$("#save_set").click(function(){
		var server_name = $("#server_name").val();
		if (server_name.length > 18){
			$(".my_h6").prepend('<div class="warning_message" style="color: red"><em>This field is limited to 18 Characters!!!</em></div>');
			return false;
		}
		else {
			$("#myform").submit();
		}

	});
	username = document.getElementById('username').value;
	passwd = document.getElementById('passwd').value;
	if (username !== '' & passwd !== '' ){
		$("#available_servers").removeAttr('disabled');
	}
	else{
		$("#available_servers").attr('disabled', 'true');
	}
    

})
