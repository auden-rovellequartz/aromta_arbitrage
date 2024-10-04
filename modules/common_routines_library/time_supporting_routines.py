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

def current_yyyymmddhhmmss_update():
	yyyymmddhhmmss = get_yyyymmddhhmmss_string(datetime.datetime.now())
	current_yyyymmddhhmmss_rows = db(db.current_yyyymmddhhmmss.id > CONSTANT_TO_SELECT_ALL_RECORDS).select()
	if (len(current_yyyymmddhhmmss_rows) != ONLY_ONE_RECORD_EXISTS):
		db.current_yyyymmddhhmmss.truncate("RESTART IDENTITY CASCADE")
		db.commit()
		db.current_yyyymmddhhmmss.insert(
			datetime = yyyymmddhhmmss,
			auto = "TRUE",
			)
		db.commit()
	elif (current_yyyymmddhhmmss_rows[0].auto == "TRUE"):
		current_yyyymmddhhmmss_rows[0].update_record(datetime = yyyymmddhhmmss)
		db.commit()
	elif (current_yyyymmddhhmmss_rows[0].auto == "SIMULATED_TRUE"): #THIS ELIF BRANCH IS PART OF THE PRODUCTION CODEBASE, BUT FOR TESTDEV PURPOSES ONLY. ENSURE EXECUTION OF THIS ELIF BRANCH IS NOT POSSIBLE FOR PRODUCTION CODE!!! 
		simulated_datetime = current_yyyymmddhhmmss_rows[0].datetime
		simulated_year = simulated_datetime[:4]
		simulated_month = simulated_datetime[4:6]
		simulated_day = simulated_datetime[6:8]
		simulated_hour = simulated_datetime[8:10]
		simulated_minute = simulated_datetime[10:12]
		simulated_second = simulated_datetime[12:14]
		dto_simulated_datetime = datetime.datetime(
			int(simulated_year),
			int(simulated_month),
			int(simulated_day),
			int(simulated_hour),
			int(simulated_minute),
			int(simulated_second),
			)
		dto_simulated_datetime_updated = (
			dto_simulated_datetime
			+
			timedelta(seconds = 1)
			)
		simulated_datetime_updated = get_yyyymmddhhmmss_string(dto_simulated_datetime_updated)
		current_yyyymmddhhmmss_rows[0].update_record(datetime = simulated_datetime_updated)
		db.commit()
	return ()
def determine_if_same_day(time_begin, time_end):
	result = "FALSE"
	if (time_begin[:LENGTH_OF_YYYYMMDD] == time_end[:LENGTH_OF_YYYYMMDD]):
		result = "TRUE"
	return (result)
