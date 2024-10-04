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
from .connections_exchange_01_supporting_routines import wsx01_get_token

def websockets_exchange_01_is_ws_connected(ws):
    ws.recv()
    return ws.connected
def websockets_exchange_01_private_on_close(ws):
    with open("_websocket_exchange_01_private_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_01_private_on_error(ws, error):
    with open("_websocket_exchange_01_private_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_01_private_on_message(ws, message):
    with open("_websocket_exchange_01_private_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_01_private_on_open(ws):
    token_data = wsx01_get_token()
    token = token_data[TOKEN]
    user_id = token_data[USER_ID]
    channel_name = "private-my_orders_btcusdt"
    channel = channel_name + "-" + str(user_id)
    auth_payload = json.dumps(
        {
            "event": "bts:subscribe",
            "data": 
            {
                "channel": channel,
                "auth": token
            }
        }
        )
    ws.send(auth_payload)    
    with open("_websocket_exchange_01_private_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_01_public_on_close(ws):
    with open("_websocket_exchange_01_public_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_01_public_on_error(ws, error):
    with open("_websocket_exchange_01_public_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_01_public_on_message(ws, message):
    with open("_websocket_exchange_01_public_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_01_public_on_open(ws):
    with open("_websocket_exchange_01_public_on_open", "a+") as file: 
        ws.send(
            json.dumps(
                {
                    "event": "bts:subscribe",
                    "data": 
                    {
                        "channel": "live_trades_btcusd"
                    }
                }
                )
            )    
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_02_btcusdt_depth_stream_on_close(ws, code, message): 
    with open("_websocket_exchange_02_btcusdt_depth_stream_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_02_btcusdt_depth_stream_on_error(ws, error):
    with open("_websocket_exchange_02_btcusdt_depth_stream_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_02_btcusdt_depth_stream_on_message(ws, message):
    with open("_websocket_exchange_02_btcusdt_depth_stream_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_02_btcusdt_depth_stream_on_open(ws, message):
    with open("_websocket_exchange_02_btcusdt_depth_stream_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_02_private_on_close(ws, code, message): 
    with open("_websocket_exchange_02_private_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_02_private_on_error(ws, error):
    with open("_websocket_exchange_02_private_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_02_private_on_message(ws, message):
    with open("_websocket_exchange_02_private_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_02_private_on_open(ws):
    timestamp = int(round(time.time() * 1000))
    data = {
        "symbol": "BTCUSDT",
        "side": "SELL",
        "type": "LIMIT",
        "timeInForce": "GTC",
        "price": "100400",
        "quantity": "0.0002",
        "timestamp": timestamp
    }
    signature = websockets_get_signature_exchange_02(data, API_SECRET_EXCHANGE_02)
    payload = json.dumps(
        {
            "id": str(timestamp),
            "method": "order.place",
            "params": 
            {
                "symbol": "BTCUSDT",
                "side": "SELL",
                "type": "LIMIT",
                "timeInForce": "GTC",
                "price": "100400",
                "quantity": "0.0002",
                "apiKey": API_KEY_EXCHANGE_02,
                "timestamp": timestamp,
                "signature": signature
            }
        }
        )
    ws.send(payload)   
    with open("_websocket_exchange_02_private_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
        file.write("\n\n========================\n\n")
        file.write(str(signature))
        file.write("\n\n========================\n\n")
        file.write(str(timestamp))
    return ()
def websockets_exchange_02_public_on_close(ws, code, message): 
    with open("_websocket_exchange_02_public_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_02_public_on_error(ws, error):
    with open("_websocket_exchange_02_public_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_02_public_on_message(ws, message):
    with open("_websocket_exchange_02_public_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_02_public_on_open(ws):
    with open("_websocket_exchange_02_public_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_03_private_on_close(ws):
    with open("_websocket_exchange_03_private_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_03_private_on_error(ws, error):
    with open("_websocket_exchange_03_private_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_03_private_on_message(ws, message):
    with open("_websocket_exchange_03_private_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_03_private_on_open(ws):
    with open("_websocket_exchange_03_private_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_03_public_on_close(ws):
    with open("_websocket_exchange_03_public_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_03_public_on_error(ws, error):
    with open("_websocket_exchange_03_public_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_03_public_on_message(ws, message):
    with open("_websocket_exchange_03_public_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_03_public_on_open(ws):
    with open("_websocket_exchange_03_public_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_04_private_on_close(ws):
    with open("_websocket_exchange_04_private_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_04_private_on_error(ws, error):
    with open("_websocket_exchange_04_private_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_04_private_on_message(ws, message):
    with open("_websocket_exchange_04_private_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_04_private_on_open(ws):
    with open("_websocket_exchange_04_private_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_exchange_04_public_on_close(ws):
    with open("_websocket_exchange_04_public_on_close", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection closed")
    return ()
def websockets_exchange_04_public_on_error(ws, error):
    with open("_websocket_exchange_04_public_on_error", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Error: {error}")
    return ()
def websockets_exchange_04_public_on_message(ws, message):
    with open("_websocket_exchange_04_public_on_message", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write(f"Received: {message}")
    return ()
def websockets_exchange_04_public_on_open(ws):
    with open("_websocket_exchange_04_public_on_open", "a+") as file:
        file.write("\n\n========================\n\n")
        file.write("Connection opened")
    return ()
def websockets_get_signature_exchange_02(data, secret):
    postdata = urllib.parse.urlencode(data)
    message = postdata.encode()
    # query_string = '&'.join([f"{d[0]}={d[1]}" for d in data])
    byte_secret = bytes(secret, 'UTF-8')
    signature = hmac.new(byte_secret, message, hashlib.sha256).hexdigest()
    return (signature)
