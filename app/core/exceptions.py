from fastapi import HTTPException, status
from app.core.error_messages import UNIQUE_FIELD_IS_OCCUPIED


class UniqueFieldOccupiedExcedption(HTTPException):
    def __init__(
        self,
        model_name: str,
        field,
        field_data
    ):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                UNIQUE_FIELD_IS_OCCUPIED.format(
                    model_name=model_name,
                    field=field,
                    field_data=field_data
                )
            )
        )
