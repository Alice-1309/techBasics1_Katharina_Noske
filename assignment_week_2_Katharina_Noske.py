# Which plant is right for you?

# ChatAI generated me the best conditions for the plants

name= input("""
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

#monstera deliciosa (Swiss Cheese Plant)
if (light == "a lot"
        and temperature == "warm"
        and humidity == "high"
        and watering == "weekly"):
    print(f"{name} your perfect plant is a monstera deliciosa!")

    time.sleep(1)

    informations = input("""
    Would you like to have some information about the plant?
    (Answer options: yes, no)
    """)

    if informations == "yes":
        print("""
        The Monstera is a striking tropical plant known for its large, glossy, hole-punctured leaves. It thrives in bright, indirect light and prefers warm, humid environments. While it enjoys regular watering in summer, it should be allowed to dry slightly between waterings in winter. This plant adds a bold, modern touch to any room. It’s ideal for plant lovers who enjoy a bit of drama and care.
        """)
    else:
        print("Good Luck!")

#sansevieria trifasciata (Snake Plant / Mother-in-Law’s Tongue)
elif ((light == "a little" or light == "medium" or light == "a lot")
      and temperature == "warm"
      and humidity == "low"
      and watering == "once per month"):
    print(f"{name} your perfect plant is a sansevieria trifasciata!")

    time.sleep(1)

    informations = input("""
    Would you like to have some information about the plant?
    (Answer options: yes, no)
    """)

    if informations == "yes":
        print("""
        Sansevieria, or Snake Plant, is one of the most resilient indoor plants, perfect for beginners. It tolerates low light, infrequent watering, and dry indoor air with ease. Its upright, sword-like leaves add a sleek, architectural look to any space. It’s also known for purifying the air, making it a practical and stylish choice. Even neglect won’t harm it—true to its nickname, “Mother-in-Law’s Tongue.”
        """)
    else:
        print("Good Luck!")

#calathea makoyana (Peacock Plant)
elif (light == "a lot"
      and temperature == "warm"
      and humidity == "high"
      and watering == "twice per week"):
    print(f"{name} your perfect plant is a calathea makoyana!")

    time.sleep(1)

    informations = input("""
    Would you like to have some information about the plant?
    (Answer options: yes, no)
    """)

    if informations == "yes":
        print("""
        Calathea makoyana, also known as the Peacock Plant, features stunning, patterned leaves that move during the day. It thrives in bright, indirect light and requires high humidity to stay healthy. Water it regularly with room-temperature water, keeping the soil moist but not soggy. It’s a bit more demanding than other houseplants but well worth the effort for its unique beauty. A true showstopper for plant enthusiasts.
        """)
    else:
        print("Good Luck!")

#peperomia obtusifolia (Baby Rubber Plant)
elif ((light == "medium" or light == "a lot")
      and temperature == "warm"
      and humidity == "medium"
      and watering == "one every other week"):
    print(f"{name} your perfect plant is a peperomia obtusifolia!")

    time.sleep(1)

    informations = input("""
    Would you like to have some information about the plant?
    (Answer options: yes, no)
    """)

    if informations == "yes":
        print("""
        Peperomia obtusifolia is a compact, charming plant with thick, rounded leaves and a slow-growing habit. It adapts well to various light levels, from medium to bright indirect light. Water it sparingly—only when the soil is dry—making it ideal for forgetful plant parents. Its low-maintenance nature and cute appearance make it perfect for desks or shelves. A small plant with big personality.
        """)
    else:
        print("Good Luck!")

#hedera helix (English Ivy)
elif ((light == "a little" or light == "medium" or light == "a lot")
      and temperature == "cooler"
      and (humidity == "medium" or humidity == "high")
      and watering == "every other week"):
    print(f"{name} your perfect plant is a hedera helix")

    time.sleep(1)

    informations = input("""
    Would you like to have some information about the plant?
    (Answer options: yes, no)
    """)

    if informations == "yes":
        print("""
        Peperomia obtusifolia is a compact, charming plant with thick, rounded leaves and a slow-growing habit. It adapts well to various light levels, from medium to bright indirect light. Water it sparingly—only when the soil is dry—making it ideal for forgetful plant parents. Its low-maintenance nature and cute appearance make it perfect for desks or shelves. A small plant with big personality.
        """)
    else:
        print("Good Luck!")

else:
    print(f"{name} maybe a deco plant suits to you the most.")