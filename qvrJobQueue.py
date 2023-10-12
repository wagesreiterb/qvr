import yaml
import time
from datetime import datetime
# pip3 install python-dateutil
from dateutil.parser import parse
import pytz


class JobQueue:
    def __init__(self):
        self.job_queue_waiting = []
        self.job_queue_running = []
        self.job_queue_finished = []

    def add_job(self, recording):
        # Todo: Error handling
        # self.check_job_for_errors(job)
        job_no_errors = True
        if job_no_errors:
            self.job_queue_waiting.append(recording)
        else:
            pass

    def del_job(self):
        pass

    def add_new_job_from_file(self):
        try:
            file_path = 'new_job.yaml'
            expected_keys = ["job_name", "start_time", "end_time", "channel"]
            with open(file_path, 'r') as file:
                new_recording = yaml.safe_load(file)
            missing_keys = []
            for key in expected_keys:
                if key not in new_recording:
                    missing_keys.append(key)
            if missing_keys:
                if len(missing_keys) == 1:
                    print(f"Error: The key '{missing_keys[0]}' is missing in the YAML data.")
                else:
                    print(f"Error: The following keys are missing in the YAML data: {', '.join(missing_keys)}")
            else:
                print("All expected keys are present in the YAML data.")
                self.add_job(new_recording)
                with open(file_path, 'w') as file:
                    file.write('')
        except yaml.YAMLError:
                print(f"Error: The file '{file_path}' is not a valid YAML file.")
        except Exception as e:
            # print(f"An error occurred: {str(e)}")
            pass


    def schedule_recording(self):
        # if startdate > now:
        # start recording
        print("----------------------------------------------")
        for job in self.job_queue_waiting:

            print(job)
            unix_timestamp_now = int(time.time())

            # Define the input date and time string
            input_time_str = "2023-10-07 01:50 PM EDT"

            # Use dateutil.parser.parse to parse the input string
            # input_datetime = parse(input_time_str)

            # Define the "EDT" time zone using pytz
            edt_timezone = pytz.timezone("US/Eastern")

            # Use dateutil.parser.parse with the recognized time zone
            input_datetime = parse(input_time_str, tzinfos={"EDT": edt_timezone})

            # Set the time zone of the parsed datetime to "EDT"
            # input_datetime = input_datetime.replace(tzinfo=edt_timezone)

            # Convert the parsed datetime to UTC
            input_datetime_utc = input_datetime.astimezone(pytz.utc)

            # Get the Unix timestamp (seconds since the epoch)
            unix_timestamp = int(input_datetime_utc.timestamp())

            print("Unix timestamp:", unix_timestamp)

            print("Now:", unix_timestamp_now)
            print("Unix timestamp:", unix_timestamp)

        print("----------------------------------------------")

    def list_jobs(self):
        print("Job Queue WAITING")
        for job in self.job_queue_waiting:
            print(job)
        print("Job Queue RUNNING")
        for job in self.job_queue_running:
            print(job)
        print("Job Queue FINISHED")
        for job in self.job_queue_finished:
            print(job)


