from datetime import datetime, timezone

from sqlalchemy import (
    Boolean,
    CheckConstraint,
    Column,
    DateTime,
    Integer,
)

from app.core.constants import (
    DEFAULT_INVESTED_AMOUNT,
    GT_FULL_AMOUNT
)
from app.core.db import Base


class InvestmentBase(Base):

    __abstract__ = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'invested_amount' not in kwargs:
            self.invested_amount = DEFAULT_INVESTED_AMOUNT

    full_amount = Column(
        Integer,
        nullable=False
    )
    invested_amount = Column(
        Integer,
    )
    fully_invested = Column(
        Boolean,
        nullable=False,
        default=False,
        server_default='false'
    )
    create_date = Column(
        DateTime,
        nullable=False,
        default=lambda: datetime.now(timezone.utc)
    )
    close_date = Column(
        DateTime,
    )

    __table_args__ = (
        CheckConstraint(
            f'full_amount > {GT_FULL_AMOUNT}',
            name='positive_full_amount'
        ),
        CheckConstraint(
            f'full_amount >= invested_amount >= {DEFAULT_INVESTED_AMOUNT}',
            name='positive_invested'
        ),
    )

    def __repr__(self):
        return (
            f'{self.full_amount=} {self.invested_amount=} '
            f'{self.create_date=} {self.close_date=}'
        )
