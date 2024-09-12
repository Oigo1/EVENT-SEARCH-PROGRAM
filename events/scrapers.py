from django.shortcuts import render, redirect, get_object_or_404
from .models import Event
import requests

# Create your views here.

#  Eventbrite API

def fetch_eventbrite_events():
    url = 'https://www.eventbriteapi.com/v3/events/search/'
    headers = {
        'Authorization': 'Bearer OLJKZC6OHRIPATT3SCVO'
    }
    params = {
        'q': 'music',  # Search query
        'location.address': 'New York',  # Location filter
        'expand': 'venue',
    }

    response = requests.get(url, headers=headers, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        try:
            events_data = response.json().get('events', [])
            if not events_data:
                print("No events found in the response.")
                return

            for event in events_data:
                Event.objects.create(
                    title=event['name']['text'],
                    description=event['description']['text'] if event['description'] else '',
                    category='party',
                    date=event['start']['local'].split('T')[0],
                    link=event['url'],
                )
        except KeyError:
            print("Error: 'events' key not found in the response.")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response JSON:", response.json())


# Meetup API

def fetch_meetup_events():
    url = 'https://api.meetup.com/2/events'
    params = {
        'key': 'YOUR_MEETUP_API_KEY',
        'group_urlname': 'tech-events',  # Replace this with a specific group or leave blank
        'sign': 'true',  # Required for some endpoints
        'page': 20  # Number of events to fetch per request
    }

    response = requests.get(url, params=params)

    # Debug: Print the response
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    if response.status_code == 200:
        try:
            events_data = response.json()['results']  # Use 'results' for older Meetup API
            for event in events_data:
                Event.objects.create(
                    title=event['name'],
                    description=event.get('description', ''),
                    category='meetup',  # Modify based on actual category data
                    date=event['time'],  # Make sure to format date if necessary
                    link=event['event_url']
                )
        except KeyError:
            print("Error: 'results' key not found in the response.")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response JSON:", response.json())


# Ticketmaster API:

def fetch_ticketmaster_events():
    url = 'https://app.ticketmaster.com/discovery/v2/events.json'
    params = {
        'apikey': 'YOUR_TICKETMASTER_API_KEY',
        'classificationName': 'music',  # You can change this to 'sports', 'arts', etc.
        'city': 'New York',  # Specify the city if needed
        'size': 20,  # Number of events to fetch
    }

    response = requests.get(url, params=params)

    # Debug: Print the response to see the full structure
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())

    if response.status_code == 200:
        try:
            events_data = response.json()['_embedded']['events']
            for event in events_data:
                Event.objects.create(
                    title=event['name'],
                    description=event.get('info', 'No description available'),
                    category=event['classifications'][0]['segment']['name'],  # Category based on classification
                    date=event['dates']['start']['localDate'],
                    link=event['url'],
                )
        except KeyError as e:
            print(f"Error: {e} key not found in the response.")
    else:
        print(f"Error: Received status code {response.status_code}")
        print("Response JSON:", response.json())

