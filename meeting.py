class Meeting:
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

class Room:
    meetings = []

    def __init__(self, title):
        self.title = title

    def addMeeting(self, meeting):
        self.meetings.append(meeting)
