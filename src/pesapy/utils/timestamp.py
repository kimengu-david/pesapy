from datetime import datetime


def get_timestamp() -> str:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    return timestamp
