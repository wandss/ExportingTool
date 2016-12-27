$(document).ready(function(){

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
			$("#servers").removeAttr('disabled');			
		}
		else{
			$("#servers").attr('disabled', 'true');			
		}
	});
	username = document.getElementById('username').value;
	passwd = document.getElementById('passwd').value;
		
	if (username !== '' & passwd !== '' ){			
		$("#servers").removeAttr('disabled');			
	}
	else{
		$("#servers").attr('disabled', 'true');			
	}

})
/*$(document).ready(function(){
	$('#available_classes').change(function(){
		var chosen_class = document.getElementById('available_classes').value;		
		$.get('/teste/',{chosen: chosen_class}, function(data){
			var properties = data;
			var splited = data.split('');

			for (i=0;i<splited.length;i++){
				$("#class_properties").append("<option id='property' value="+splited[i]+">"+splited[i]+"</option>")
			}
		});
	});


	var properties = []
	$("#class_properties").change(function(){
		var props = document.getElementById("class_properties").value;	
		var teste = document.getElementById("class_properties");	
		alert(teste.selected);
		var found = false;
		
		for (i=0; i < properties.length; i++){
			if (props == properties[i]){
				found = true;				
			}
		} 
		if (found === false) {
			properties.push(props)
		}
		$("#chosen_props").val(properties);
		
	});

})

*/