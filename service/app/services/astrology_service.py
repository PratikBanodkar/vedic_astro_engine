from ..models.response.birth_details_response_model import BirthDetailsResponseModel
import swisseph as swe
from datetime import datetime, timezone, timedelta
from fastapi import HTTPException
from ..static_data import RASI_DATA, PLANET_DETAILS, get_nakshatra_details
from ..models.astrology_models import (
    PlanetModel, NakshatraModel, RasiModel, ZodiacModel, 
    AdditionalInfoModel, BirthDataModel
)

class AstrologyService:
    """Service layer for astrology calculations."""

    def __init__(self, ephe_path: str = "/app/ephe"):
        swe.set_ephe_path(ephe_path)
        
        # Vimshottari Data
        self.DASHA_LORDS = [8, 6, 0, 1, 2, 7, 4, 5, 3] 
        self.DASHA_YEARS = {8: 7, 6: 20, 0: 6, 1: 10, 2: 7, 7: 18, 4: 16, 5: 19, 3: 17}
        
        # Logic Helper Data
        self.OWN_SIGNS = {
            0: [4], 1: [3], 2: [0, 7], 3: [2, 5], 4: [8, 11], 5: [1, 6], 6: [9, 10]
        }
        self.EXALTED_SIGNS = {
            0: 0, 1: 1, 2: 9, 3: 5, 4: 3, 5: 11, 6: 6
        }
        

    def get_birth_details(self, datetime_str: str, lat: float, lon: float, ayanamsa: int = 1) -> BirthDetailsResponseModel:
        """
        Calculate birth chart details from datetime and coordinates.
        
        Args:
            datetime_str: ISO 8601 datetime string
            coordinates_str: "lat,long" format
            ayanamsa: Ayanamsa mode (default: Lahiri)
        
        Returns:
            dict: Birth chart details including nakshatra, chandra_rasi, soorya_rasi, zodiac
        
        Raises:
            HTTPException: For invalid input or calculation errors
        """
        try:
            # 1. Parse & Time            
            try:
                dt_obj = datetime.fromisoformat(datetime_str.replace('Z', '+00:00'))
                dt_utc = dt_obj.astimezone(timezone.utc)
            except ValueError:
                return BirthDetailsResponseModel.bad_request(message="Invalid ISO 8601 datetime format")

            decimal_hour = dt_utc.hour + (dt_utc.minute / 60.0) + (dt_utc.second / 3600.0)
            jd = swe.julday(dt_utc.year, dt_utc.month, dt_utc.day, decimal_hour)

            # 2. Calculations
            swe.set_sid_mode(swe.SIDM_LAHIRI) # Enforce Lahiri for Vedic
            
            # Sun/Moon/Zodiac
            moon_res = swe.calc_ut(jd, swe.MOON, swe.FLG_SIDEREAL)
            sun_res_sid = swe.calc_ut(jd, swe.SUN, swe.FLG_SIDEREAL)
            sun_res_trop = swe.calc_ut(jd, swe.SUN, 0)
            
            moon_long = moon_res[0][0]
            sun_long_sid = sun_res_sid[0][0]
            sun_long_trop = sun_res_trop[0][0]

            # 3. Logic
            nk_idx = int(moon_long / 13.333333)            
            nk_data = get_nakshatra_details(nk_idx)            
            pada = int((moon_long % 13.333333) / 3.333333) + 1

            c_rasi_idx = int(moon_long / 30.0)
            s_rasi_idx = int(sun_long_sid / 30.0)
            z_rasi_idx = int(sun_long_trop / 30.0)

            # 4. Construct Models
            nakshatra_model = NakshatraModel(
                id=nk_data["id"], name=nk_data["name"], 
                lord=PlanetModel(**nk_data["lord"]) if nk_data.get("lord") else None, 
                pada=pada
            )        

            # Build additional_info carefully to avoid duplicate 'planet' values
            info_dict = {k: v for k, v in nk_data.get("info", {}).items() if k in AdditionalInfoModel.model_fields}
            # Ensure 'planet' is set only once (prefer the nakshatra lord's vedic_name)
            info_dict.pop("planet", None)
            info_dict["syllables"] = ", ".join(nk_data.get("syllables", []))
            info_dict["planet"] = nk_data.get("lord", {}).get("vedic_name") if nk_data.get("lord") else None

            birth_data = BirthDataModel(
                nakshatra=nakshatra_model,
                chandra_rasi=RasiModel(id=c_rasi_idx+1, name=RASI_DATA[c_rasi_idx]["name"], lord=PlanetModel(**PLANET_DETAILS[RASI_DATA[c_rasi_idx]["lord_id"]])),
                soorya_rasi=RasiModel(id=s_rasi_idx+1, name=RASI_DATA[s_rasi_idx]["name"], lord=PlanetModel(**PLANET_DETAILS[RASI_DATA[s_rasi_idx]["lord_id"]])),
                zodiac=ZodiacModel(id=z_rasi_idx+1, name=RASI_DATA[z_rasi_idx]["zodiac_name"]),
                additional_info=AdditionalInfoModel(**info_dict)
            )

            return BirthDetailsResponseModel.success_response(data=birth_data, message="Success")

        except Exception as e:            
            return BirthDetailsResponseModel.internal_server_error(message=str(e))