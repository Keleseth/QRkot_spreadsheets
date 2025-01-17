from sqlalchemy import (
    Column,
    ForeignKey,
    Integer,
    Text,
)

from .base import InvestmentBase


class Donation(InvestmentBase):

    user_id = Column(
        Integer,
        ForeignKey(
            'user.id',
            ondelete='SET NULL'  # На случай прямого удаления пользователя.
        ),
        nullable=True
    )
    comment = Column(
        Text,
    )

    def __repr__(self):
        return (
            f'{self.user_id=}: '
            f'{super().__repr__()}'
        )
