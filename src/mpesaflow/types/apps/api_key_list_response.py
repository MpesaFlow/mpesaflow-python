# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["APIKeyListResponse", "Data"]


class Data(BaseModel):
    id: str

    application_id: str = FieldInfo(alias="applicationId")

    key_name: str = FieldInfo(alias="keyName")


class APIKeyListResponse(BaseModel):
    data: Optional[List[Data]] = None
