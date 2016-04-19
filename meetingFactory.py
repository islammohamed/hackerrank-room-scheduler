from meetingReader import *
from meeting import *

class MeetingFactory:

    def __init__(self, MeetingReader):
        self.meetingReader = MeetingReader

    '''
    order the meetings list by duration
    '''
    def _order_meetings(self, meetings):
        return sorted(meetings, key=lambda meeting: meeting.duration, reverse=True)

    '''
    return ordered list of meetings list
    '''
    def get_meetings(self):
        meetingsCollection = []
        for meeting in self.meetingReader.get_lines():
            meetingsCollection.append(Meeting(meeting[0], meeting[1]))

        return self._order_meetings(meetingsCollection)
