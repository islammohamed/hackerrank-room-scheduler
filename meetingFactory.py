from meetingReader import *
from meeting import *

class MeetingFactory:

    def __init__(self, MeetingReader):
        self.meetingReader = MeetingReader

    def getMeetings(self):
        meetingsCollection = []
        for meeting in self.meetingReader.getLines():
            meetingsCollection.append(Meeting(meeting[0], meeting[1]))

        return meetingsCollection
