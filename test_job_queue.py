import qvrJobQueue

job_queue = qvrJobQueue.JobQueue()
first_job = {
    "uuid": "886313e1-3b8a-5372-9b90-0c9aee199e5d",
    "job_name": "test_job",
    "start_time": "2023-10-07 01:50 PM EDT",
    "end_time": "2023-10-07 04:10 PM EDT",
    "command": "ffmpeg -i ....."
}
job_queue.add_job(first_job)
job_queue.list_jobs()