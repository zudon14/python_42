def ft_water_reminder():
    water_days = int(input("Days since last watering: "))
    if water_days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
