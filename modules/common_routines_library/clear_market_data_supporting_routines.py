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

def clear_all_market_data():
    db.httpx03_market_data_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.httpx03_market_data_btcusdt_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.httpx03_raw_data_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.httpx03_raw_data_btcusdt_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.httpx03_status_messages_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx01_market_data_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx01_market_data_btcusd_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx01_raw_data_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx01_raw_data_btcusd_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx01_status_messages_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx02_market_data_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx02_market_data_btcusdt_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx02_raw_data_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx02_raw_data_btcusdt_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx02_status_messages_btcusdt.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx04_market_data_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx04_market_data_btcusd_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx04_raw_data_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx04_raw_data_btcusd_historical_24h.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    db.wsx04_status_messages_btcusd.truncate("RESTART IDENTITY CASCADE")
    db.commit()
    return ()
def clear_market_data_process():
    clear_market_data_x01_process()
    clear_market_data_x02_process()
    clear_market_data_x03_process()
    clear_market_data_x04_process() 
    return ()
def clear_market_data_x01_process():
    limit = MARKET_DATA_RECORDS_LIMIT // CUT_IN_HALF_DIVISOR
    wsx01_raw_data_btcusd_historical_24h_records = db(
        (db.wsx01_raw_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx01_raw_data_btcusd_historical_24h.id)
    len_wsx01_raw_data_btcusd_historical_24h_records = len(wsx01_raw_data_btcusd_historical_24h_records)
    if (len_wsx01_raw_data_btcusd_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx01_raw_data_btcusd_historical_24h_records = db(
            (db.wsx01_raw_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx01_raw_data_btcusd_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx01_raw_data_btcusd_historical_24h_records:
            x.delete_record()
            db.commit()
    wsx01_market_data_btcusd_historical_24h_records = db(
        (db.wsx01_market_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx01_market_data_btcusd_historical_24h.id)
    len_wsx01_market_data_btcusd_historical_24h_records = len(wsx01_market_data_btcusd_historical_24h_records)
    if (len_wsx01_market_data_btcusd_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx01_market_data_btcusd_historical_24h_records = db(
            (db.wsx01_market_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx01_market_data_btcusd_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx01_market_data_btcusd_historical_24h_records:
            x.delete_record()
            db.commit()
    return ()
def clear_market_data_x02_process():
    limit = MARKET_DATA_RECORDS_LIMIT // CUT_IN_HALF_DIVISOR
    wsx02_raw_data_btcusdt_historical_24h_records = db(
        (db.wsx02_raw_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx02_raw_data_btcusdt_historical_24h.id)
    len_wsx02_raw_data_btcusdt_historical_24h_records = len(wsx02_raw_data_btcusdt_historical_24h_records)
    if (len_wsx02_raw_data_btcusdt_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx02_raw_data_btcusdt_historical_24h_records = db(
            (db.wsx02_raw_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx02_raw_data_btcusdt_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx02_raw_data_btcusdt_historical_24h_records:
            x.delete_record()
            db.commit()
    wsx02_market_data_btcusdt_historical_24h_records = db(
        (db.wsx02_market_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx02_market_data_btcusdt_historical_24h.id)
    len_wsx02_market_data_btcusdt_historical_24h_records = len(wsx02_market_data_btcusdt_historical_24h_records)
    if (len_wsx02_market_data_btcusdt_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx02_market_data_btcusdt_historical_24h_records = db(
            (db.wsx02_market_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx02_market_data_btcusdt_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx02_market_data_btcusdt_historical_24h_records:
            x.delete_record()
            db.commit()
    return ()
def clear_market_data_x03_process():
    limit = MARKET_DATA_RECORDS_LIMIT // CUT_IN_HALF_DIVISOR
    httpx03_raw_data_btcusdt_historical_24h_records = db(
        (db.httpx03_raw_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.httpx03_raw_data_btcusdt_historical_24h.id)
    len_httpx03_raw_data_btcusdt_historical_24h_records = len(httpx03_raw_data_btcusdt_historical_24h_records)
    if (len_httpx03_raw_data_btcusdt_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        httpx03_raw_data_btcusdt_historical_24h_records = db(
            (db.httpx03_raw_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.httpx03_raw_data_btcusdt_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in httpx03_raw_data_btcusdt_historical_24h_records:
            x.delete_record()
            db.commit()
    httpx03_market_data_btcusdt_historical_24h_records = db(
        (db.httpx03_market_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.httpx03_market_data_btcusdt_historical_24h.id)
    len_httpx03_market_data_btcusdt_historical_24h_records = len(httpx03_market_data_btcusdt_historical_24h_records)
    if (len_httpx03_market_data_btcusdt_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        httpx03_market_data_btcusdt_historical_24h_records = db(
            (db.httpx03_market_data_btcusdt_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.httpx03_market_data_btcusdt_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in httpx03_market_data_btcusdt_historical_24h_records:
            x.delete_record()
            db.commit()
    return ()
def clear_market_data_x04_process():
    limit = MARKET_DATA_RECORDS_LIMIT // CUT_IN_HALF_DIVISOR
    wsx04_raw_data_btcusd_historical_24h_records = db(
        (db.wsx04_raw_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx04_raw_data_btcusd_historical_24h.id)
    len_wsx04_raw_data_btcusd_historical_24h_records = len(wsx04_raw_data_btcusd_historical_24h_records)
    if (len_wsx04_raw_data_btcusd_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx04_raw_data_btcusd_historical_24h_records = db(
            (db.wsx04_raw_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx04_raw_data_btcusd_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx04_raw_data_btcusd_historical_24h_records:
            x.delete_record()
            db.commit()
    wsx04_market_data_btcusd_historical_24h_records = db(
        (db.wsx04_market_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
        ).select(orderby = db.wsx04_market_data_btcusd_historical_24h.id)
    len_wsx04_market_data_btcusd_historical_24h_records = len(wsx04_market_data_btcusd_historical_24h_records)
    if (len_wsx04_market_data_btcusd_historical_24h_records > MARKET_DATA_RECORDS_LIMIT):
        wsx04_market_data_btcusd_historical_24h_records = db(
            (db.wsx04_market_data_btcusd_historical_24h.id > CONSTANT_TO_SELECT_ALL_RECORDS)
            ).select(
                orderby = db.wsx04_market_data_btcusd_historical_24h.id,
                limitby = (FIRST_ELEMENT, limit)
                )
        for x in wsx04_market_data_btcusd_historical_24h_records:
            x.delete_record()
            db.commit()
    return ()






