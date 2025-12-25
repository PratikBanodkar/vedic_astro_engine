from typing import Any, Optional, Type, TypeVar
from pydantic import BaseModel, Field
from datetime import datetime

T = TypeVar("T", bound="BaseResponseModel")


class BaseResponseModel(BaseModel):
    success: bool
    status: str  # "success", "error", "fail"
    code: int  # 200, 400, 500, custom codes
    data: Optional[Any] = None
    message: Optional[str] = None
    timestamp: datetime = Field(default_factory=datetime.utcnow)

    @classmethod
    def success_response(cls: Type[T], data: Any = None, message: Optional[str] = None, code: int = 200) -> T:
        """Return a success response instance of this class."""
        return cls(success=True, status="success", code=code, data=data, message=message)

    @classmethod
    def bad_request(cls: Type[T], message: Optional[str] = "Bad Request", data: Any = None) -> T:
        return cls(success=False, status="fail", code=400, data=data, message=message)

    @classmethod
    def unauthorized(cls: Type[T], message: Optional[str] = "Unauthorized", data: Any = None) -> T:
        return cls(success=False, status="fail", code=401, data=data, message=message)

    @classmethod
    def internal_server_error(cls: Type[T], message: Optional[str] = "Internal Server Error", data: Any = None) -> T:
        return cls(success=False, status="error", code=500, data=data, message=message)

    @classmethod
    def not_found(cls: Type[T], message: Optional[str] = "Not Found", data: Any = None) -> T:
        return cls(success=False, status="fail", code=404, data=data, message=message)
