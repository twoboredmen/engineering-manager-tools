from typing import Dict, List, Tuple, Union
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from os import getenv
from error import NotRealUserError
from logger import create
from hello_message import pick_hello_msg
import logging


class SlackHelper:
    def __init__(
        self,
        api_token=getenv("SLACK_BOT_TOKEN"),
        logger_instance=create("SlackHelper", logging.INFO),
    ) -> None:
        self._client = WebClient(token=api_token)
        self._logger = logger_instance

    def list_all_users(self) -> Dict:
        """
        List all users in dictionary with their name
        as the key for easy look up
        """
        api_response = self._client.users_list()
        members = api_response["members"]

        all_active_users = dict()
        for member_info in members:
            try:
                m = SlackMember(member_info)
                all_active_users[m.name] = {
                    "id": m.user_id,
                    "real_name": m.real_name,
                }
            except NotRealUserError as e:
                self._logger.debug(f"ignoring user {e}")

        return all_active_users

    def send_message(self, user_id: str, msg: str = pick_hello_msg()) -> None:
        """
        Send slack message to the user ID specified
        """
        try:
            self._client.chat_postMessage(channel=user_id, text=msg)
            self._logger.info(f"message sent to {user_id}")
        except SlackApiError as e:
            self._logger.error(
                f"fail to send message to {user_id} because {e.response}"
            )

    def get_all_conversations(self) -> Union[List, None]:
        """
        List all slack conversation
        """
        try:
            resp = self._client.conversations_list(types="im")
        except SlackApiError as e:
            self._logger.error(f"fail to get all conversation because {e.response}")
            return None

        return resp["channels"]

    def get_all_message_history(self, user_id: str) -> Union[List, None]:
        """
        Get all conversation history of the user
        """
        try:
            resp = self._client.conversations_history(channel=user_id)
        except SlackApiError as e:
            self._logger.error(f"fail to get message history because {e.response}")
            return None

        return resp["messages"]


class SlackMember:
    def __init__(self, user_info) -> None:
        self._user_id, self._name, self._real_name = self.__parse_member(user_info)
        self._info = {
            "id": self._user_id,
            "name": self._name,
            "real_name": self._real_name,
        }

    @property
    def user_id(self) -> str:
        return self._user_id

    @property
    def name(self) -> str:
        return self._name

    @property
    def real_name(self) -> str:
        return self._real_name

    @property
    def info_dump(self) -> Dict:
        return self._info

    def __parse_member(self, member: Dict) -> Tuple:
        if member["deleted"] or member["is_bot"]:
            raise NotRealUserError(member["name"])

        return member["id"], member["name"], member["real_name"]
