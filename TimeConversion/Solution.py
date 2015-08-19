time = input()
time = time.split(':')
hours = int(time[0])
minutes = int(time[1])
suffix = time[2]
seconds = int(time[2].rstrip("APM"))

if (suffix.endswith("AM") and hours == 12):
    hours = 0
elif (suffix.endswith("PM")):
    if (hours != 12):
        hours = (hours + 12) % 24

print("%02d:%02d:%02d" % (hours, minutes, seconds))
