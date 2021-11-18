import time

Response = (str(input("Have you started your work? ''Type yes or no'' "))).lower()
if(Response == "yes"):
    print("Ok, so I am your personal assistant FLAPPY! I will take care of your eyes by reminding you after every 20 minutes to take a break... Let's start... ")
    time.sleep(1200)
    print("Please look 20 feet away for next 20 seconds!")

    while(True):

        time.sleep(20)
        print("You can continue your work!")
        time.sleep(1200)
        print("Please look 20 feet away for next 20 seconds!")
