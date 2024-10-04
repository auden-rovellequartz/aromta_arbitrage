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
from .time_supporting_routines import get_timestamp

def connections_manager_wsx04_btcusd():
	ws = websocket.WebSocketApp(
		"wss://ws-auth.kraken.com/v2",
		on_close = wsx04_btcusd_on_close,
		on_error = wsx04_btcusd_on_error,
		on_message = wsx04_btcusd_on_message,
		on_open = wsx04_btcusd_on_open,
		)
	t = Thread(target = ws.run_forever)
	t.start()
	return ()
def connections_manager_wsx04_btcusd_ref():
	ws = websocket.WebSocketApp(
		"wss://ws.kraken.com",
		on_close = wsx04_btcusd_on_close,
		on_error = wsx04_btcusd_on_error,
		on_message = wsx04_btcusd_on_message,
		on_open = wsx04_btcusd_on_open,
		)
	t = Thread(target = ws.run_forever)
	t.start()
	return ()
def generate_token_x04():
	token = "UNDEFINED"
	api_path = '/0/private/GetWebSocketsToken'
	api_nonce = str(int(time.time()*1000))
	api_post = 'nonce=' + api_nonce
	api_sha256 = hashlib.sha256(api_nonce.encode('utf-8') + api_post.encode('utf-8'))
	api_hmac = hmac.new(
		base64.b64decode(API_SECRET_EXCHANGE_04), 
		api_path.encode('utf-8') + api_sha256.digest(), 
		hashlib.sha512
		)
	api_signature = base64.b64encode(api_hmac.digest())
	api_request = urllib.request.Request(
		'https://api.kraken.com/0/private/GetWebSocketsToken', 
		api_post.encode('utf-8')
		)
	api_request.add_header('API-Key', API_KEY_EXCHANGE_04)
	api_request.add_header('API-Sign', api_signature)
	api_response = urllib.request.urlopen(api_request).read().decode()
	token = json.loads(api_response)['result']['token']
	return (token)
def wsx04_btcusd_on_close(ws, close_status_code, close_msg):
	timestamp = get_timestamp()
	message = f"connection closed; Status Code: {close_status_code}; Message: {close_msg}"
	db.wsx04_status_messages_btcusd.insert(
		message = message,
		callback_category = "ON_CLOSE",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx04_btcusd_on_error(ws, error):
	timestamp = get_timestamp()
	message = f"error: {error}"
	db.wsx04_status_messages_btcusd.insert(
		message = message,
		callback_category = "ON_ERROR",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx04_btcusd_on_message(ws, message):
	timestamp = get_timestamp()
	raw_data = f"received: {message}"
	wsx04_raw_data_btcusd_records = db(
		db.wsx04_raw_data_btcusd.id > CONSTANT_TO_SELECT_ALL_RECORDS
		).select()
	len_wsx04_raw_data_btcusd_records = len(wsx04_raw_data_btcusd_records)
	if (len_wsx04_raw_data_btcusd_records == ONLY_ONE_RECORD_EXISTS):
		wsx04_raw_data_btcusd_records[EXISTING_RECORD].update_record(
			raw_data = raw_data,
			timestamp = timestamp,
			)
		db.commit()
	else:
		db.wsx04_raw_data_btcusd.truncate("RESTART IDENTITY CASCADE")
		db.commit()
		db.wsx04_raw_data_btcusd.insert(
			raw_data = raw_data,
			timestamp = timestamp,
			)
		db.commit()
	db.wsx04_raw_data_btcusd_historical_24h.insert(
		raw_data = raw_data,
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx04_btcusd_on_open(ws):
	timestamp = get_timestamp()
	token = generate_token_x04()
	payload = json.dumps(
		{
			"method": "add_order", 
			"params": {
				"order_type": "limit",
				"side": "sell",
				"limit_price": 111500.4,
				"order_qty": 0.00015,
				"symbol": "BTC/USD",
				"token": token
			},
			"req_id": 123456789
		}
		)
	ws.send(payload)    
	db.wsx04_status_messages_btcusd.insert(
		message = "connection opened",
		callback_category = "ON_OPEN",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx04_btcusd_on_open_ref(ws):
	timestamp = get_timestamp()
	payload = json.dumps(
		{
			"event": "subscribe",
			"pair": ["XBT/USD"],
			"subscription": 
			{
				"name": "book",
				"depth": 10
			}
		}
		)
	ws.send(payload)    
	db.wsx04_status_messages_btcusd.insert(
		message = "connection opened",
		callback_category = "ON_OPEN",
		timestamp = timestamp,
		)
	db.commit()
	return ()


