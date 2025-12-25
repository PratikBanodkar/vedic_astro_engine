from pydantic import BaseModel
from typing import Optional, List


class PlanetModel(BaseModel):
    id: Optional[int]
    name: Optional[str]
    vedic_name: Optional[str]


class NakshatraModel(BaseModel):
    id: int
    name: str
    lord: PlanetModel
    pada: int


class RasiModel(BaseModel):
    id: int
    name: str
    lord: PlanetModel


class ZodiacModel(BaseModel):
    id: int
    name: str


class AdditionalInfoModel(BaseModel):
    deity: Optional[str] = None
    ganam: Optional[str] = None
    symbol: Optional[str] = None
    animal_sign: Optional[str] = None
    nadi: Optional[str] = None
    color: Optional[str] = None
    best_direction: Optional[str] = None
    birth_stone: Optional[str] = None
    gender: Optional[str] = None
    enemy_yoni: Optional[str] = None
    syllables: Optional[str] = None
    planet: Optional[str] = None


class BirthDataModel(BaseModel):
    nakshatra: NakshatraModel
    chandra_rasi: RasiModel
    soorya_rasi: RasiModel
    zodiac: ZodiacModel
    additional_info: AdditionalInfoModel    
