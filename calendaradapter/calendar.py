from pyexchange import Exchange2010Service, ExchangeNTLMAuthConnection
from datetime import datetime, timedelta
import time
from pytz import timezone
import string

class Calendar:
    def __init__(self, url=None, username=None, password=None, tz="US/Mountain", start=None, stop=None):
        self.connection = ExchangeNTLMAuthConnection(url=url,
                                        username=username,
                                        password=password)
        self.service = Exchange2010Service(self.connection)
        if start == None:
            start = datetime.now() - timedelta(days=14)
        if stop == None:
            stop = datetime.now()
        self.events = self.service.calendar().list_events(start=timezone(tz).localize(start), end=timezone(tz).localize(stop), details=True).events
