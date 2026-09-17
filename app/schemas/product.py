from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field


class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=200)
    slug: str = Field(..., min_length=1, max_length=220)
    description: str | None = None
    price: Decimal = Field(..., ge=0)
    stock: int = Field(0, ge=0)
    image_url: str | None = None
    category_id: int
    is_active: bool = True


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    name: str | None = Field(None, min_length=1, max_length=200)
    slug: str | None = Field(None, min_length=1, max_length=220)
    description: str | None = None
    price: Decimal | None = Field(None, ge=0)
    stock: int | None = Field(None, ge=0)
    image_url: str | None = None
    category_id: int | None = None
    is_active: bool | None = None


class ProductRead(ProductBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
