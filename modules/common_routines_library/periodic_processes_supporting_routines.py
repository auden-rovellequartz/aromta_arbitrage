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
from .clear_market_data_supporting_routines import clear_market_data_x01
from .clear_market_data_supporting_routines import clear_market_data_x02
from .clear_market_data_supporting_routines import clear_market_data_x03
from .clear_market_data_supporting_routines import clear_market_data_x04

def asset_balances_monitor_process():
    return ()
def clear_market_data_process():
    clear_market_data_x01()
    clear_market_data_x02()
    clear_market_data_x03()
    clear_market_data_x04() 
    return ()
def trade_executions_monitor_process():
    return ()
def trade_operations_process():
    return ()