def get_countdown_to_next_time(hour, minute):
	remaining_seconds = get_remaining_seconds_to_time(hour, minute)
	hours = str(remaining_seconds // SECONDS_PER_HOUR).zfill(2)
	minutes = str((remaining_seconds % SECONDS_PER_HOUR) // SECONDS_PER_MINUTE).zfill(2)
	seconds = str((remaining_seconds % SECONDS_PER_HOUR) % SECONDS_PER_MINUTE).zfill(2)
	coundown_string = ":".join([hours, minutes, seconds])
	return (coundown_string)
def get_current_yyyymmddhhmmss_record():
	current_yyyymmddhhmmss_rows = db(
		(db.current_yyyymmddhhmmss.id > CONSTANT_TO_SELECT_ALL_RECORDS)
		).select()
	if (len(current_yyyymmddhhmmss_rows) != ONLY_ONE_RECORD_EXISTS):
		current_yyyymmddhhmmss_update()
		current_yyyymmddhhmmss_rows = db(
			(db.current_yyyymmddhhmmss.id > CONSTANT_TO_SELECT_ALL_RECORDS)
			).select()
	return (current_yyyymmddhhmmss_rows[EXISTING_RECORD])
def get_dto_from_yyyymmddhhmm(yyyymmddhhmm):
	datetime_object = datetime.datetime.strptime(yyyymmddhhmm, "%Y%m%d%H%M")
	return (datetime_object)
def get_dto_from_yyyymmddhhmmss(yyyymmddhhmmss):
	datetime_object = datetime.datetime.strptime(yyyymmddhhmmss, "%Y%m%d%H%M%S")
	return (datetime_object)
def get_dto_date_now_no_secs():
	current_yyyymmddhhmmss_rows = db(
		(db.current_yyyymmddhhmmss.id > CONSTANT_TO_SELECT_ALL_RECORDS)
		).select()
	if (len(current_yyyymmddhhmmss_rows) != ONLY_ONE_RECORD_EXISTS):
		current_yyyymmddhhmmss_update()
		current_yyyymmddhhmmss_rows = db(
			(db.current_yyyymmddhhmmss.id > CONSTANT_TO_SELECT_ALL_RECORDS)
			).select()
		if (len(current_yyyymmddhhmmss_rows) != 1):
			session["status_msg"] = (
				"length of 'current_yyyymmddhhmmss_rows' should be exactly 1; "
				+
				"not "
				+
				str(len(current_yyyymmddhhmmss_rows))
				+
				"."
				)
			session["url_f"] = "conduit_logout"
			session["logged_in"] = FALSE
			redirect(
				URL("status")
				)
	dto_date_now = get_dto_from_yyyymmddhhmm(current_yyyymmddhhmmss_rows[0].datetime[:12])
	return (dto_date_now)
def get_dto_date_now():
	current_yyyymmddhhmmss_record = get_current_yyyymmddhhmmss_record()
	dto_datetime_now = get_dto_from_yyyymmddhhmmss(current_yyyymmddhhmmss_record.datetime)
	return (dto_datetime_now)
def get_duration_in_minutes(time_begin, time_end):
	same_day_indicator = determine_if_same_day(time_begin, time_end)
	dto_time_begin = get_dto_from_yyyymmddhhmm(time_begin)
	dto_time_end = get_dto_from_yyyymmddhhmm(time_end)
	total_duration = int((dto_time_end - dto_time_begin).total_seconds() / SECONDS_PER_MINUTE)
	if (same_day_indicator != "TRUE"):
		hhmm_time_begin = time_begin[LENGTH_OF_YYYYMMDD:LENGTH_OF_YYYYMMDDHHMM]
		hhmm_time_end = time_end[LENGTH_OF_YYYYMMDD:LENGTH_OF_YYYYMMDDHHMM]
		minutes_elapsed_time_begin = get_minutes_elapsed(hhmm_time_begin)
		first_day_duration = MINUTES_PER_DAY - minutes_elapsed_time_begin
		last_day_duration = get_minutes_elapsed(hhmm_time_end)
	else:
		first_day_duration = total_duration
		last_day_duration = total_duration
	return (total_duration, first_day_duration, last_day_duration, same_day_indicator)
def get_duration_in_seconds(time_begin, time_end):
	dto_time_begin = get_dto_from_yyyymmddhhmmss(time_begin)
	dto_time_end = get_dto_from_yyyymmddhhmmss(time_end)
	total_duration = (dto_time_end - dto_time_begin).total_seconds()
	return (total_duration)
def get_minutes_elapsed(hhmm):
	hours = int(hhmm[:LENGTH_OF_HH])
	minutes = int(hhmm[LENGTH_OF_HH:(LENGTH_OF_HH + LENGTH_OF_MM)])
	minutes_elapsed = (
		(hours * MINUTES_PER_HOUR)
		+
		minutes
		)
	return (minutes_elapsed)
def get_month_and_weekday(yyyymmddhhmm):
	month = "UNDEFINED"
	weekday = "UNDEFINED"
	datetime_object = datetime.datetime.strptime(yyyymmddhhmm[:LENGTH_OF_YYYYMMDD], "%Y%m%d")
	weekday = calendar.day_name[datetime_object.weekday()]
	month = calendar.month_name[datetime_object.month]
	return (month, weekday)
def get_next_weekday(current_weekday):
	current_index = DAYS_OF_WEEK.index(current_weekday)
	next_index = (current_index + INCREMENT_TO_NEXT_VALUE) % DAYS_PER_WEEK
	next_weekday = DAYS_OF_WEEK[next_index]
	return (next_weekday)
def get_remaining_seconds_to_time(hour, minute):
	remaining_seconds = 9999999
	dto_datetime_now = get_dto_date_now()
	remaining_seconds = int(
		(
			timedelta(hours = HOURS_PER_DAY) 
			- 
			(
				dto_datetime_now 
				- 
				dto_datetime_now.replace(hour = hour, minute = minute, second = ZERO))
			).total_seconds() 
		% 
		SECONDS_PER_DAY
		)
	return (remaining_seconds)
def get_time_am_pm(yyyymmddhhmm):
	am_pm = " AM"
	hour_digits = int(yyyymmddhhmm[8:10])
	minute_digits = int(yyyymmddhhmm[10:])
	if (hour_digits > 12):
		hour_digits = hour_digits - 12
		am_pm = " PM"
	time_am_pm = (
		str(hour_digits)
		+
		":"
		+
		str(ENSURE_TWO_CHARS_LENGTH_ENCODE + minute_digits)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		am_pm
		)
	return (time_am_pm)
def get_timestamp_no_secs():
	dto_date_now = get_dto_date_now_no_secs()
	timestamp = (
		str(dto_date_now.year)
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.month)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.day)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.hour)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.minute)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.second)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		)
	return (timestamp)
