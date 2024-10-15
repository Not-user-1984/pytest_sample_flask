import app.model as model
import app.db as db
from typing import List

TITLE_LIMIT = 30
TEXT_LIMIT = 200


class LogicException(Exception):
    pass


class CalendarLogic:
    def __init__(self):
        self._calendar_db = db.CalendarDB()

    @staticmethod
    def _validate_calendar(calendar: model.Calendar):
        pass


    def create(self, calendar: model.Calendar) -> str:
        self._validate_calendar(calendar)
        try:
            return self._calendar_db.create(calendar)
        except LogicException as ex:
            raise LogicException(f"Failed CREATE operation with: {ex}")

    def list(self) -> List[model.Calendar]:
        try:
            return self._calendar_db.list()
        except Exception as ex:
            raise LogicException(f"failed LIST operation with: {ex}")

    def read(self, _id: str) -> model.Calendar:
        try:
            return self._calendar_db.read(_id)
        except Exception as ex:
            raise LogicException(f"failed READ operation with: {ex}")

    def update(self, _id: str, calendar: model.Calendar):
        self._validate_calendar(calendar)
        if not hasattr(calendar, "_id") and not hasattr(calendar, "id"):
            raise LogicException("Calendar object has no '_id' or 'id' attribute")
        try:
            return self._calendar_db.update(_id, calendar)
        except Exception as ex:
            raise LogicException(f"Failed UPDATE operation with: {ex}")

    def delete(self, _id: str):
        try:
            return self._calendar_db.delete(_id)
        except Exception as ex:
            raise LogicException(f"failed DELETE operation with: {ex}")
