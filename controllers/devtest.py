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

@action("devtest_btcusdt_depth_stream_exchange_02_b")
@action.uses("devtest/devtest_btcusdt_depth_stream_exchange_02_b.html")
@action.uses(db, session)
def devtest_btcusdt_depth_stream_exchange_02_b():
	result = session.get("result_devtest_btcusdt_depth_stream_exchange_02")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_exchange_01")
@action.uses("devtest/devtest_exchange_01.html")
@action.uses(db, session)
def devtest_exchange_01():
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	form = form_submit_button("start public websocket", "conduit_devtest_websocket_public_exchange_01")
	form_b = form_submit_button("start private websocket", "conduit_devtest_websocket_private_exchange_01")
	return dict(
		# form = websockets_get_token_exchange_01(),
		form = form,
		form_b = form_b,
		home = home,
		)
@action("devtest_exchange_02")
@action.uses("devtest/devtest_exchange_02.html")
@action.uses(db, session)
def devtest_exchange_02():
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	form = form_submit_button("start public websocket", "conduit_devtest_websocket_public_exchange_02")
	form_b = form_submit_button("start private websocket", "conduit_devtest_websocket_private_exchange_02")
	form_c = form_submit_button("start btcusdt@depth stream", "conduit_devtest_btcusdt_depth_stream_exchange_02")
	return dict(
		form = form,
		form_b = form_b,
		form_c = form_c,
		home = home,
		)
@action("devtest_exchange_03")
@action.uses("devtest/devtest_exchange_03.html")
@action.uses(db, session)
def devtest_exchange_03():
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	form = form_submit_button("start public websocket", "conduit_devtest_websocket_public_exchange_03")
	form_b = form_submit_button("start private websocket", "conduit_devtest_websocket_private_exchange_03")
	form_c = form_submit_button("test sell order", "conduit_test_sell_order_exchange_03")
	return dict(
		form = form,
		form_b = form_b,
		form_c = form_c,
		home = home,
		)
@action("devtest_exchange_04")
@action.uses("devtest/devtest_exchange_04.html")
@action.uses(db, session)
def devtest_exchange_04():
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	form = form_submit_button("start public websocket", "conduit_devtest_websocket_public_exchange_04")
	form_b = form_submit_button("start private websocket", "conduit_devtest_websocket_private_exchange_04")
	return dict(
		form = form,
		form_b = form_b,
		home = home,
		)
@action("devtest_home")
@action.uses("devtest/devtest_home.html")
@action.uses(db, session)
def devtest_home():
	clear_all_market_data_div = DIV(
		A(
			"CLEAR ALL MARKET DATA",
			_href = URL("conduit_clear_all_market_data")
			)
		)
	devtest_exchange_01_div = DIV(
		A(
			"Devtest EXCHANGE_01",
			_href = URL("devtest_exchange_01")
			)
		)
	devtest_exchange_02_div = DIV(
		A(
			"Devtest EXCHANGE_02",
			_href = URL("devtest_exchange_02")
			)
		)
	devtest_exchange_03_div = DIV(
		A(
			"Devtest EXCHANGE_03",
			_href = URL("devtest_exchange_03")
			)
		)
	devtest_exchange_04_div = DIV(
		A(
			"Devtest EXCHANGE_04",
			_href = URL("devtest_exchange_04")
			)
		)
	return dict(
		clear_all_market_data_div = clear_all_market_data_div,
		devtest_exchange_01_div = devtest_exchange_01_div,
		devtest_exchange_02_div = devtest_exchange_02_div,
		devtest_exchange_03_div = devtest_exchange_03_div,
		devtest_exchange_04_div = devtest_exchange_04_div,
		)
@action("devtest_websocket_private_exchange_01_b")
@action.uses("devtest/devtest_websocket_private_exchange_01_b.html")
@action.uses(db, session)
def devtest_websocket_private_exchange_01_b():
	result = session.get("result_devtest_websocket_private_exchange_01")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_private_exchange_02_b")
@action.uses("devtest/devtest_websocket_private_exchange_02_b.html")
@action.uses(db, session)
def devtest_websocket_private_exchange_02_b():
	result = session.get("result_devtest_websocket_private_exchange_02")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_private_exchange_03_b")
@action.uses("devtest/devtest_websocket_private_exchange_03_b.html")
@action.uses(db, session)
def devtest_websocket_private_exchange_03_b():
	result = session.get("result_devtest_websocket_private_exchange_03")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_private_exchange_04_b")
@action.uses("devtest/devtest_websocket_private_exchange_04_b.html")
@action.uses(db, session)
def devtest_websocket_private_exchange_04_b():
	result = session.get("result_devtest_websocket_private_exchange_04")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_public_exchange_01_b")
@action.uses("devtest/devtest_websocket_public_exchange_01_b.html")
@action.uses(db, session)
def devtest_websocket_public_exchange_01_b():
	result = session.get("result_devtest_websocket_public_exchange_01")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_public_exchange_02_b")
@action.uses("devtest/devtest_websocket_public_exchange_02_b.html")
@action.uses(db, session)
def devtest_websocket_public_exchange_02_b():
	result = session.get("result_devtest_websocket_public_exchange_02")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_public_exchange_03_b")
@action.uses("devtest/devtest_websocket_public_exchange_03_b.html")
@action.uses(db, session)
def devtest_websocket_public_exchange_03_b():
	result = session.get("result_devtest_websocket_public_exchange_03")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)
@action("devtest_websocket_public_exchange_04_b")
@action.uses("devtest/devtest_websocket_public_exchange_04_b.html")
@action.uses(db, session)
def devtest_websocket_public_exchange_04_b():
	result = session.get("result_devtest_websocket_public_exchange_04")
	home = DIV(
		A(
			"DevTest Home",
			_href = URL("devtest_home")
			)
		)
	return dict(
		result = result,
		home = home,
		)

