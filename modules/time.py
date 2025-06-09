import datetime

def tell_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    print(f"The time is {current_time}")
