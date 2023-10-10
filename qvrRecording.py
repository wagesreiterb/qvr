import qvrConfig
import qvrDateTime
import subprocess
import time


class Person:

    def __init__(self, p1Name, p2Name):
        self.p1Name = p1Name
        self.p2Name = p2Name

    def getNameP1(self):
        return self.p1Name


class QvrRecording:
    def __init__(self):
        # my_date_time = qvrDateTime.QfrDateTime()
        pass

    def start_recording(self, jobID):
        server_url = qvrConfig.server_url
        user = qvrConfig.user
        password = qvrConfig.password
        channel = "2101"

        # recording_duration = 12000  # ins seconds # 12000
        recording_duration = 65
        new_recording_duration = recording_duration
        recording_name = "testinger_"
        check_interval = 1
        start_time = time.time()

        while time.time() - start_time < recording_duration:
            new_recording_duration = int(recording_duration - (time.time() - start_time) + 1)
            print(qvrDateTime.formatted_timestamp(), "[Debug]", "recording_duration:", recording_duration)
            print(qvrDateTime.formatted_timestamp(), "[Debug]", "new_recording_duration:", new_recording_duration)
            if new_recording_duration < 60:  # ffmpeg doesn't start properly if recording duration is < 6
                print(qvrDateTime.formatted_timestamp(), "[Info]",
                      "new_recording_duration < 60, not starting recording anymore:", new_recording_duration)
                break  # Exit the loop
            try:
                command = "ffmpeg" \
                          + " -i " + server_url + "/" \
                          + user + "/" \
                          + password + "/" \
                          + channel + " -t " \
                          + str(new_recording_duration) \
                          + " -c:v copy -c:a copy " \
                          + recording_name + str(qvrDateTime.unix_time_stamp()) + ".mkv"
                print(qvrDateTime.formatted_timestamp(), "[Debug]", "command: ", command)
                process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                           text=True)
                print(qvrDateTime.formatted_timestamp(), "[Info]", "ffmpeg has started")
                process.wait()

                if recording_duration >= 0:
                    print(qvrDateTime.formatted_timestamp(), "[Error]", "ffmpeg died, restarting...")
                else:
                    print(qvrDateTime.formatted_timestamp(), "[Info]", "ffmpeg completed successfully")

            except subprocess.CalledProcessError:
                print(qvrDateTime.formatted_timestamp(), "[Error]",
                      "ffmpeg has ended unexpectedly with a non-zero return code.")
            except Exception as e:
                print(f"An error occurred: {str(e)}")  # If any other exception is raised, handle it here

        print(qvrDateTime.formatted_timestamp(), "[Info]", "program has ended")