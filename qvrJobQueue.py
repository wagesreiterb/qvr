
class JobQueue:
    def __init__(self):
        self.job_queue_waiting = []
        self.job_queue_running = []
        self.job_queue_finished = []

    def add_job(self, job):
        self.job_queue_waiting.append(job)

    def del_job(self):
        pass

    def get_jobs(self):
        pass

    def list_jobs(self):
        print("Job Queue WAITING")
        for job in self.job_queue_waiting:
            print(self.job_queue_waiting)
        print("Job Queue RUNNING")
        for job in self.job_queue_running:
            print(self.job_queue_running)
        print("Job Queue FINISHED")
        for job in self.job_queue_finished:
            print(self.job_queue_finished)

