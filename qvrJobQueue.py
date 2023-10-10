from enum import Enum


class State(Enum):
    WAITING = 1
    RUNNING = 2
    FINISHED = 3


class Job:
    # job
    # job_id; job_name; start_time; end_time; command
    # uuid  ; string  ; datetime  ; datetime; string
    # "886313e1-3b8a-5372-9b90-0c9aee199e5d"; "2023-10-07 01:50 PM EDT"; "2023-10-07 04:10 PM EDT"; "ffmpeg -i ....."
    def __init__(self, uuid, job_name, start_time, end_time, command):
        self.uuid = uuid
        self.state = State.WAITING
        self.job_name = job_name
        self.start_time = start_time
        self.end_time = end_time
        self.command = command


class JobQueue:
    def __init__(self):
        self.jobs = []

    def add_job(self, job):
        self.jobs.append(job)

    def del_job(self):
        pass

    def get_jobs(self):
        pass

    def list_jobs(self):
        for job in self.jobs:
            print(job.uuid, job.state, job.job_name, job.start_time, job.end_time, job.command)


job_queue = JobQueue()
job = Job("886313e1-3b8a-5372-9b90-0c9aee199e5d", "first_job", "2023-10-07 01:50 PM EDT", "2023-10-07 04:10 PM EDT",
          "ffmpeg -i .....")
job_queue.add_job(job)
job_queue.list_jobs()
