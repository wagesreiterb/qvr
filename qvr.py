import qvrDateTime
import qvrRecording
import qvrScheduler
import qvrJobQueue
import time
from datetime import datetime


if __name__ == '__main__':

    # my_date_time = qvrDateTime.QfrDateTime()
    print(qvrDateTime.formatted_timestamp(), "[Info]", "starting qfr")

    record_date_time = "2023-10-08 01:31 AM EDT"
    recording_duration = qvrDateTime.time_to_seconds("01:30")
    print(qvrDateTime.formatted_timestamp(), "[Debug]", "recording_duration in seconds: ", recording_duration)


    # edt_time = datetime.strptime(record_date_time, '%Y-%m-%d %I:%M %p EDT')
    record_date_time_CET = qvrDateTime.convert_to_CET(record_date_time)

    print("start recording at: ", record_date_time_CET)

    ######################################
    # Define the target timestamp as a formatted string
    # target_time_str = "2023-10-07 14:44:00"
    target_time_str = record_date_time_CET
    # Convert the target time string to a datetime object
    # target_datetime = datetime.strptime(target_time_str, "%Y-%m-%d %H:%M:%S")
    target_datetime = datetime.strptime(record_date_time_CET, '%Y-%m-%d %H:%M:%S %Z%z')

    target_timestamp = int(target_datetime.timestamp()) # Convert the target datetime to a Unix timestamp
    current_timestamp = int(time.time())
    time_difference = target_timestamp - current_timestamp

    # Check if the target time is in the future
    if time_difference > 0:
        print(f"Waiting for {time_difference} seconds until the target timestamp...")
        time.sleep(time_difference)
        print("Wait is over. The target timestamp has been reached.")
    else:
        print("The target timestamp has already passed.")

    #######################################

    # my_qvr_recording = qvrRecording.QvrRecording()
    # my_qvr_recording.start_recording("abc")

    #######################################

    job_queue = qvrJobQueue.JobQueue()
    scheduler = qvrScheduler.QvrScheduler(job_queue)
    scheduler.run()







