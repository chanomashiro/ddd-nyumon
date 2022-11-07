from __future__ import annotations

import abc

from src.domain.models.user.user_name import UserName


class IUserFactory(metaclass=abc.ABCMeta):
    @abc.abstractstaticmethod
    def create(name: UserName) -> IUserFactory:
        raise NotImplementedError()
