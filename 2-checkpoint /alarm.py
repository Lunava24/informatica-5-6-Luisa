def main():
    is_armed = False
    motion_detected = True
    door_open = False
    is_night = True
    display_alarm(is_armed, motion_detected, door_open, is_night)

def display_alarm(iar, ms, dop, an):
    if iar:
        if ms:
            print("INTRUDER!!!!!!!!")
        if dop:
            print("door is open")
    else:
        if an and ms:
            print("Welcome home! Turning the light on!")

main()

        