import datetime
import timeit
from commNetMathCalculation import commNetMathCalculation
from commNetMathInput import commNetMathInput

objMassKG = 5.2915158e22
objRadiusM = 600000
finalOrbitHeightM = 82155000
numberOfSatellites = 3

input = commNetMathInput(objMassKG, objRadiusM, finalOrbitHeightM, numberOfSatellites)
if len(input.messages):
    print(*input.messages, sep = "\n")

print("\nCalculating Results...")
start = timeit.default_timer()
output = commNetMathCalculation.computeResult(input)
end = timeit.default_timer()
print("Finished Calculation, took "+str(1000*(end-start))+"ms\n")

print("Results:")
print("Initial orbit should have perigee(low point) of "+str(output.initialOrbitPerigeeMeter), "m")
print("Delta V (changes in velocity in meters per second) needed: "+str(output.deltaVelocityMeterPerSecond), "m/s")
print("Initial time in seconds is "+str(output.initialTimeSecond)+"s, equals to "+str(datetime.timedelta(seconds=round(output.initialTimeSecond))))
print("Final time in seconds is "+str(output.finalTimeSecond)+"s, equals to "+str(datetime.timedelta(seconds=round(output.finalTimeSecond))))
if len(output.messages):
    print(*output.messages, sep='\n')