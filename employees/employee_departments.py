import datetime

class Employee:
    def __init__(self, name, job_title):
        self.name = name
        self.job_title = job_title
        self.start_date = ""

    def hire(self):
        self.start_date = datetime.datetime.now

    