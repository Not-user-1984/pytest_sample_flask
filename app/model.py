from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Calendar(Base):
    __tablename__ = 'calendars'

    id = Column(Integer, primary_key=True)
    date = Column(String, nullable=False)
    title = Column(String, nullable=False)
    text = Column(String)

    def __init__(self, date, title, text, id=None):
        self.id = id
        self.date = date
        self.title = title
        self.text = text

    def __repr__(self):
        return f"<Calendar(id={self.id}, date='{self.date}', title='{self.title}', text='{self.text}')>"
