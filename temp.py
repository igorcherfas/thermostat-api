from datetime import datetime

def get_timestamp():
    return datetime.now().strftime(("%Y-%m-%d %H:%M:%S"))

ROOMS = {
        "Living Room": {
            "temp": 60,
            "set_point": 72,
            "timestamp": get_timestamp()
            }
        }

def read():
    return [ROOMS[key] for key in sorted(ROOMS.keys())]

