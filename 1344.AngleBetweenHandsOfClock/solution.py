class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        # Angle made by minute's hand w.r.t 00:00
        minuteAngle = minutes*6
        # Angle made by hour's hand w.r.t 00:00
        hourAngle = (hour%12)*30 + (minutes/60)*30
        # Angle between hour's and minute's hand
        angle = abs(hourAngle-minuteAngle)
        # Minimum angle between them.
        return min(angle, 360-angle)
        
