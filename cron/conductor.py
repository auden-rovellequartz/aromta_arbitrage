# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                 #
#   application:                       AROMTA Arbitrage                                           #
#   author:                            Auden RovelleQuartz                                        #
#                                                                                                 #
#   author's contact:                  auden.rovellequartz@gmail.com                              #
#   notices and information:           https://arbitrage.deborlen.com/software_notices_info       #
#                                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from ..modules.external_imports import *
from ..modules.framework_imports import *
from ..modules.application_imports import *
		
@action("start_conductor")
@action.uses(db)
def start_conductor():
	previous_error = "UNDEFINED"
	try:
		while (True):
			try:
				clear_market_data_process()
			except Exception as error:
				if (str(error) != previous_error):
					argument_list = [
						"LOG_AND_CONTINUE",
						(inspect.currentframe().f_code.co_name, "reference point #0"),
						error,
						]
					previous_error = str(error)
					error_processing(argument_list)
			try:
				current_yyyymmddhhmmss_update()
			except Exception as error:
				if (str(error) != previous_error):
					argument_list = [
						"LOG_AND_CONTINUE",
						(inspect.currentframe().f_code.co_name, "reference point #1"),
						error,
						]
					previous_error = str(error)
					error_processing(argument_list)
			time.sleep(ONE_SECOND)
	except Exception as error:
		with open("start_conductor_error", "a+") as file:
			file.write("\n\n=============================\n\n")
			file.write(str(error))
	return ()
