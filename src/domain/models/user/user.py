from src.domain.models.user.user_id import UserId
from src.domain.models.user.user_name import UserName
from src.domain.models.user.user_type import UserType


class User:
    def __init__(
        self, user_id: UserId, user_name: UserName, user_type: UserType
    ) -> None:
        self._id = user_id
        self._name = user_name
        self._type = user_type

    @property
    def id(self) -> UserId:
        return self._id

    @property
    def name(self) -> UserName:
        return self._name

    @property
    def type(self) -> UserType:
        return self._type

    def is_premium(self) -> bool:
        return self.type is UserType.PREMIUM

    def change_name(self, name: UserName):
        self._name = name

    def upgrade(self):
        self._type = UserType.PREMIUM

    def downgrade(self):
        self._type = UserType.NORMAL
