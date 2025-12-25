from typing import Optional
from .base_response_model import BaseResponseModel
from ..astrology_models import BirthDataModel

class BirthDetailsResponseModel(BaseResponseModel):
    # `data` inherited from BaseResponseModel; specialize its type for IDEs/docs
    data: Optional[BirthDataModel] = None
