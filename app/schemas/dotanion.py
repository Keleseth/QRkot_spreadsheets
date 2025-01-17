from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, Extra

from app.core.constants import (
    GT_FULL_AMOUNT,
    DEFAULT_INVESTED_AMOUNT
)


class BaseDonationScheme(BaseModel):

    full_amount: int = Field(..., gt=GT_FULL_AMOUNT)
    comment: Optional[str]

    class Config:
        extra = Extra.forbid


class CreateDonationScheme(BaseDonationScheme):

    invested_amount: int = Field(
        DEFAULT_INVESTED_AMOUNT, readOnly=True
    )


class UserDonationDBScheme(BaseDonationScheme):

    id: int
    create_date: datetime

    class Config:
        orm_mode = True


class DonationDBScheme(UserDonationDBScheme):

    user_id: int
    invested_amount: int
    fully_invested: bool
    close_date: Optional[datetime]
