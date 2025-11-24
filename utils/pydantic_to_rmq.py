from typing import Type

from pydantic import BaseModel

from rmq.items.rmq_item import RMQItem


def pydantic_to_rmq(item: BaseModel, rmq_item_cls: Type[RMQItem] = RMQItem) -> RMQItem:
    """Convert a Pydantic BaseModel instance to an RMQItem.

    Only fields declared on the RMQItem are copied to avoid typos and unexpected keys.
    """
    rmq_item = rmq_item_cls()
    data = item.dict()
    declared_fields = set(rmq_item.fields.keys())
    for k, v in data.items():
        if k in declared_fields:
            rmq_item[k] = v
    return rmq_item
