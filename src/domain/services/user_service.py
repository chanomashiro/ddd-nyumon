from src.domain.models.user.user import User
from src.domain.models.user.user_repository_interface import IUserRepository


class UserService:
    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def exists(self, user: User) -> bool:
        finded_user = self._user_repository.find_by_name(user_name=user.name)
        return finded_user is not None
