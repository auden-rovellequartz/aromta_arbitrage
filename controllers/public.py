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

@action("index")
@action.uses("public/index.html")
@action.uses(db, session)
def index():
	public_client = bitstamp.client.Public()
	trading_client = bitstamp.client.Trading(
		username = "034030",
		key = API_KEY_EXCHANGE_01,
		secret = API_SECRET_EXCHANGE_01,
		# secret = API_SECRET_EXCHANGE_01.decode('utf8'),
		)
	account_balance_01 = trading_client.account_balance()
	ticker_01 = public_client.ticker()
	output = DIV(
		DIV("EXCHANGE 01 ticker:"),
		DIV(ticker_01),
		DIV("EXCHANGE 01  account balance:"),
		DIV(account_balance_01)
		)
	return dict(
		output = output,
		)



