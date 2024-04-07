from src.models.repository.events_repository import EventsRepository
from src.models.settings.connection import db_connection_handler

db_connection_handler.connect_to_db

def test_insert_event():
    event = {
        'uuid': 'uuid test',
        'title': 'title test',
        'slug': 'slug test',
        'maximum_attendees': 20
    }
    
    event_repository = EventsRepository()
    event_repository.insert_event(event)
    print(event)