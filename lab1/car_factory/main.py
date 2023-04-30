from cars.sedan import Sedan
from cars.hatchback import Hatchback
from cars.suv import SUV

from engines.gasoline import GasolineEngine
from engines.diesel import DieselEngine
from engines.electric import ElectricEngine

def main():
    gasoline_engine = GasolineEngine()
    diesel_engine = DieselEngine()
    electric_engine = ElectricEngine()

    sedan = Sedan(gasoline_engine)
    hatchback = Hatchback(diesel_engine)
    suv = SUV(electric_engine)

    sedan.start_engine()
    hatchback.start_engine()
    suv.start_engine()

if __name__ == "__main__":
    main()
