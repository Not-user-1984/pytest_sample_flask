import app.logic as logic
import app.model as model
from flask import Flask
from flask import request
from app.model import Calendar

app = Flask(__name__)

_calendar_logic = logic.CalendarLogic()


class ApiException(Exception):
    pass


def _from_raw(raw_calendar: str) -> Calendar:
    parts = raw_calendar.split('|')
    if len(parts) == 3:
        return Calendar(date=parts[0], title=parts[1], text=parts[2])
    elif len(parts) == 4:
        return Calendar(id=int(parts[0]), date=parts[1], title=parts[2], text=parts[3])
    else:
        raise ApiException(f"Invalid RAW calendar data {raw_calendar}")


def _to_raw(calendar: model.Calendar) -> str:
    if calendar.id is None:
        return f"{calendar.date}|{calendar.title}|{calendar.text}"
    else:
        return f"{calendar.id}|{calendar.date}|{calendar.title}|{calendar.text}"


API_ROOT = "/api/v1"

CALENDAR_API_ROOT = API_ROOT + "/calendar"


@app.route(CALENDAR_API_ROOT + "/", methods=["POST"])
def create():
    pass



@app.route(CALENDAR_API_ROOT + "/", methods=["GET"])
def list():
    pass

@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["GET"])
def read(_id: str):
    pass

@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["PUT"])
def update(_id: str):
    pass



@app.route(CALENDAR_API_ROOT + "/<_id>/", methods=["DELETE"])
def delete(_id: str):
    pass
