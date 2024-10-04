# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # 
#                                                                                                 #
#   application:                       AROMTA Arbitrage                                           #
#   author:                            Auden RovelleQuartz                                        #
#                                                                                                 #
#   author's contact:                  auden.rovellequartz@gmail.com                              #
#   notices and information:           https://arbitrage.deborlen.com/software_notices_info       #
#                                                                                                 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

from .common_routines_library.clear_market_data_supporting_routines import \
    clear_all_market_data
from .common_routines_library.clear_market_data_supporting_routines import \
    clear_market_data_process
from .common_routines_library.clear_market_data_supporting_routines import \
    clear_market_data_x01_process
from .common_routines_library.clear_market_data_supporting_routines import \
    clear_market_data_x02_process
from .common_routines_library.clear_market_data_supporting_routines import \
    clear_market_data_x03_process
from .common_routines_library.clear_market_data_supporting_routines import \
    clear_market_data_x04_process
from .common_routines_library.error_processing_supporting_routines import \
    error_processing
from .common_routines_library.time_supporting_routines import \
    current_yyyymmddhhmmss_update
from .common_routines_library.time_supporting_routines import \
    determine_if_same_day
from .common_routines_library.time_supporting_routines import \
    get_countdown_to_next_time
from .common_routines_library.time_supporting_routines import \
    get_current_yyyymmddhhmmss_record
from .common_routines_library.time_supporting_routines import \
    get_dto_date_now_no_secs
from .common_routines_library.time_supporting_routines import \
    get_dto_date_now
from .common_routines_library.time_supporting_routines import \
    get_dto_from_yyyymmddhhmm
from .common_routines_library.time_supporting_routines import \
    get_dto_from_yyyymmddhhmmss
from .common_routines_library.time_supporting_routines import \
    get_duration_in_minutes
from .common_routines_library.time_supporting_routines import \
    get_duration_in_seconds
from .common_routines_library.time_supporting_routines import \
    get_minutes_elapsed
from .common_routines_library.time_supporting_routines import \
    get_month_and_weekday
from .common_routines_library.time_supporting_routines import \
    get_next_weekday
from .common_routines_library.time_supporting_routines import \
    get_remaining_seconds_to_time
from .common_routines_library.time_supporting_routines import \
    get_time_am_pm
from .common_routines_library.time_supporting_routines import \
    get_timestamp
from .common_routines_library.time_supporting_routines import \
    get_timestamp_formatted
from .common_routines_library.time_supporting_routines import \
    get_timestamp_no_secs
from .common_routines_library.time_supporting_routines import \
    get_yyyymmdd
from .common_routines_library.time_supporting_routines import \
    get_yyyymmddhhmmss_string
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_buy_order_exchange_01
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_buy_order_exchange_02
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_buy_order_exchange_03
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_buy_order_exchange_04
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_sell_order_exchange_01
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_sell_order_exchange_02
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_sell_order_exchange_03
from .common_routines_library.trade_execution_supporting_routines import \
    cancel_sell_order_exchange_04
from .common_routines_library.trade_execution_supporting_routines import \
    place_buy_order_exchange_01
from .common_routines_library.trade_execution_supporting_routines import \
    place_buy_order_exchange_02
from .common_routines_library.trade_execution_supporting_routines import \
    place_buy_order_exchange_03
from .common_routines_library.trade_execution_supporting_routines import \
    place_buy_order_exchange_04
from .common_routines_library.trade_execution_supporting_routines import \
    place_sell_order_exchange_01
from .common_routines_library.trade_execution_supporting_routines import \
    place_sell_order_exchange_02
from .common_routines_library.trade_execution_supporting_routines import \
    place_sell_order_exchange_03
from .common_routines_library.trade_execution_supporting_routines import \
    place_sell_order_exchange_04
from .common_routines_library.connections_exchange_01_supporting_routines import \
    connections_manager_wsx01_btcusd
from .common_routines_library.connections_exchange_01_supporting_routines import \
    wsx01_get_token
from .common_routines_library.connections_exchange_02_supporting_routines import \
    connections_manager_wsx02_btcusdt
from .common_routines_library.connections_exchange_03_supporting_routines import \
    connections_manager_httpx03_btcusdt
from .common_routines_library.connections_exchange_04_supporting_routines import \
    connections_manager_wsx04_btcusd

################################## DevTest Functions ###############################################

from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_private_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_private_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_private_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_private_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_public_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_public_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_public_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_01_public_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_btcusdt_depth_stream_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_btcusdt_depth_stream_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_btcusdt_depth_stream_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_btcusdt_depth_stream_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_private_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_private_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_private_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_private_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_public_on_close 
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_public_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_public_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_02_public_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_private_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_private_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_private_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_private_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_public_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_public_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_public_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_03_public_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_private_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_private_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_private_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_private_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_public_on_close
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_public_on_error
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_public_on_message
from .common_routines_library.websockets_supporting_routines import \
    websockets_exchange_04_public_on_open
from .common_routines_library.websockets_supporting_routines import \
    websockets_get_signature_exchange_02
from .common_routines_library.devtest_supporting_routines import \
    form_submit_button
from .common_routines_library.devtest_supporting_routines import \
    form_dropdown_input_submit_button
from .common_routines_library.devtest_supporting_routines import \
    form_text_input_submit_button
