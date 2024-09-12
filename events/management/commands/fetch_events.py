from django.core.management.base import BaseCommand
from events.scrapers import fetch_eventbrite_events, fetch_meetup_events, fetch_ticketmaster_events


class Command(BaseCommand):
    help = 'Fetch events from external APIs'

    def handle(self, *args, **kwargs):
        fetch_eventbrite_events()
        fetch_meetup_events()
        fetch_ticketmaster_events()
        self.stdout.write(self.style.SUCCESS('Successfully fetched events from APIs'))