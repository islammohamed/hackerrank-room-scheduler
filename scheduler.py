from meetingReader import *
from meetingFactory import *
from scheduler impoty RoomScheduler

if __name__ == "__main__":
    meeting_input_file = 'input/meetings.txt'
    meetingsReader = MeetingReader(meeting_input_file)
    meetingsCollection = MeetingFactory(meetingsReader).getMeetings()

    RoomScheduler(meetingsCollection).schedule()
