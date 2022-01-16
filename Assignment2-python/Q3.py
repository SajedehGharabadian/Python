
time = int(input("enter time : "))

hour = time // 3600
reminder_hour = time % 3600
minutes = reminder_hour // 60
seconds =reminder_hour  % 60

print(hour , ":" , minutes , ":" , seconds)