def get_timestamp():
	current_yyyymmddhhmmss_record = get_current_yyyymmddhhmmss_record()
	timestamp = current_yyyymmddhhmmss_record.datetime
	return (timestamp)
def get_timestamp_formatted():
	dto_date_now = get_dto_date_now()
	dto_day_of_week = calendar.day_name[dto_date_now.weekday()]
	dto_month_name = calendar.month_name[dto_date_now.month]
	timestamp_formatted = (
		dto_day_of_week
		+
		", "
		+
		dto_month_name
		+ 
		" "
		+ 
		str(dto_date_now.day)
		+
		", "
		+
		str(dto_date_now.year)
		+ 
		" "
		+ 
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.hour)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+ 
		":"
		+ 
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.minute)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+ 
		":"
		+ 
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(dto_date_now.second)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		)
	return (timestamp_formatted)
def get_yyyymmdd(datetime_object):
	yyyymmdd = (
		str(datetime_object.year)
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(datetime_object.month)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		+
		str(
			ENSURE_TWO_CHARS_LENGTH_ENCODE + int(datetime_object.day)
			)[ENSURE_TWO_CHARS_LENGTH_DECODE:]
		)
	return (yyyymmdd)
def get_yyyymmddhhmmss_string(datetime_object):
	year = str(datetime_object.year)
	if (len(str(datetime_object.month)) == 1):
		month = "".join(("0", str(datetime_object.month)))
	else:
		month = str(datetime_object.month)
	if (len(str(datetime_object.day)) == 1):
		day = "".join(("0", str(datetime_object.day)))
	else:
		day = str(datetime_object.day)
	if (len(str(datetime_object.hour)) == 1):
		hour = "".join(("0", str(datetime_object.hour)))
	else:
		hour = str(datetime_object.hour)
	if (len(str(datetime_object.minute)) == 1):
		minute =  "".join(("0", str(datetime_object.minute)))
	else:
		minute = str(datetime_object.minute)
	if (len(str(datetime_object.second)) == 1):
		second =  "".join(("0", str(datetime_object.second)))
	else:
		second = str(datetime_object.second)
	set_sequence = (year, month, day, hour, minute, second)
	yyyymmddhhmmss = "".join(set_sequence)
	return (yyyymmddhhmmss)



