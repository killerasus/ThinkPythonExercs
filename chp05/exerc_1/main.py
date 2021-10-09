import time

currentTime = time.time()
days = currentTime // (60*60*24)
hoursInEpoch = currentTime % (60*60*24)
minutesInEpoch = currentTime % (60*60)
secondsInEpoch = currentTime % (60)

print("Days since epoch:", int(days))
print("Current time: " + str(int(hoursInEpoch//(3600))) + ":" + str(int(minutesInEpoch//60)) + ":" + str(int(secondsInEpoch)))