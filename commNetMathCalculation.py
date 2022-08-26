from math import pi, sqrt
from commNetMathInput import commNetMathInput
from commNetMathOutput import commNetMathOutput

GRAVITATIONAL_CONSTANT = 6.67408e-11 # Newton's gravitational constant

## thanks to https://www.youtube.com/watch?v=3Qb_gcJyGQI 
class commNetMathCalculation:
    def computeResult(input: commNetMathInput, orbitingCount:int|None=None) -> commNetMathOutput:
        if not orbitingCount:
            orbitingCount = 1   # default one orbit per satellite

        stdGravParamM = GRAVITATIONAL_CONSTANT * input.bodyMassKilogram # m^3/s^2
        stdGravParamKM = stdGravParamM / (1000 ** 3)    # km^3/s^2

        #finalOrbitRadiusKM = (input.targetOrbitHeightMeter + input.bodyRadiusMeter) / 1000
        finalOrbitRadiusKM = input.targetOrbitHeightMeter / 1000
        finalOrbitalPeriod = 2 * pi * sqrt(finalOrbitRadiusKM**3 / stdGravParamKM)  # seconds
        initialOrbitalPeriod = (input.numberOfSatellites-1)/input.numberOfSatellites * finalOrbitalPeriod   # seconds

        # a_i is the semi major axis of the initial orbit, half way point between perigee and apogee
        a_i = ((stdGravParamKM * initialOrbitalPeriod**2) / (4 * pi * pi)) ** (1./3.)
        initialOrbitPerigee = (2*a_i - finalOrbitRadiusKM) * 1000   # meters
        initialOrbitPerigeeHeightM = initialOrbitPerigee - input.bodyRadiusMeter
        if(initialOrbitPerigeeHeightM<=0):
            # happens when initial orbit goes inside the celestial body
            # enlarge init orbit's period by 2x. orbit twice as much before releasing next satellite.
            # if still not enough, recurse till a good orbit is found
            input.numberOfSatellites *= 2
            return commNetMathCalculation.computeResult(input, orbitingCount=orbitingCount*2)

        velocityFinal = sqrt(stdGravParamKM / finalOrbitRadiusKM)   # km/s
        velocityInitial = sqrt((2/finalOrbitRadiusKM - 1/a_i) * stdGravParamKM) # km/s
        deltaVelocityMeterPerSecond = (velocityFinal - velocityInitial) * 1000  # m/s

        return commNetMathOutput(initialOrbitPerigee, input.targetOrbitHeightMeter, deltaVelocityMeterPerSecond, initialOrbitalPeriod, finalOrbitalPeriod, orbitingCount)