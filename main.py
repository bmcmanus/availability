from calendaradapter.calendar import Calendar
import os

if __name__ == "__main__":
    url = os.getenv('EXCHANGE_URL')
    username = os.getenv('EXCHANGE_USERNAME')
    password = os.getenv('EXCHANGE_PASSWORD')
    calendar = Calendar(url=url, username=username, password=password)
    for event in calendar.events:
        print ("{start} {stop} - {subject}".format(start=event.start, stop=event.end, subject=event.subject))

