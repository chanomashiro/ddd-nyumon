from src.domain.models.exception import ArgumentException


class CircleName:
    def __init__(self, value: str) -> None:
        if len(value) < 3:
            raise ArgumentException("サークル名は3文字以上です。")
        if len(value) > 20:
            raise ArgumentException("サークル名は20文字以下です。")

        self._value = value

    @property
    def value(self) -> str:
        return self._value

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, CircleName):
            return NotImplemented
        return self.value == other.value
