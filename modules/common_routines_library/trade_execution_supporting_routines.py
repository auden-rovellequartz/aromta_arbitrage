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

def cancel_buy_order_exchange_01(asset, amount, price, denomination):
	return ()
def cancel_buy_order_exchange_02(asset, amount, price, denomination):
	return ()
def cancel_buy_order_exchange_03(asset, amount, price, denomination):
	return ()
def cancel_buy_order_exchange_04(asset, amount, price, denomination):
	return ()
def cancel_sell_order_exchange_01(asset, amount, price, denomination):
	return ()
def cancel_sell_order_exchange_02(asset, amount, price, denomination):
	return ()
def cancel_sell_order_exchange_03(asset, amount, price, denomination):
	return ()
def cancel_sell_order_exchange_04(asset, amount, price, denomination):
	return ()
def generate_signature_x03(data, secret):
	signature = "UNDEFINED"
	# sorted_data = {k: data[k] for k in sorted(data)}
	# concatenated_values = ''.join([str(value) for value in sorted_data.values()]) + secret
	# signature = hmac.new(secret.encode(), concatenated_values.encode(), hashlib.sha256).hexdigest()
	return (signature)
def get_request_id_x01():
	request_id = "UNDEFINED"
	request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	len_request_ids_records = len(request_ids_records)
	if (len_request_ids_records != ONLY_ONE_RECORD_EXISTS):
		initialize_request_ids()
		request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	request_id = str(
		int(request_ids_records[EXISTING_RECORD].exchange_01) + INCREMENT_TO_NEXT_VALUE
		)
	request_ids_records[EXISTING_RECORD].update_record(exchange_01 = request_id)
	db.commit()
	return (request_id)
def get_request_id_x02():
	request_id = "UNDEFINED"
	request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	len_request_ids_records = len(request_ids_records)
	if (len_request_ids_records != ONLY_ONE_RECORD_EXISTS):
		initialize_request_ids()
		request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	request_id = str(
		int(request_ids_records[EXISTING_RECORD].exchange_02) + INCREMENT_TO_NEXT_VALUE
		)
	request_ids_records[EXISTING_RECORD].update_record(exchange_02 = request_id)
	db.commit()
	return (request_id)
def get_request_id_x03():
	request_id = "UNDEFINED"
	request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	len_request_ids_records = len(request_ids_records)
	if (len_request_ids_records != ONLY_ONE_RECORD_EXISTS):
		initialize_request_ids()
		request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	request_id = str(
		int(request_ids_records[EXISTING_RECORD].exchange_03) + INCREMENT_TO_NEXT_VALUE
		)
	request_ids_records[EXISTING_RECORD].update_record(exchange_03 = request_id)
	db.commit()
	return (request_id)
