name = input("what is your name?: ")
print(f"hello {name} and welcome to ct8")

print("Today i will tell a story with your help") 
print("") 
print("")  
name = input("Pick a name: ")
pronoun = input("how do they identify: type 1 for he/him, 2 for she/her, 3 for them/they: ")
if pronoun == "1":
    subject_pr = "he"
    object_pr = "his"
elif pronoun == "2":
    subject_pr = "she" 
    object_pr = "her's"
else:
    subject_pr = "they"
    object_pr = "their"

place_to_eat = input("now pick a place to eat: ")
if place_to_eat == "burger master":
    print(" amazing thats my favorite place to eat ")
elif "burger" in place_to_eat:
    print ("almost my favorite but good choice ")
else:
    print("ok not my favorite but good choice ")
location = input("now that we have all the information we are just missing one thing location please pick a location: ")
print("~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*~~~*")
print(f"one day, {name} wanted to go get {place_to_eat} but {subject_pr} didn't know how to get there so {subject_pr} searched it up on the internet but the nearest one was 12 miles away so {subject_pr} started walking and walking. Then {subject_pr} walked by {location} and after walking 12 miles {subject_pr} finally made it and got {object_pr} food ")



