# Which plant is right for you?

# ChatAI generated me the best conditions for the plants

name = input("""
What is your name?
""")

print(f"""
Hello {name} :)
Together we will find the best plant for you!
""")

import time
time.sleep(2)

print("""
Before we know what plant suits you, you need to answer the following questions:
""")

time.sleep(1)

light = input("""
How much light does the plant get, in the spot you have in mind? 
(Answer options: a lot, medium, a little)
""")

temperature = input("""
What is the temperature like in the spot? 
(Answer options: warm, medium, cooler)
""")

humidity = input("""
What is the humidity like in the spot? 
(Answer options: high, medium, low)
""")

watering = input("""
How often would you be willing to water the plant?? 
(Answer options: twice per week, weekly, every other week, once per month)
""")

print("")

time.sleep(3)

#Monstera deliciosa (Swiss Cheese Plant)
if (
    light == "a lot"
    and temperature == "warm"
    and humidity == "high"
    and watering == "weekly"
    ):
    print(f"{name} your perfect plant is a monstera deliciosa!")

#Sansevieria trifasciata (Snake Plant / Mother-in-Law’s Tongue)
elif (
        light == "a little" or "medium" or "a lot"
        and temperature == "warm"
        and humidity == "low"
        and watering == "once per month"
        ):
        print(f"{name} your perfect plant is a sansevieria trifasciata!")

#Calathea makoyana (Peacock Plant)
elif (
        light == "a lot"
        and temperature == "warm"
        and humidity == "high"
        and watering == "twice per week"
        ):
        print(f"{name} your perfect plant is a calathea makoyana!")

#Peperomia obtusifolia (Baby Rubber Plant)
elif (
        light == "medium" or "a lot"
        and temperature == "warm"
        and humidity == "medium"
        and watering == "one every other week"
        ):
        print(f"{name} your perfect plant is a peperomia obtusifolia!")

#Hedera helix (English Ivy)
elif (
        light == "a little" or "medium" or "a lot"
        and temperature == "cooler"
        and humidity == "medium" or "high"
        and watering == "every other week"
        ):
        print(f"{name} your perfect plant is a hedera helix")

else: print(f"{name} maybe a deco plant suits to you the most.")