$(function(){
	date_now = Date.now();
	$('#after').children().each(function(){
		var date_event = new Date(this.getAttribute('data'));
		if (date_event > date_now){
			$('#before').append(this);
		}
	});
	if ($('#before').children().length == 0 ) {
		$('#before').append('<p> Não tem futuros eventos cadastrados </p>')
	}
});