def get_request_id_x04():
	request_id = "UNDEFINED"
	request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	len_request_ids_records = len(request_ids_records)
	if (len_request_ids_records != ONLY_ONE_RECORD_EXISTS):
		initialize_request_ids()
		request_ids_records = db(db.request_ids.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	request_id = str(
		int(request_ids_records[EXISTING_RECORD].exchange_04) + INCREMENT_TO_NEXT_VALUE
		)
	request_ids_records[EXISTING_RECORD].update_record(exchange_04 = request_id)
	db.commit()
	return (request_id)
def initialize_request_ids():
	db.request_ids.truncate("RESTART IDENTITY CASCADE")
	db.commit()
	db.request_ids.insert(
		exchange_01 = "100000000",
		exchange_02 = "100000000",
		exchange_03 = "100000000",
		exchange_04 = "100000000",
		)
	db.commit()
	return ()
def place_buy_order_exchange_01(asset, amount, price, denomination):
	return ()
def place_buy_order_exchange_02(asset, amount, price, denomination):
	return ()
def place_buy_order_exchange_03(asset, amount, price, denomination):
	order_response = "UNDEFINED"
	market = "UNDEFINED"
	if ((asset == "BTC") and (denomination == "USDT")):
		market = "BTCUSDT"
	if (market != "UNDEFINED"):
		post_url = "https://api.dex-trade.com/v1/private/create-order"
		request_id = get_request_id_x03()
		order_data = {
			"pair": str(market),
			"rate": str(price),
			"request_id": str(request_id),
			"type": str(BUY_ON_EXCHANGE_03),
			"type_trade": str(LIMIT_ORDER_ON_EXCHANGE_03),
			"volume": str(amount),
		}
		# signature = generate_signature_x03(order_data, API_SECRET_EXCHANGE_03)
		concatenated_values = market + price + request_id + str(BUY_ON_EXCHANGE_03) + str(LIMIT_ORDER_ON_EXCHANGE_03) + amount + API_SECRET_EXCHANGE_03
		signature = hmac.new(secret.encode(), concatenated_values.encode(), hashlib.sha256).hexdigest()

		headers = \
		{
			"content-type": "application/json",
			"login-token": API_KEY_EXCHANGE_03,
			"x-auth-sign": signature,
		}
		try:
			order_response = requests.post(
				post_url, 
				headers = headers, 
				data = json.dumps(order_data)
				).json()
		except Exception as error:
			argument_list = [
				"LOG_AND_CONTINUE",
				(inspect.currentframe().f_code.co_name, "reference point #0"),
				error,
				]
			error_processing(argument_list)
	return (order_response)
def place_buy_order_exchange_04(asset, amount, price, denomination):
	return ()
def place_sell_order_exchange_01(asset, amount, price, denomination):
	return ()
def place_sell_order_exchange_02(asset, amount, price, denomination):
	return ()
def place_sell_order_exchange_03(asset, amount, price, denomination):
	from hashlib import sha256
	order_response = "UNDEFINED"
	market = "UNDEFINED"
	if ((asset == "BTC") and (denomination == "USDT")):
		market = "BTCUSDT"
	if (market != "UNDEFINED"):
		post_url = "https://api.dex-trade.com/v1/private/create-order"
		request_id = "123456789"
		order_data = {
			"pair": "BTCUSDT",
			"rate": price,
			"request_id": request_id,
			"type": 1,			# sell
			"type_trade": 0, 	# limit
			"volume": amount,
		}
		concatenated_values = "BTCUSDT" + price + request_id + "1" + "0" + amount + "fd1a3c117e8ef1ae5f3444abf225ab839d6614ac0dc101829ac23d2ee9c1a9c7"
		# signature = hmac.new("397597769aef3a65f489860c994426a229d051e2f0535b94dfe9c05f0706fec8".encode(), concatenated_values.encode(), hashlib.sha256).hexdigest()
		signature = sha256(concatenated_values.encode()).hexdigest()
		headers = {
			"content-type": "application/json",
			"login-token": API_KEY_EXCHANGE_03,
			"x-auth-sign": signature,
		}
		try:
			order_response = requests.post(
				post_url, 
				headers = headers, 
				data = json.dumps(order_data)
				).json()
		except Exception as error:
			argument_list = [
				"LOG_AND_CONTINUE",
				(inspect.currentframe().f_code.co_name, "reference point #0"),
				error,
				]
			error_processing(argument_list)
	return (order_response)
def place_sell_order_exchange_03_ref(asset, amount, price, denomination):
	order_response = "UNDEFINED"
	market = "UNDEFINED"
	post_url = "https://api.dex-trade.com/v1/private/orders"
	request_id = get_request_id_x03()
	order_data = {
		"request_id": request_id,
	}
	concatenated_values = request_id + API_SECRET_EXCHANGE_03
	signature = hmac.new(API_SECRET_EXCHANGE_03.encode(), concatenated_values.encode(), hashlib.sha256).hexdigest()
	headers = {
		"content-type": "application/json",
		"login-token": API_KEY_EXCHANGE_03,
		"x-auth-sign": signature,
	}
	try:
		order_response = requests.post(
			post_url, 
			headers = headers, 
			data = json.dumps(order_data)
			).json()
	except Exception as error:
		argument_list = [
			"LOG_AND_CONTINUE",
			(inspect.currentframe().f_code.co_name, "reference point #0"),
			error,
			]
		error_processing(argument_list)
	"""
	if ((asset == "BTC") and (denomination == "USDT")):
		market = "BTCUSDT"
	if (market != "UNDEFINED"):
		post_url = "https://api.dex-trade.com/v1/private/create-order"
		request_id = get_request_id_x03()
		order_data = {
			# "pair": str(market),
			"pair": 1041,
			"rate": price,
			"request_id": request_id,
			"type": BUY_ON_EXCHANGE_03,
			"type_trade": LIMIT_ORDER_ON_EXCHANGE_03,
			"volume": amount,
		}
		concatenated_values = "1041" + price + str(request_id) + str(BUY_ON_EXCHANGE_03) + str(LIMIT_ORDER_ON_EXCHANGE_03) + str(amount) + API_SECRET_EXCHANGE_03
		signature = hmac.new(API_SECRET_EXCHANGE_03.encode(), concatenated_values.encode(), hashlib.sha256).hexdigest()
		# order_data = \
		# {
		# 	"type_trade": LIMIT_ORDER_ON_EXCHANGE_03,
		# 	"type": SELL_ON_EXCHANGE_03,
		# 	"rate": str(price),
		# 	"volume": str(amount),
		# 	"pair": str(market),
		# 	"request_id": str(request_id),
		# }
		# signature = generate_signature_x03(order_data, API_SECRET_EXCHANGE_03)
		headers = \
		{
			"content-type": "application/json",
			"login-token": API_KEY_EXCHANGE_03,
			"x-auth-sign": signature,
		}
		try:
			order_response = requests.post(
				post_url, 
				headers = headers, 
				data = json.dumps(order_data)
				).json()
		except Exception as error:
			argument_list = [
				"LOG_AND_CONTINUE",
				(inspect.currentframe().f_code.co_name, "reference point #0"),
				error,
				]
			error_processing(argument_list)
	"""
	return (order_response)
def place_sell_order_exchange_04(asset, amount, price, denomination):
	return ()
