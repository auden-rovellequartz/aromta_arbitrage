# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                 #
#   application:                       AROMTA Arbitrage                                           #
#   author:                            Auden RovelleQuartz                                        #
#                                                                                                 #
#   author's contact:                  auden.rovellequartz@gmail.com                              #
#   notices and information:           https://arbitrage.deborlen.com/software_notices_info       #
#                                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from ...modules.external_imports import *
from ...modules.framework_imports import *
from ...modules.constants.app_constants import *
from .time_supporting_routines import get_timestamp_formatted

def error_processing(arguments_array):
    if (arguments_array == "placeholder"):
        session["status_alert_type"] = "error"
        session["status_msg"] = (
            "a system error occurred; you are being logged out"
            )
        session["url_f"] = "conduit_logout"
        redirect(
            URL("status")
            )
    elif (arguments_array[FIRST_ELEMENT] == "LOG_AND_CONTINUE"):
        timestamp = get_timestamp_formatted()
        with open("_probe_error_processing", "a+") as file:
            file.write("\n\n")
            file.write("============ " + timestamp + " ============")
            file.write("\n\n")
            for item in arguments_array:
                file.write("\n\n")
                file.write(str(item))
            file.write("\n\n")
    elif (arguments_array[FIRST_ELEMENT] == "LOG_AND_EXIT"):
        timestamp = get_timestamp_formatted()
        message = "a system error occurred;"
        for x in range(len(arguments_array)):
            if (x != FIRST_ELEMENT):
                message = message + "<br>" + str(arguments_array[x])
        session["status_alert_type"] = "error"
        session["status_msg"] = message
        session["url_f"] = "conduit_logout"
        redirect(
            URL("status")
            )
    return ()
