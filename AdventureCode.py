#Adventure Game your_name
print("Last night, you went to sleep in your own home.")
print("Now, you wake up in a locked room.")
print("Could there be a lockpick hidden somewhere?")
print("In the room, you can see:")
#The menu funtion:
def menu(list, question):
  for item in list:
    print(1 + list.index(item), item)
   return int(input(question))
#This is a list of the items in the room:
items = ["backpack","paperbag","trashcan","basket","door"]
import random
keylocation = random.randint(1,4)
#The key is not found:
keyfound = "No"
loop = 1
#Display the menu until the key is found:
while loop == 1:
  choice = menu(items, "What do you want to inspect?")
  print("")
  if choice < 5:
    if choice == keylocation:
      print("you found a lockpick in the", items[choice -1])
      keyfound = "Yes"
    else:
      print("You found nothing in the", items[choice -1])
    elif choice == 5:
      if keyfound == "Yes":
        loop = 0 
        print("You insert the lockpick in the keyhole and jiggle it till it opens.")
       else:
        print("The door is locked. You need to find a key.")
      else
        print("Choose a number less than 6.")
print("You open the door to your freedom.")
