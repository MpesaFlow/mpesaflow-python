# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["AppListResponse", "Data"]


class Data(BaseModel):
    id: str

    name: str

    description: Optional[str] = None


class AppListResponse(BaseModel):
    data: Optional[List[Data]] = None
