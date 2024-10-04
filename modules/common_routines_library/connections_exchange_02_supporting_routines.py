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
from .time_supporting_routines import get_timestamp

def connections_manager_wsx02_btcusdt():
	ws = websocket.WebSocketApp(
		"wss://stream.binance.us:9443/ws/btcusdt@depth",
		on_close = wsx02_btcusdt_on_close,
		on_error = wsx02_btcusdt_on_error,
		on_message = wsx02_btcusdt_on_message,
		on_open = wsx02_btcusdt_on_open,
		)
	t = Thread(target = ws.run_forever)
	t.start()
	return ()
def wsx02_btcusdt_on_close(ws, close_status_code, close_msg):
	timestamp = get_timestamp()
	message = f"connection closed; Status Code: {close_status_code}; Message: {close_msg}"
	db.wsx02_status_messages_btcusdt.insert(
		message = message,
		callback_category = "ON_CLOSE",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx02_btcusdt_on_error(ws, error):
	timestamp = get_timestamp()
	message = f"error: {error}"
	db.wsx02_status_messages_btcusdt.insert(
		message = message,
		callback_category = "ON_ERROR",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx02_btcusdt_on_message(ws, message):
	timestamp = get_timestamp()
	raw_data = f"received: {message}"
	wsx02_raw_data_btcusdt_records = db(
		db.wsx02_raw_data_btcusdt.id > CONSTANT_TO_SELECT_ALL_RECORDS
		).select()
	len_wsx02_raw_data_btcusdt_records = len(wsx02_raw_data_btcusdt_records)
	if (len_wsx02_raw_data_btcusdt_records == ONLY_ONE_RECORD_EXISTS):
		wsx02_raw_data_btcusdt_records[EXISTING_RECORD].update_record(
			raw_data = raw_data,
			timestamp = timestamp,
			)
		db.commit()
	else:
		db.wsx02_raw_data_btcusdt.truncate("RESTART IDENTITY CASCADE")
		db.commit()
		db.wsx02_raw_data_btcusdt.insert(
			raw_data = raw_data,
			callback_category = "ON_MESSAGE",
			timestamp = timestamp,
			)
		db.commit()
	db.wsx02_raw_data_btcusdt_historical_24h.insert(
		raw_data = raw_data,
		callback_category = "ON_MESSAGE",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx02_btcusdt_on_open(ws):
	timestamp = get_timestamp()
	db.wsx02_status_messages_btcusdt.insert(
		message = "connection opened",
		callback_category = "ON_OPEN",
		timestamp = timestamp,
		)
	db.commit()
	return ()


