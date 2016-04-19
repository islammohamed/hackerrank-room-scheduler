# How to use the room scheduler.

You can execute the Scheduler using the following command
```python
python scheduler.py
```

### meeting input
The application loads the data using the configuration parameter defined in 

```python
scheduleConfig.py
from meeting import MeetingRoom
'''
config file to read meeting data from.
'''
meeting_input_file = 'input/meetings.txt'

'''
Meeting Rooms definations 
'''

MeetingRoomList = [MeetingRoom("Room 1"), MeetingRoom("Room 2")]

```

Presentation of the input provided to the appliction
```
All Hands meeting 60min
Marketing presentation 30min
Product team sync 30min
Ruby vs Go presentation 45min
....
```

### In the format of 
```
{title_with_space_allowed} {duration_in_minutes}min
```

you can change the logic of reading the files and validating the format by extending the method validate 
```python

meeting_re = re.compile(r"([\s\w]*) (\d*)min")
def validate(self, meeting_entry):
        return self.meeting_re.match(meeting_entry)
```

and pass the subset class as a different MeetingReader to MeetingFactory instance in the Scheduler.py file in the main function 

```python

def main():
    meetingsReader = MeetingReader(meeting_input_file)
    meetingsCollection = MeetingFactory(meetingsReader).get_meetings()

    room_scheduler = RoomScheduler()
    room_scheduler.schedule(meetingsCollection, [MeetingRoom("Room 1"), MeetingRoom("Room 2")])
    output(room_scheduler.get_schedule())
```

## changing the room list 
you can change the room list from the configuration file  by adding new instances of MeetingRoom class


```python
scheduleConfig.py
from meeting import MeetingRoom
'''
config file to read meeting data from.
'''
meeting_input_file = 'input/meetings.txt'

'''
Meeting Rooms definations 
'''

MeetingRoomList = [MeetingRoom("Room 1"), MeetingRoom("Room 2")]

```
