from app.core import constants
from app.core.error_messages import (
    COLOMNS_NUMBER_EXCEEDS_SHEET_CAPACITY,
    ROWS_NUMBER_EXCEEDS_SHEET_CAPACITY
)


def validate_sheet_capacity(
    rows_to_insert: int,
    columns_to_insert: int
) -> None:
    if rows_to_insert > constants.SHEET_MAX_ROWS:
        raise ValueError(
            ROWS_NUMBER_EXCEEDS_SHEET_CAPACITY.format(
                rows_capacity=constants.SHEET_MAX_ROWS,
                rows=rows_to_insert
            )
        )
    if columns_to_insert > constants.SHEET_MAX_COLUMNS:
        raise ValueError(
            COLOMNS_NUMBER_EXCEEDS_SHEET_CAPACITY.format(
                colomns_capacity=constants.SHEET_MAX_COLUMNS,
                colomns=columns_to_insert
            )
        )
