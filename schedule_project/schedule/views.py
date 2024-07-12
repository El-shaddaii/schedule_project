from django.shortcuts import render
from .models import Event



def schedule_view(request):
    hours = list(range(24))
    events = [
        # Sample event data structure
        {'day': 'Tue', 'start_hour': 10, 'duration': 5, 'name': 'KVCC'},
        {'day': 'Wed', 'start_hour': 10, 'duration': 5, 'name': 'KVCC'},
        {'day': 'Thu', 'start_hour': 10, 'duration': 5, 'name': 'KVCC'},
        
        {'day': 'Tue', 'start_hour': 16, 'duration': 8, 'name': 'ITC'},
        {'day': 'Wed', 'start_hour': 0, 'duration': 8, 'name': ''},
        {'day': 'Wed', 'start_hour': 16, 'duration': 8, 'name': 'ITC'},
        {'day': 'Thu', 'start_hour': 0, 'duration': 8, 'name': ''},
        {'day': 'Fri', 'start_hour': 16, 'duration': 5, 'name': 'ITC'},
        {'day': 'Sat', 'start_hour': 8, 'duration': 8, 'name': 'ITC'},
        # Add more events as needed
    ]
    return render(request, 'schedule/schedule.html', {'hours': hours, 'events': events})
