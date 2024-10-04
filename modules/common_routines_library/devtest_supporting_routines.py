# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#																									#
#	application:							AROMTA Arbitrage										#
#	author:									Auden RovelleQuartz										#
#											                                                		#
#																									#
#	author's contact:						auden.rovellequartz@gmail.com							#
#	notices and information:				https://arbitrage.deborlen.com/software_notices_info	#
#																									#
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from ...modules.external_imports import *
from ...modules.framework_imports import *
from ...modules.constants.app_constants import *

def form_submit_button(button_label, form_action):
	form = FORM(
		SECTION(
			DIV(
				DIV(
					DIV(
						INPUT(
							_type = "submit",
							_value = button_label,
							_class = "ovx-btn expand",
							),
						_class = "Textcenter",
						),
					_class = "pure-u-1"
					),
				_class = "pure-g",
				),
			_class = "pure-u-1",
			),
		_method = "POST",
		_enctype = "multipart/form-data",
		_action = URL(form_action),
		_class = "ovx-form",
		)
	return (form)
def form_dropdown_input_submit_button(
	selector_label,
	options,
	button_label,
	form_action
	):
	form = FORM(
		SECTION(
			DIV(
				DIV(
					FIELDSET(
						LABEL(selector_label),
						DIV(
							SELECT(
								*[OPTION(x, _value = x) for x in options],
								_name = "input",
								_class = "ovx-select-group",
								),
							_class = "ovx-select-group-wrap"
							),
						_class = "mandatory",
						),
					_class = "pure-u-1",
					),
				_class = "pure-g",
				),
			DIV(
				DIV(
					DIV(
						INPUT(
							_type = "submit",
							_value = button_label,
							_class = "ovx-btn expand",
							),
						_class = "Textcenter",
						),
					_class = "pure-u-1"
					),
				_class = "pure-g",
				),
			_class = "pure-u-1",
			),
		_method = "POST",
		_enctype = "multipart/form-data",
		_action = URL(form_action),
		_class = "ovx-form",
		)
	return (form)
def form_text_input_submit_button(text_label, button_label, form_action):
	form = FORM(
		SECTION(
			DIV(
				DIV(
					FIELDSET(
						LABEL(text_label),
						INPUT(
							_type = "text",
							_name = "input",
							_class = "ovx-input-1",
							),
						_class = "mandatory",
						),
					_class = "pure-u-1",
					),
				_class = "pure-g",
				),
			DIV(
				DIV(
					DIV(
						INPUT(
							_type = "submit",
							_value = button_label,
							_class = "ovx-btn expand",
							),
						_class = "Textcenter",
						),
					_class = "pure-u-1"
					),
				_class = "pure-g",
				),
			_class = "pure-u-1",
			),
		_method = "POST",
		_enctype = "multipart/form-data",
		_action = URL(form_action),
		_class = "ovx-form",
		)
	return (form)

