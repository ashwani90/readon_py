from datetime import datetime

def get_current_datetime():
    return datetime.datetime.now()

def get_current_date():
    return datetime.date.today()

def get_datetime_string():
    now = datetime.now()
    date_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return date_time

def get_string_from_datetime(date_time):
    return date_time.strftime("%Y-%m-%d %H:%M:%S")

def convert_format_datetime(date,format):
    return datetime.strptime(date, format)

def convert_datetime_to_timestamp(date_time=False,format=False):
    if not date_time:
        return datetime.timestamp(datetime.now())
    return datetime.timestamp(convert_format_datetime(date_time,format))

def convert_timestamp_to_datetime(timestamp):
    timestamp = int(timestamp)
    date_time = datetime.fromtimestamp(timestamp)
    return get_string_from_datetime(date_time)
