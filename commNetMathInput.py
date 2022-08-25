from math import pi, radians, sin


class commNetMathInput:
    bodyMassKilogram = -1
    bodyRadiusMeter = -1
    targetOrbitHeightMeter = -1
    numberOfSatellites = -1
    messages = []

    def __init__(self, mass, radius, orbitHeight, numSat):
        self.bodyMassKilogram = mass if mass>0 else 1
        self.bodyRadiusMeter = radius if radius>0 else 1
        self.targetOrbitHeightMeter = orbitHeight if orbitHeight>self.bodyRadiusMeter else self.bodyRadiusMeter*1.1
        self.numberOfSatellites = numSat if numSat>=3 else 3

        if mass<=0:     # only positive mass allowed
            self.messages.append("Target celestial body mass has to be non-zero positive. Defaulted to 1kg")
        if radius<=0:   # must have positive radius
            self.messages.append("Target celestial body radius has to be non-zero positive. Defaulted to 1m")
        if orbitHeight<=self.bodyRadiusMeter:   # orbit must be bigger than the celestial body
            self.messages.append("Target CommNet orbit can't be smaller than its parent object. Defaulted to parent radius + 1m")
        if numSat<3:    # at least 3 satellites needed for full coverage
            self.messages.append("At least 3 satellites needed for full network coverage. Defaulted to 3 satellites")

class commNetMathInput_noTargetOrbit(commNetMathInput):
    def __init__(self, mass, radius, numSat):
        n = numSat if numSat>=3 else 3
        r = radius if radius>0 else 1
        radiansBetweenSatellites = (n-2) * pi / n
        minOrbitHeight = r / sin(radiansBetweenSatellites/2)
        super().__init__(mass, radius, minOrbitHeight, numSat)