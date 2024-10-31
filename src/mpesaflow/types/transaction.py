# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Transaction"]


class Transaction(BaseModel):
    id: str

    account_reference: str = FieldInfo(alias="accountReference")

    amount: float

    phone_number: str = FieldInfo(alias="phoneNumber")

    transaction_desc: str = FieldInfo(alias="transactionDesc")

    transaction_id: str = FieldInfo(alias="transactionId")

    date_created: Optional[datetime] = None

    result_desc: Optional[str] = FieldInfo(alias="resultDesc", default=None)

    status: Optional[Literal["pending", "completed", "failed"]] = None
