from slack_helper import SlackHelper
from time_check import older_than
from logger import create
import logging

###### Parameters
# Time (in hour) since the last message
HOURS_SINCE = 72

# Put a list of slack name of the people you want to check in here here
LIST_OF_PEOPLE_TO_CHECKIN = [
    "...",
]
######


def main():
    log = create("MAIN", logging.INFO)

    # Initialise SlackHelper instance
    sh = SlackHelper(logger_instance=log)

    # Get all active Slack users
    users = sh.list_all_users()
    # Get all conversation
    all_conversations = {
        item["user"]: item["id"] for item in sh.get_all_conversations()
    }

    # Loop around to see whether the last message is older than HOURS_SINCE
    for person in LIST_OF_PEOPLE_TO_CHECKIN:
        try:
            user_id = users[person]["id"]
            conversation_id = all_conversations[user_id]
            msgs = sh.get_all_message_history(conversation_id)
            last_msg = msgs[0]

            if older_than(hours=HOURS_SINCE, last_msg_time=float(last_msg["ts"])):
                # Here is where you can do anything you wish.
                # Currently, we are just printing out. But SlackHelper
                # can also help you send message to that person directly!
                # sh.send_message(user_id=user_id)

                # Or if you feel like it is too much, you can consider extending
                # to have Slack Bot notify you instead.
                log.info(f"Time to send a message to {person}")

        except KeyError:
            log.warning(f"{person} does not exist on slack workspace")


if __name__ == "__main__":
    main()
