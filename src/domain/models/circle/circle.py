from src.domain.models.circle.circle_id import CircleId
from src.domain.models.circle.circle_name import CircleName
from src.domain.models.user.user_id import UserId


class Circle:
    def __init__(
        self, id: CircleId, name: CircleName, owner: UserId, members: list[UserId]
    ) -> None:
        self._id = id
        self._name = name
        self._owner = owner
        self._members = members

    @property
    def id(self) -> CircleId:
        return self._id

    @property
    def name(self) -> CircleName:
        return self._name

    @property
    def owner(self) -> UserId:
        return self._owner

    @property
    def members(self) -> list[UserId]:
        return self._members
