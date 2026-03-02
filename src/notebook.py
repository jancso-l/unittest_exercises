import datetime


class Note:

    DATE_FORMAT = '%m-%d-%Y %H:%M:%S'
    CATEGORY = 'stock market'

    def __init__(self, content):
        self.content = content
        self.creation_time = datetime.datetime.now().strftime(self.DATE_FORMAT)