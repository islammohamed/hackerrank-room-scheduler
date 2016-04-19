from datetime import time, timedelta

class Meeting:
    scheduled = False
    def __init__(self, title, duration):
        self.title = title
        self.duration = duration

    def set_scheduled(already_scheduled):
        self.scheduled = True


class MeetingRoom:
    meetings = []
    schedule   = []
    time_range = [time(9, 0, 0), time(17, 0, 0)]
    break_time = [time(12, 0, 0), time(13, 0, 0)]
    last_schedule = time_range[0]

    def __init__(self, title):
        self.title = title

    def add_meeting(self, meeting):
        #if not self._meeting_is_suitable(meeting):
        #    return False

        #print self.last_schedule + timedelta(minutes = meeting_duration)
        meeting.set_scheduled = True
        self.meetings.append(meeting)
        return True

    def _meeting_is_suitable(self, meeting):
        meeting_duration = meeting.duration
        #if not self._is_break and self._is_enough_duration(meeting_duration):


    def _is_break(self, meetingDuration):
        return False

    def _is_enough_duration(self, meetingDuration):
        """Return true if x is in the range [start, end]"""
        if self.time_range[0] <= self.time_range[1]:
            return True
        else:
            return False
