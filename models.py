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

from .common import db, Field
from pydal.validators import *

migrate_status = True

db.define_table("current_yyyymmddhhmmss",
	Field("datetime", default = "00010101000000"),
	Field("seconds_since_reset", default = "0"),
	Field("auto", default = "TRUE"),
	migrate = migrate_status,
	)
db.define_table("httpx03_market_data_btcusdt",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("httpx03_market_data_btcusdt_historical_24h",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("httpx03_raw_data_btcusdt",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("httpx03_raw_data_btcusdt_historical_24h",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("httpx03_status_messages_btcusdt",
	Field("message", default = "UNDEFINED"),
	Field("callback_category", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("request_ids",
	Field("exchange_01", default = "UNDEFINED"),
	Field("exchange_02", default = "UNDEFINED"),
	Field("exchange_03", default = "UNDEFINED"),
	Field("exchange_04", default = "UNDEFINED"),
	migrate = migrate_status,
	)
db.define_table("wsx01_market_data_btcusd",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx01_market_data_btcusd_historical_24h",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx01_raw_data_btcusd",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx01_raw_data_btcusd_historical_24h",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx01_status_messages_btcusd",
	Field("message", default = "UNDEFINED"),
	Field("callback_category", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx02_market_data_btcusdt",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx02_market_data_btcusdt_historical_24h",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx02_raw_data_btcusdt",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx02_raw_data_btcusdt_historical_24h",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx02_status_messages_btcusdt",
	Field("message", default = "UNDEFINED"),
	Field("callback_category", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx04_market_data_btcusd",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx04_market_data_btcusd_historical_24h",
	Field("bid_or_ask", default = "UNDEFINED"),
	Field("price_best_effective", default = "UNDEFINED"),
	Field("amount_cummulative", default = "UNDEFINED"),
	Field("depth_pricepoint", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx04_raw_data_btcusd",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx04_raw_data_btcusd_historical_24h",
	Field("raw_data", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)
db.define_table("wsx04_status_messages_btcusd",
	Field("message", default = "UNDEFINED"),
	Field("callback_category", default = "UNDEFINED"),
	Field("timestamp", default = "00010101000000"),
	migrate = migrate_status,
	)

db.commit()


