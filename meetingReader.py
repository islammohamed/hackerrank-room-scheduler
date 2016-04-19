import re
import meeting

class MeetingReader:
    meeting_re = re.compile(r"([\s\w]*) (\d*)min")

    def __init__(self, input_file):
        self.file = input_file
        self.meeting_entries = []

    def _read(self):
        with open(self.file, 'r') as meeting_input:
            for line in meeting_input.readlines():
                self.meeting_entries.append(line)
        meeting_input.close

    def validate(self, meeting_entry):
        return self.meeting_re.match(meeting_entry)

    def getLines(self):
        self._read()
        for meeting_title in self.meeting_entries:
            input_re = self.validate(meeting_title)
            if input_re:
                yield input_re.groups()
