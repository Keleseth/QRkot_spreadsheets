from datetime import datetime, timezone

from app.models.base import InvestmentBase


def distribute_donation(
    new_object: InvestmentBase,
    available_targets: list[InvestmentBase],
) -> list[InvestmentBase]:
    """
    Функция распределния неизрасходованных донатов по проектам, которые еще
    не полностью проинвестированы.
    Функция принимает:
    Список с объектами с fully_invested=False в параметр available_targets.
    Новый объект с fully_invested=False в параметр new_object.
    Циклом распределяет свободную сумму донатов в проекты.
    """
    changed = []
    for target in available_targets:
        if new_object.fully_invested:
            break
        contribution = min(
            new_object.full_amount - new_object.invested_amount,
            target.full_amount - target.invested_amount
        )
        for obj in (new_object, target):
            obj.invested_amount += contribution
            if obj.full_amount == obj.invested_amount:
                obj.fully_invested = True
                obj.close_date = datetime.now(timezone.utc)
        changed.append(target)
    return changed
