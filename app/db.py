from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import List
from app.model import Base, Calendar
from datetime import datetime

class DBException(Exception):
    pass

class CalendarDB:
    def __init__(self):
        self.engine = create_engine('sqlite:///calendar.db')
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def create(self, calendar: Calendar) -> str:
        try:
            session = self.Session()
            session.add(calendar)
            session.commit()
            calendar_id = str(calendar.id)
            session.close()
            return calendar_id
        except Exception as ex:
            raise DBException(f"failed CREATE operation with: {ex}")

    def list(self) -> List[Calendar]:
        try:
            session = self.Session()
            calendars = session.query(Calendar).all()
            session.close()
            return calendars
        except Exception as ex:
            raise DBException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> Calendar:
        try:
            session = self.Session()
            calendar = session.query(Calendar).filter(Calendar.id == int(_id)).first()
            if calendar is None:
                raise DBException(f"Calendar with id {_id} not found")
            session.close()
            return calendar
        except Exception as ex:
            raise DBException(f"failed READ operation with: {ex}")

    def update(self, _id: str, calendar: Calendar):
        try:
            session = self.Session()
            existing_calendar = session.query(Calendar).filter(Calendar.id == int(_id)).first()
            if existing_calendar is None:
                raise DBException(f"Calendar with id {_id} not found")
            existing_calendar.date = calendar.date
            existing_calendar.title = calendar.title
            existing_calendar.text = calendar.text
            session.commit()
            session.close()
        except Exception as ex:
            raise DBException(f"failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            session = self.Session()
            calendar = session.query(Calendar).filter(Calendar.id == int(_id)).first()
            if calendar is None:
                raise DBException(f"Calendar with id {_id} not found")
            session.delete(calendar)
            session.commit()
            session.close()
        except Exception as ex:
            raise DBException(f"failed DELETE operation with: {ex}")
    def clear(self):
        try:
            session = self.Session()
            session.query(Calendar).delete()  # {{ edit_1 }}
            session.commit()
            session.close()
        except Exception as ex:
            raise DBException(f"failed CLEAR operation with: {ex}")