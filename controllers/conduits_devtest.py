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

####################################################################################################
@action("CONDUITS_DEVTEST_TEMPLATE", method = ["GET", "POST"])
@action.uses(db, session)
def CONDUITS_DEVTEST_TEMPLATE():
	redirect(
		URL("")
		)
	return ()
####################################################################################################
@action("conduit_clear_all_market_data", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_clear_all_market_data():
	clear_all_market_data()
	redirect(
		URL("devtest_home")
		)
	return ()
@action("conduit_devtest_btcusdt_depth_stream_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_btcusdt_depth_stream_exchange_02():
	ws = websocket.WebSocketApp(
			"wss://stream.binance.us:9443/ws/btcusdt@depth",
			on_message = websockets_exchange_02_btcusdt_depth_stream_on_message,
			on_error = websockets_exchange_02_btcusdt_depth_stream_on_error,
			on_close = websockets_exchange_02_btcusdt_depth_stream_on_close
			)
	ws.on_open = websockets_exchange_02_btcusdt_depth_stream_on_open
	t = Thread(target = ws.run_forever)
	t.start()
	session["result_devtest_btcusdt_depth_stream_exchange_02"] = "The operation has been executed."
	redirect(
		URL("devtest_btcusdt_depth_stream_exchange_02_b")
		)
	return ()
@action("conduit_devtest_buy_order_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_buy_order_exchange_01():
	redirect(
		URL("devtest_buy_order_exchange_01")
		)
	return ()
@action("conduit_devtest_buy_order_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_buy_order_exchange_02():
	redirect(
		URL("devtest_buy_order_exchange_02")
		)
	return ()
@action("conduit_devtest_buy_order_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_buy_order_exchange_03():
	redirect(
		URL("devtest_buy_order_exchange_03")
		)
	return ()
@action("conduit_devtest_buy_order_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_buy_order_exchange_04():
	redirect(
		URL("devtest_buy_order_exchange_04")
		)
	return ()
@action("conduit_devtest_cancel_all_orders_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_all_orders_exchange_01():
	redirect(
		URL("devtest_cancel_all_orders_exchange_01")
		)
	return ()
@action("conduit_devtest_cancel_all_orders_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_all_orders_exchange_02():
	redirect(
		URL("devtest_cancel_all_orders_exchange_02")
		)
	return ()
@action("conduit_devtest_cancel_all_orders_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_all_orders_exchange_03():
	redirect(
		URL("devtest_cancel_all_orders_exchange_03")
		)
	return ()
@action("conduit_devtest_cancel_all_orders_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_all_orders_exchange_04():
	redirect(
		URL("devtest_cancel_all_orders_exchange_04")
		)
	return ()
@action("conduit_devtest_cancel_order_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_order_exchange_01():
	redirect(
		URL("devtest_cancel_order_exchange_01")
		)
	return ()
@action("conduit_devtest_cancel_order_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_order_exchange_02():
	redirect(
		URL("devtest_cancel_order_exchange_02")
		)
	return ()
@action("conduit_devtest_cancel_order_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_order_exchange_03():
	redirect(
		URL("devtest_cancel_order_exchange_03")
		)
	return ()
@action("conduit_devtest_cancel_order_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_cancel_order_exchange_04():
	redirect(
		URL("devtest_cancel_order_exchange_04")
		)
	return ()
@action("conduit_devtest_sell_order_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_sell_order_exchange_01():
	redirect(
		URL("devtest_sell_order_exchange_01")
		)
	return ()
@action("conduit_devtest_sell_order_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_sell_order_exchange_02():
	redirect(
		URL("devtest_sell_order_exchange_02")
		)
	return ()
@action("conduit_devtest_sell_order_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_sell_order_exchange_03():
	redirect(
		URL("devtest_sell_order_exchange_03")
		)
	return ()
@action("conduit_devtest_sell_order_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_sell_order_exchange_04():
	redirect(
		URL("devtest_sell_order_exchange_04")
		)
	return ()
@action("conduit_devtest_websocket_private_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_private_exchange_01():
	ws = websocket.WebSocketApp(
			"wss://ws.bitstamp.net",
			on_message = websockets_exchange_01_private_on_message,
			on_error = websockets_exchange_01_private_on_error,
			on_close = websockets_exchange_01_private_on_close
			)
	ws.on_open = websockets_exchange_01_private_on_open
	t = Thread(target = ws.run_forever)
	t.start()
	session["result_devtest_websocket_private_exchange_01"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_private_exchange_01_b")
		)
	return ()
@action("conduit_devtest_websocket_private_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_private_exchange_02():
	ws = websocket.WebSocketApp(
			"wss://ws-api.binance.us:443/ws-api/v3",
			on_message = websockets_exchange_02_private_on_message,
			on_error = websockets_exchange_02_private_on_error,
			on_close = websockets_exchange_02_private_on_close
			)
	ws.on_open = websockets_exchange_02_private_on_open
	t = Thread(target = ws.run_forever)
	t.start()
	session["result_devtest_websocket_private_exchange_02"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_private_exchange_02_b")
		)
	return dict()
@action("conduit_devtest_websocket_private_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_private_exchange_03():
	session["result_devtest_websocket_private_exchange_03"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_private_exchange_03_b")
		)
	return dict()
@action("conduit_devtest_websocket_private_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_private_exchange_04():
	session["result_devtest_websocket_private_exchange_04"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_private_exchange_04_b")
		)
	return dict()
@action("conduit_devtest_websocket_public_exchange_01", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_public_exchange_01():
	connections_manager_wsx01_btcusd()
	# ws = websocket.WebSocketApp(
	# 		"wss://ws.bitstamp.net",
	# 		on_message = websockets_exchange_01_public_on_message,
	# 		on_error = websockets_exchange_01_public_on_error,
	# 		on_close = websockets_exchange_01_public_on_close
	# 		)
	# ws.on_open = websockets_exchange_01_public_on_open
	# t = Thread(target = ws.run_forever)
	# t.start()
	session["result_devtest_websocket_public_exchange_01"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_public_exchange_01_b")
		)
	return dict()
@action("conduit_devtest_websocket_public_exchange_02", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_public_exchange_02():
	connections_manager_wsx02_btcusdt()
	session["result_devtest_websocket_public_exchange_02"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_public_exchange_02_b")
		)
	return dict()
@action("conduit_devtest_websocket_public_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_public_exchange_03():
	connections_manager_httpx03_btcusdt()
	session["result_devtest_websocket_public_exchange_03"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_public_exchange_03_b")
		)
	return dict()
@action("conduit_devtest_websocket_public_exchange_04", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_devtest_websocket_public_exchange_04():
	connections_manager_wsx04_btcusd()
	session["result_devtest_websocket_public_exchange_04"] = "The operation has been executed."
	redirect(
		URL("devtest_websocket_public_exchange_04_b")
		)
	return dict()
@action("conduit_test_sell_order_exchange_03", method = ["GET", "POST"])
@action.uses(db, session)
def conduit_test_sell_order_exchange_03():
	order_response = place_sell_order_exchange_03("BTC", "0.00015", "100000", "USDT")

	with open("_probe_20241003_001", "a+") as file:
		file.write("\n\n===========================\n\n")
		file.write(str(order_response))
		file.write("\n\n===========================\n\n")
		file.write(str(get_timestamp_formatted()))

	redirect(
		URL("devtest_exchange_03")
		)
	return ()

