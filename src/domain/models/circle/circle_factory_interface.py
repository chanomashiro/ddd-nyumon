import abc

from src.domain.models.circle.circle_name import CircleName
from src.domain.models.user.user import User


class ICircleFactory(metaclass=abc.ABCMeta):
    @abc.abstractclassmethod
    def create(cls, name: CircleName, owner: User):
        raise NotImplementedError()
