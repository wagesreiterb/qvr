import qvrJobQueue
import time


class QvrScheduler:
    def __init__(self, job_queue):
        self.job_queue = job_queue
        first_job = {
            "job_name": "test_job",
            "start_time": "2023-10-07 01:50 PM EDT",
            "end_time": "2023-10-07 04:10 PM EDT",
            "channel": "2101"
        }
        self.job_queue.add_job(first_job)
        pass

    def run(self):
        while True:
            # if new job schedulable
            # schedule_new_job
            self.job_queue.add_new_job_from_file()
            self.job_queue.schedule_recording()
            print(".")
            self.job_queue.list_jobs()
            time.sleep(3)
            pass

    def run_new_job(self):
        pass