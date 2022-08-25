from math import pi, sqrt

from commNetMathOutput import commNetMathOutput


GRAVITATIONAL_CONSTANT = 6.67408e-11 # Newton's gravitational constant

class commNetMathCalculation:
    def computeResult(input):
        stdGravParamM = GRAVITATIONAL_CONSTANT * input.bodyMassKilogram
        stdGravParamKM = stdGravParamM / (1000 ** 3)

        finalOrbitRadiusKM = (input.targetOrbitHeightMeter + input.bodyRadiusMeter) / 1000
        timeFinal = 2 * pi * sqrt(finalOrbitRadiusKM**3 / stdGravParamKM)
        timeInitial = (input.numberOfSatellites-1)/input.numberOfSatellites * timeFinal

        a_i = ((stdGravParamKM * timeInitial**2) / (4 * pi * pi)) ** (1./3.)
        initialOrbitPerigee = (2*a_i - finalOrbitRadiusKM) * 1000
        initialOrbitPerigeeHeightM = initialOrbitPerigee - input.bodyRadiusMeter

        velocityFinal = sqrt(stdGravParamKM / finalOrbitRadiusKM)
        velocityInitial = sqrt((2/finalOrbitRadiusKM - 1/a_i) * stdGravParamKM)
        deltaVelocityMeterPerSecond = (velocityFinal - velocityInitial) * 1000

        return commNetMathOutput(initialOrbitPerigeeHeightM, deltaVelocityMeterPerSecond, timeInitial, timeFinal)