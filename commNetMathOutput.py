class commNetMathOutput:
    initialOrbitPerigeeMeter = -1
    finalOrbitMeter = -1
    deltaVelocityMeterPerSecond = -1
    initialTimeSecond = -1
    finalTimeSecond = -1
    orbitCountPerSatellite = -1
    messages = []

    def __init__(self, perigee, height, deltaV, initTimeSec, finalTimeSec, orbitCount):
        self.initialOrbitPerigeeMeter = perigee if perigee>0 else None
        self.finalOrbitMeter = height if height>self.initialOrbitPerigeeMeter else None
        self.deltaVelocityMeterPerSecond = deltaV if deltaV>0 else None
        self.initialTimeSecond = initTimeSec if initTimeSec>0 else None
        self.finalTimeSecond = finalTimeSec if finalTimeSec>0 else None
        self.orbitCountPerSatellite = orbitCount

        if perigee<=0:
            self.messages.append("Perigee(lowest point of orbit) can't be less than zero")
        if height<=self.initialOrbitPerigeeMeter:
            self.messages.append("Final orbit can't be smaller than initial orbit")
        if deltaV<=0:
            self.messages.append("Delta V can't be negative")
        if initTimeSec<=0:
            self.messages.append("Initial time can't be negative")
        if finalTimeSec<=0:
            self.messages.append("Final time can't be negative")
        if orbitCount<1:
            self.messages.append("Orbiting needed per satellite calculated incorrectly")