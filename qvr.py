import qvrDateTime
import subprocess
import time
from datetime import datetime


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    my_date_time = qvrDateTime.QfrDateTime()
    print(my_date_time.formatted_timestamp(), "[Info]", "starting qfr")

    record_date_time = "2023-10-08 01:31 AM EDT"
    recording_duration = my_date_time.time_to_seconds("01:30")
    print(my_date_time.formatted_timestamp(), "[Debug]", "recording_duration in seconds: ", recording_duration)


    # edt_time = datetime.strptime(record_date_time, '%Y-%m-%d %I:%M %p EDT')
    record_date_time_CET = my_date_time.convert_to_CET(record_date_time)

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


    server_url = "http://:8080"
    user = ""
    password = ""
    channel = "2101"

    # recording_duration = 12000  # ins seconds # 12000
    recording_duration = 65
    new_recording_duration = recording_duration
    recording_name = "testinger_"
    check_interval = 1
    start_time = time.time()

    while time.time() - start_time < recording_duration:
        new_recording_duration = int(recording_duration - (time.time() - start_time) + 1)
        print(my_date_time.formatted_timestamp(), "[Debug]", "recording_duration:", recording_duration)
        print(my_date_time.formatted_timestamp(), "[Debug]", "new_recording_duration:", new_recording_duration)
        if new_recording_duration < 60: # ffmpeg doesn't start properly if recording duration is < 6
            print(my_date_time.formatted_timestamp(), "[Info]", "new_recording_duration < 60, not starting recording anymore:", new_recording_duration)
            break  # Exit the loop
        try:
            command = "ffmpeg" \
                      + " -i " + server_url + "/" \
                      + user + "/" \
                      + password + "/" \
                      + channel + " -t " \
                      + str(new_recording_duration) \
                      + " -c:v copy -c:a copy " \
                      + recording_name + str(my_date_time.unix_time_stamp()) + ".mkv"
            print(my_date_time.formatted_timestamp(), "[Debug]", "command: ", command)
            process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(my_date_time.formatted_timestamp(), "[Info]", "ffmpeg has started")
            process.wait()

            if recording_duration >= 0:
                print(my_date_time.formatted_timestamp(), "[Error]", "ffmpeg died, restarting...")
            else:
                print(my_date_time.formatted_timestamp(), "[Info]", "ffmpeg completed successfully")

        except subprocess.CalledProcessError:
            print(my_date_time.formatted_timestamp(), "[Error]", "ffmpeg has ended unexpectedly with a non-zero return code.")
        except Exception as e:
            print(f"An error occurred: {str(e)}") # If any other exception is raised, handle it here

    print(my_date_time.formatted_timestamp(), "[Info]", "program has ended")