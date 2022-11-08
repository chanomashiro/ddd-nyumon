import abc

from src.domain.models.circle.circle import Circle
from src.domain.models.circle.circle_id import CircleId
from src.domain.models.circle.circle_name import CircleName


class ICircleRepositry(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def find_by_id(self, id: CircleId) -> Circle | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_by_name(self, name: CircleName) -> Circle | None:
        raise NotImplementedError()

    @abc.abstractmethod
    def find_all(self) -> list[Circle]:
        raise NotImplementedError()

    @abc.abstractmethod
    def save(self, circle: Circle):
        raise NotImplementedError()

    @abc.abstractmethod
    def delete(self, circle: Circle):
        raise NotImplementedError()
