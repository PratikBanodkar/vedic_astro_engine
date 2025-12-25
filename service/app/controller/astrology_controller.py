from fastapi import APIRouter, Query, Depends, Request
from urllib.parse import unquote
from fastapi.responses import JSONResponse
from slowapi import Limiter
from slowapi.util import get_remote_address

from ..services.astrology_service import AstrologyService
from ..models.response.birth_details_response_model import BirthDetailsResponseModel
from ..services.security_service import enforce_rate_limit, validate_api_key


router = APIRouter(prefix="/astrology", tags=["astrology"])
astrology_service = AstrologyService()

@router.get("/get-birth-details", response_model=BirthDetailsResponseModel)
def get_birth_details(
    request: Request,
    api_key: str = Depends(validate_api_key),
    _: None = Depends(enforce_rate_limit),
    datetime: str = Query(..., description="ISO 8601 datetime string"),
    lat: float = Query(..., description="Latitude"),
    lon: float = Query(..., description="Longitude"),
    ayanamsa: int = Query(1, description="Ayanamsa mode")
):
    ''' Get birth chart details including nakshatra, chandra_rasi, soorya_rasi, and zodiac.
    Args:
        datetime: ISO 8601 datetime string
        lat: Latitude
        lon: Longitude
        ayanamsa: Ayanamsa mode (default: Lahiri)
    Returns:
        BirthDetailsResponseModel: Birth chart details
    '''
    try:
        decoded_dt = unquote(datetime)
    except Exception:
        decoded_dt = datetime

    result = astrology_service.get_birth_details(
        datetime_str=decoded_dt,
        lat=lat,
        lon=lon,
        ayanamsa=ayanamsa,
    )

    status_code = 200
    if getattr(result, "code", None) is not None:
        status_code = int(result.code)

    return JSONResponse(status_code=status_code, content=result.model_dump(mode='json'))