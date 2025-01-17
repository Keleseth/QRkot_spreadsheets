from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, Extra

from app.core.constants import (
    DEFAULT_INVESTED_AMOUNT,
    MIN_PROJECT_DESCRIPTION_LENGTH,
    MAX_PROJECT_NAME_LENGTH,
    GT_FULL_AMOUNT,
    MIN_PROJECT_NAME_LENGTH,
)


class CharityProjectBase(BaseModel):
    name: str = Field(..., max_length=MAX_PROJECT_NAME_LENGTH)
    description: str
    full_amount: int = Field(..., gt=GT_FULL_AMOUNT)

    class Config:
        min_anystr_length = 1
        extra = Extra.forbid


class CharityProjectCreate(CharityProjectBase):

    invested_amount: int = Field(
        DEFAULT_INVESTED_AMOUNT, readOnly=True
    )


class CharityProjectUpdate(BaseModel):
    name: Optional[str] = Field(
        None,
        min_length=MIN_PROJECT_NAME_LENGTH,
        max_length=MAX_PROJECT_NAME_LENGTH,
    )
    description: Optional[str] = Field(
        None, min_length=MIN_PROJECT_DESCRIPTION_LENGTH
    )
    full_amount: Optional[int] = Field(
        None, gt=GT_FULL_AMOUNT
    )

    class Config(CharityProjectBase.Config):
        pass


class CharityProjectDB(CharityProjectBase):
    id: int
    invested_amount: int
    fully_invested: bool
    create_date: datetime
    close_date: Optional[datetime] = None

    class Config:
        orm_mode = True
