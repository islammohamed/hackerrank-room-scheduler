from meetingReader import *
from meetingFactory import *
from roomScheduler import RoomScheduler
from scheduleConfig import meeting_input_file, MeetingRoomList

def main():
    meetingsReader = MeetingReader(meeting_input_file)
    meetingsCollection = MeetingFactory(meetingsReader).get_meetings()

    room_scheduler = RoomScheduler()
    room_scheduler.schedule(meetingsCollection, MeetingRoomList)
    output(room_scheduler.get_schedule())

def output(rooms):
    for room in rooms:
        for meeting in room.meetings :
            print '{0} in room {1}'.format(meeting.title, room.title)

if __name__ == "__main__":
    main()
