from datetime import datetime, timedelta


def older_than(hours: int, last_msg_time: float) -> bool:
    """
    Check whether the last message time is
    older than specified time (in hour)
    """
    time_since_last_msg = datetime.now() - datetime.fromtimestamp(last_msg_time)
    return time_since_last_msg < timedelta(hours=hours)
