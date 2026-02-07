from pydantic import BaseModel, Field, EmailStr, field_validator
from typing import Optional


class Poster(BaseModel):
    """用户注册数据模式"""

    title: str = Field(..., min_length=3, max_length=15, description="标题")
    content: str = Field(..., description="内容")
    status: int = Field(..., description="状态")


class ListUserQuery(BaseModel):
    """用户注册数据模式"""

    page: int = Field(..., description="当前页数")
    page_size: int = Field(..., description="每页数量")
