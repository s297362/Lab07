import datetime
from dataclasses import dataclass
@dataclass
class Situazione:
    Localita: str
    Data: datetime.datetime
    Tmedia: int
    Tmin: int
    Tmax: int
    Puntorugiada: int
    Umidita: int
    Visibilita: int
    Ventomedia: int
    Ventomax: int
    Raffica: int
    Pressioneslm: int
    Pressionemedia: int
    Pioggia: int
    Fenomeni: str