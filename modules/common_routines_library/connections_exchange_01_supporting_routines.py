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

def connections_manager_wsx01_btcusd():
	ws = websocket.WebSocketApp(
		"wss://ws.bitstamp.net",
		on_close = wsx01_btcusd_on_close,
		on_error = wsx01_btcusd_on_error,
		on_message = wsx01_btcusd_on_message,
		on_open = wsx01_btcusd_on_open,
		)
	t = Thread(target = ws.run_forever)
	t.start()
	return ()
def wsx01_btcusd_on_close(ws, close_status_code, close_msg):
	timestamp = get_timestamp()
	message = f"connection closed; Status Code: {close_status_code}; Message: {close_msg}"
	db.wsx01_status_messages_btcusd.insert(
		message = message,
		callback_category = "ON_CLOSE",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx01_btcusd_on_error(ws, error):
	timestamp = get_timestamp()
	message = f"error: {error}"
	db.wsx01_status_messages_btcusd.insert(
		message = message,
		callback_category = "ON_ERROR",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx01_btcusd_on_message(ws, message):
	timestamp = get_timestamp()
	raw_data = f"received: {message}"
	wsx01_raw_data_btcusd_records = db(
		db.wsx01_raw_data_btcusd.id > CONSTANT_TO_SELECT_ALL_RECORDS
		).select()
	len_wsx01_raw_data_btcusd_records = len(wsx01_raw_data_btcusd_records)
	if (len_wsx01_raw_data_btcusd_records == ONLY_ONE_RECORD_EXISTS):
		wsx01_raw_data_btcusd_records[EXISTING_RECORD].update_record(
			raw_data = raw_data,
			timestamp = timestamp,
			)
		db.commit()
	else:
		db.wsx01_raw_data_btcusd.truncate("RESTART IDENTITY CASCADE")
		db.commit()
		db.wsx01_raw_data_btcusd.insert(
			raw_data = raw_data,
			callback_category = "ON_MESSAGE",
			timestamp = timestamp,
			)
		db.commit()
	db.wsx01_raw_data_btcusd_historical_24h.insert(
		raw_data = raw_data,
		callback_category = "ON_MESSAGE",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx01_btcusd_on_open(ws):
	timestamp = get_timestamp()
	payload = json.dumps(
		{
			"event": "bts:subscribe",
			"data": 
			{
				"channel": "detail_order_book_btcusd"
			}
		}
		)
	ws.send(payload)    
	db.wsx01_status_messages_btcusd.insert(
		message = "connection opened",
		callback_category = "ON_OPEN",
		timestamp = timestamp,
		)
	db.commit()
	return ()
def wsx01_get_token():
	nonce = str(uuid.uuid4())
	timestamp = str(int(round(time.time() * 1000)))
	nonce_and_timestamp = nonce + timestamp
	message = (
		'BITSTAMP ' 
		+ 
		API_KEY_EXCHANGE_01 
		+ 
		'POST' 
		+ 
		'www.bitstamp.net/api/v2/websockets_token/' 
		+ 
		'' 
		+ 
		nonce_and_timestamp 
		+ 
		'v2'
		)
	message = message.encode('utf-8')
	byte_secret = bytes(API_SECRET_EXCHANGE_01, 'UTF-8')
	signature = hmac.new(byte_secret, message, hashlib.sha256).hexdigest()
	headers = \
	{
		'X-Auth': 'BITSTAMP ' + API_KEY_EXCHANGE_01,
		'X-Auth-Signature': signature,
		'X-Auth-Nonce': nonce,
		'X-Auth-Timestamp': timestamp,
		'X-Auth-Version': 'v2',
	}
	r = requests.post(
		'https://www.bitstamp.net/api/v2/websockets_token/',
		headers=headers
		)
	token = r.json()["token"]
	user_id = r.json()["user_id"]
	# return (r.content, r.json(), r.json()["token"], r.json()["user_id"], r.status_code)
	return (token, user_id)
