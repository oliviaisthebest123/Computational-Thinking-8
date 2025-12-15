print ("hello this quiz will be to show what your spirit animal is: ")
name = input ("what is your name: ")
print("")

sloth = 0
cheetah = 0
fox = 0 
hamster = 0 
gorilla = 0 
lion = 0 
pig = 0 
whale = 0 

print(f"hello {name} welcome to the spirit animal quiz ")
question1= input("pick one of these answers a for sleeping: b for working out: C for camping: d for spending time with people: e for telling people what to do: f for eating junk food: g for swimmming:  ")

print("")

if question1== "a":
    sloth+=1

elif question1== "b":
    gorilla+=1 
    lion+=1
    cheetah+=1

elif question1== "c":
    fox+=1

elif question1== "d":
    hamster+=1

elif question1== "e":
    lion+=1

elif question1== "f":
    pig+=1

elif question1== "g":
    whale+=1

question2= input("now pick your favorite: 1 for spring: 2 for summer: 3 fall/autumn: 4 winter: ")

print("")

if question2== "1":
    hamster+=1
    cheetah+=1
    gorilla+=1

elif question2== "2":
    lion+=1
    whale+=1
    pig+=1
    sloth+=1

elif question2== "3":
    fox+=1

color = input("what is your favorite colors: 1 for red: 2 for orange: 3 yellow: 4 green: 5 blue: 6 purple: 7 pink: 8 white: 9 black: ")

print("")

if color== "1":
    fox+=1

elif color== "2":
    cheetah+=1

elif color== "3":
    lion+=1
    cheetah+=1


elif color== "4":
    gorilla+=1
    hamster+=1

elif color== "5":
    whale+=1
     
elif color== "7":
    pig+=1

elif color== "8":
    sloth+=1

elif color== "9":
    sloth+=1
    gorilla+=1 

you = input ("what matches you the best: 1 happy: 2 sad: 3 loveable: 4 Calm: 5 angry: ")

if you== "1":
    pig+=1
    fox+=1

elif you== "2":
    sloth+=1
    whale+=1

elif you == "3":
    hamster+=1
    pig+=1

elif you  == "4":
    sloth+=1 

elif you== "5":
    cheetah+=1
    lion+=1
    gorilla+=1 

hair= input("what color is your hair:1 brown: 2 blond: 3 ginger: 4 red: 5 blue: 6 black: 7 other: ")

if hair== "1":
    hamster+=1
    cheetah+=1
    sloth+=1 

elif hair== "2" :
    lion+=1

elif hair== "3":
    fox+=1

elif hair== "4":
    fox+=1
    pig+=1 

elif hair== "5":
    whale+=1

elif hair== "6":
    gorilla+=1

if gorilla > whale and gorilla >= fox and gorilla >= lion and gorilla >= sloth and gorilla >= pig and gorilla >= cheetah and gorilla >= hamster:
    print ("you are strong like a gorilla! ")

elif whale >= fox and whale >= lion and whale >= sloth and whale >= pig and whale >= cheetah and whale >= hamster: 
    print ("you love to swim like a whale! ")

elif fox >= lion and fox >= sloth and fox >= pig and fox >= cheetah and fox >= hamster: 
    print (" you are fearless like a lion! ")

