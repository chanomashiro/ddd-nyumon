from src.domain.models.circle.circle import Circle
from src.domain.models.circle.circle_repository_interface import ICircleRepositry


class CircleService:
    def __init__(self, circle_repository: ICircleRepositry) -> None:
        self._circle_repository = circle_repository

    def exists(self, circle: Circle) -> bool:
        target = self._circle_repository.find_by_name(name=circle.name)
        return target is not None
