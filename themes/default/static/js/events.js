jQuery(function(){
	date_now = Date.now();
	jQuery('#after').children().each(function(){
		var date_event = new Date(this.getAttribute('data') + " 00:00");
		if (date_event > date_now){
			jQuery('#before').append("<li>" + $(this).html() + "</li>");
			this.remove();
		}
	});
	if (jQuery('#before').children() == [] ) {
		jQuery('#before').append('<p> Não tem futuros eventos cadastrados </p>')
	}

});
