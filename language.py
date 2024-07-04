# Language -COMPOSITION- zh-TW, en-US
from abc import ABC, abstractmethod


class Language(ABC):
    msg_key: str

    @abstractmethod
    def get_msg(self, msg_key: str) -> str:
        pass
