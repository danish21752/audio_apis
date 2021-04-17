import uuid
from enum import Enum


class CommonService:
    @classmethod
    def generate_id(cls):
        return uuid.uuid4()


class ChoiceEnum(Enum):
    @classmethod
    def choices(cls):
        return tuple((x.value, x.name) for x in cls)


class AudioType(ChoiceEnum):
    SONG = 0
    PODCAST = 1
    AUDIOBOOK = 2
