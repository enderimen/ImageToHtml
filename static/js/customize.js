$('#upload').click(function () {

	$("#file").trigger('click');

	$("#file").on('change', function () {
		var file =  $("#file").val();

		alert(file);
	});

	
	 
});