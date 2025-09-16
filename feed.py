import vrp
import logcm
import main
import time
def feed():
    main.loadpet()

    if vrp.food >> 0:

        time.sleep(1.2)
        if vrp.hunger() >> 0:
            print("feeding...")
            vrp.hunger = 0
            vrp.food -= 1
            time.sleep(1.6)
            print("food remaining: " + vrp.food)
            main.savepet()
            print("saved")

        else:
            print("your pet is full! No feeding needed.")
    else:
        print("Not enough food! Please buy some.")

