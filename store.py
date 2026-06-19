print("loading store page...")
import time
import vrp
print("done in:" + time.strftime("%H:%M:%S"))
def store_page():
    if vrp.money > 0:
        print("Money: " + str(vrp.money))
        print("Want to buy chicken legs? Cost: " + str(vrp.costcl))
        print("Yes or no? (y/n)")
        if input("> ").lower() == "y":
            vrp.money -= vrp.costcl
            vrp.chickenlegscount += 1
            print("Chicken legs were added to your inventory.")
            return
        return
    else:
        print("Not enough money")
        print("Returning to pet in 5 seconds...")
        time.sleep(5)
        from main import savepet, breakout
        savepet()
        breakout()
