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
	counter_asset_balances_monitor = ZERO
	counter_clear_market_data = ZERO
	counter_trade_executions_monitor = ZERO
	counter_trade_operations = ZERO
	previous_error = "UNDEFINED"
	reference_point = ZERO
	try:
		while (True):
			try:
				current_yyyymmddhhmmss_update()
			except Exception as error:
				if (str(error) != previous_error):
					argument_list = [
						"LOG_AND_CONTINUE",
						(
							inspect.currentframe().f_code.co_name, 
							f"reference point #{reference_point}"
							),
						error,
						]
					previous_error = str(error)
					error_processing(argument_list)
			if (
				(counter_trade_operations % TRADE_OPERATIONS_PERIOD) 
				== 
				EXECUTION_INDICATOR_TRUE
				):
				try:
					trade_operations_process()
					reference_point = reference_point + INCREMENT_TO_NEXT_VALUE
				except Exception as error:
					if (str(error) != previous_error):
						argument_list = [
							"LOG_AND_CONTINUE",
							(
								inspect.currentframe().f_code.co_name, 
								f"reference point #{reference_point}"
								),
							error,
							]
						previous_error = str(error)
						error_processing(argument_list)
			if (
				(counter_trade_executions_monitor % TRADE_EXECUTIONS_MONITOR_PERIOD)
				== 
				EXECUTION_INDICATOR_TRUE
				):
				try:
					trade_executions_monitor_process()
					reference_point = reference_point + INCREMENT_TO_NEXT_VALUE
				except Exception as error:
					if (str(error) != previous_error):
						argument_list = [
							"LOG_AND_CONTINUE",
							(
								inspect.currentframe().f_code.co_name, 
								f"reference point #{reference_point}"
								),
							error,
							]
						previous_error = str(error)
						error_processing(argument_list)
			if (
				(counter_asset_balances_monitor % ASSET_BALANCES_MONITOR_PERIOD) 
				== 
				EXECUTION_INDICATOR_TRUE
				):
				try:
					asset_balances_monitor_process()
					reference_point = reference_point + INCREMENT_TO_NEXT_VALUE
				except Exception as error:
					if (str(error) != previous_error):
						argument_list = [
							"LOG_AND_CONTINUE",
							(
								inspect.currentframe().f_code.co_name, 
								f"reference point #{reference_point}"
								),
							error,
							]
						previous_error = str(error)
						error_processing(argument_list)
			if (
				(counter_clear_market_data % CLEAR_MARKET_DATA_PERIOD) 
				== 
				EXECUTION_INDICATOR_TRUE
				):
				try:
					clear_market_data_process()
					reference_point = reference_point + INCREMENT_TO_NEXT_VALUE
				except Exception as error:
					if (str(error) != previous_error):
						argument_list = [
							"LOG_AND_CONTINUE",
							(
								inspect.currentframe().f_code.co_name, 
								f"reference point #{reference_point}"
								),
							error,
							]
						previous_error = str(error)
						error_processing(argument_list)
			counter_asset_balances_monitor = (
				counter_asset_balances_monitor + INCREMENT_TO_NEXT_VALUE
				)
			counter_clear_market_data = (
				counter_clear_market_data + INCREMENT_TO_NEXT_VALUE
				)
			counter_trade_executions_monitor = (
				counter_trade_executions_monitor + INCREMENT_TO_NEXT_VALUE
				)
			counter_trade_operations = (
				counter_trade_operations + INCREMENT_TO_NEXT_VALUE
				)
			time.sleep(ONE_SECOND)
	except Exception as error:
		with open("start_conductor_error", "a+") as file:
			file.write("\n\n=============================\n\n")
			file.write(str(error))
	return ()
