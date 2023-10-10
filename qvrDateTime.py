from datetime import datetime
import pytz


def formatted_timestamp():
    current_time = datetime.now()
    formatted_time = current_time.strftime("[%Y-%m-%d %H:%M:%S]")

    return formatted_time


def time_to_seconds(time_str):
    try:
        # Split the time string into hours and minutes
        hours, minutes = map(int, time_str.split(":"))

        # Calculate the total seconds
        total_seconds = (hours * 3600) + (minutes * 60)

        return total_seconds
    except ValueError:
        # Handle invalid input gracefully
        return None


def unix_time_stamp():
    current_datetime = datetime.utcnow()
    unix_timestamp = int(current_datetime.timestamp())

    return unix_timestamp


def convert_to_CET(_date_time):
    # Define the input time string in EDT
    # edt_time_str = "2023-10-07 02:00 AM EDT"
    edt_time_str = _date_time

    # Parse the time string into a datetime object
    edt_time = datetime.strptime(edt_time_str, '%Y-%m-%d %I:%M %p EDT')

    # Set the timezone to EDT
    edt_timezone = pytz.timezone('America/New_York')
    edt_time = edt_timezone.localize(edt_time)

    # Convert to CET
    cet_timezone = pytz.timezone('Europe/Berlin')
    cet_time = edt_time.astimezone(cet_timezone)

    print("EDT Time:", edt_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))
    print("CET Time:", cet_time.strftime('%Y-%m-%d %H:%M:%S %Z%z'))

    return cet_time.strftime('%Y-%m-%d %H:%M:%S %Z%z')


class QfrDateTime:
    def __init__(self):
        pass
