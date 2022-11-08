from src.domain.models.user.user_repository_interface import IUserRepository
from src.domain.models.circle.circle import Circle
from src.domain.models.user.user import User
from src.domain.models.user.user_type import UserType


class CircleFullSpecification:
    def __init__(self, user_repository: IUserRepository) -> None:
        self._user_repository = user_repository

    def is_satisfied_by(self, circle: Circle) -> bool:
        member_count = circle.count_members()
        if member_count < 30:
            return False
        users = self._user_repository.find_by_ids(user_ids=circle.members)
        premium_member_count = self.count_premium_member(members=users)
        max_threshold = 50 if premium_member_count > 10 else 30
        return member_count >= max_threshold

    def count_premium_member(self, members: list[User]) -> int:
        return len([m for m in members if m.type is UserType.PREMIUM])
