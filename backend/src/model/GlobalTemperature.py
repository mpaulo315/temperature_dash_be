from sqlalchemy import Column, Float, Date, ForeignKey, func
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadate = Base.metadate

class GlobalTemperature(Base):
    __tablename__ = "global_temperature"

    land_avg_temperature = Column(Float)
    land_avg_temperature_uncertainty = Column(Float)
    land_max_temperature = Column(Float)
    land_max_temperature_uncertainty = Column(Float)
    land_min_temperature = Column(Float)
    land_min_temperature_uncertainty = Column(Float)
    land_ocean_avg_temperature = Column(Float)
    land_ocean_avg_temperature_uncertainty = Column(Float)
    date = Column(Date, ForeignKey('date.date'))

    def __repr__(self):
        formatter = lambda x, y, z: f"{x}: {y} {f"{z} " if z else ""} ºC\n"
        return f"{self.date}:" + \
        formatter("Land avg. temperature", self.land_avg_temperature, self.land_avg_temperature_uncertainty) + \
        formatter("Land min. temperature", self.land_min_temperature, self.land_min_temperature_uncertainty) + \
        formatter("Land max. temperature", self.land_max_temperature, self.land_max_temperature_uncertainty) + \
        formatter("Land and ocean avg. temperature", self.land_and_ocean_avg_temperature, self.land_and_ocean_avg_temperature_uncertainty)