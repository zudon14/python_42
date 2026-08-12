
def ft_count_harvest_recursive():
    day = int(input("Days until harvest: "))
    count = 0
    ft_call_harvest_recursive(day, count)

def ft_call_harvest_recursive(day, count):
    if count < day:
        count += 1
        print("Day", count)
        ft_call_harvest_recursive(day, count)
    else:
        print("Harvest time!")
