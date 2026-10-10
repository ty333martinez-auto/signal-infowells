"""Status labels — kept strictly distinct."""

from enum import Enum


class Status(str, Enum):
    CONFIRMED = "CONFIRMED"
    NOT_YET_VERIFIED = "NOT-YET-VERIFIED"
    NOT_RUN = "NOT-RUN"

    def __str__(self) -> str:
        return self.value
