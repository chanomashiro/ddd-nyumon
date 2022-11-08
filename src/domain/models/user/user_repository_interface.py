import abc

from src.domain.models.user.user import User
from src.domain.models.user.user_id import UserId
from src.domain.models.user.user_name import UserName


class IUserRepository(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, user_id: UserId) -> User | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_name(self, user_name: UserName) -> User | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_ids(self, user_ids: list[UserId]) -> list[User]:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> list[User]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, user: User) -> None:
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, user: User) -> None:
        raise NotImplementedError()
