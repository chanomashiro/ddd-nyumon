from src.domain.models.circle.circle_id import CircleId
from src.domain.models.circle.circle_name import CircleName
from src.domain.models.circle.circle_full_specification import CircleFullSpecification
from src.domain.models.circle.circle_full_exception import CircleFullException
from src.domain.models.user.user_id import UserId
from src.domain.models.user.user import User


class Circle:
    def __init__(self, id: CircleId, name: CircleName, owner: UserId, members: list[UserId]) -> None:
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

    def count_members(self) -> int:
        return len(self._members) + 1

    def join(self, member: User, fullspec: CircleFullSpecification):
        if fullspec.is_satisfied_by(circle=self):
            raise CircleFullException()
        self._members.append(member.id)

    def change_user_name(self, name: CircleName):
        self._name = name
