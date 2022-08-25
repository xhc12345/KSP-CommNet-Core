class commNetMathOutput:
    initialOrbitPerigeeMeter = -1
    deltaVelocityMeterPerSecond = -1
    initialTimeSecond = -1
    initialTimeHour = -1
    finalTimeSecond = -1
    finalTimeHour = -1
    messages = []

    def __init__(self, perigee, deltaV, initTimeSec, finalTimeSec):
        self.initialOrbitPerigeeMeter = perigee if perigee>0 else None
        self.deltaVelocityMeterPerSecond = deltaV if deltaV>0 else None
        self.initialTimeSecond = initTimeSec if initTimeSec>0 else None
        self.finalTimeSecond = finalTimeSec if finalTimeSec>0 else None

        if perigee<=0:
            self.messages.append("Perigee(lowest point of orbit) can't be less than zero")
        if deltaV<=0:
            self.messages.append("Delta V can't be negative")
        if initTimeSec<=0:
            self.messages.append("Initial time can't be negative")
        if finalTimeSec<=0:
            self.messages.append("Final time can't be negative")