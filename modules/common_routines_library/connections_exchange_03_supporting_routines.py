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

def connections_manager_httpx03_btcusdt():
	t = Thread(target = conn_manager_httpx03_btcusdt)
	t.start()
	return ()
def conn_manager_httpx03_btcusdt():
	db.httpx03_raw_data_btcusdt_historical_24h.truncate("RESTART IDENTITY CASCADE")
	db.commit()
	while(True):
		timestamp = get_timestamp()
		raw_data = requests.get("https://api.dex-trade.com/v1/public/book?pair=BTCUSDT")
		db.httpx03_raw_data_btcusdt_historical_24h.insert(
			raw_data = raw_data.json(),
			timestamp = timestamp,
			)
		db.commit()
		time.sleep(1)
	return ()




