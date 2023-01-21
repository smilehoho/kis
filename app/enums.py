from enum import Enum


class AccessKeyStatusEnum(str, Enum):
    active = "active"
    expired = "expired"
