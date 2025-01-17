from sqlalchemy import (
    Column,
    String,
    Text,
)

from .base import InvestmentBase
from app.core.constants import (
    MAX_PROJECT_NAME_LENGTH,
)


class CharityProject(InvestmentBase):

    name = Column(
        String(MAX_PROJECT_NAME_LENGTH),
        nullable=False,
        unique=True
    )
    description = Column(
        Text,
        nullable=False
    )

    def __repr__(self):
        return (
            f'{self.name[:20]=}: {super().__repr__()}'
        )
