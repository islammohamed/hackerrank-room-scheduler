class RoomScheduler:

    def schedule(self, meetings, rooms):
        for meeting in meetings:
            for room in rooms:
                if not meeting.scheduled:
                    room.add_meeting(meeting)

        self.rooms = rooms

    def get_schedule(self):
        return self.rooms
