from src.models.settings import base
from sqlalchemy import Column

class Events(base):
    tablename = 'events'

    id = Column(str, primary_key=True)
    title = Column(str, nullable=False)
    details = Column(str)
    slug = Column(str, nullable=False)
    maximum_attendees = Column(int)