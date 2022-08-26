import datetime
import timeit
from commNetMathCalculation import commNetMathCalculation
from commNetMathInput import commNetMathInput, commNetMathInput_noTargetOrbit

objMassKG = 6.4169e23
objRadiusM = 3396200
finalOrbitHeightM = 1506600 + objRadiusM
numberOfSatellites = 6

#input = commNetMathInput_noTargetOrbit(objMassKG, objRadiusM, numberOfSatellites)
input = commNetMathInput(objMassKG, objRadiusM, finalOrbitHeightM, numberOfSatellites)
if len(input.messages):
    print(*input.messages, sep = "\n")

print("\nCalculating Results...")
start = timeit.default_timer()
output = commNetMathCalculation.computeResult(input)
end = timeit.default_timer()
print("Finished Calculation, took "+str(1000*(end-start))+"ms\n")

print("Results:")
print("Initial orbit should have perigee(low point) of "+str(output.initialOrbitPerigeeMeter)+"m")
print("Final orbit height should be "+str(output.finalOrbitMeter)+"m")
print("Delta V (changes in velocity in meters per second) needed: "+str(output.deltaVelocityMeterPerSecond)+"m/s")
print("Initial orbital period is "+str(output.initialTimeSecond)+"s, equals to "+str(datetime.timedelta(seconds=round(output.initialTimeSecond))))
print("Target orbital period is "+str(output.finalTimeSecond)+"s, equals to "+str(datetime.timedelta(seconds=round(output.finalTimeSecond))))
print("Launch station needs to orbit "+str(output.orbitCountPerSatellite)+" time(s) for every satellite released")
if len(output.messages):
    print('\n')
    print(*output.messages, sep='\n')