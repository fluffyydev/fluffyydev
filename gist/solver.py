#Introduction
print('\033[40m' + '\033[37m' + "⭐ Made by  fluffyydev ⭐")
print('\033[0m' + '\033[34m' + "The question below is the one I will solve for you: \n")
#Input
NumberForQuestion = input('\033[35m' + "\nIf you would only like to know if a specific door is open, type the number of the door you want from \033[4m\033[30m1-1000\033[0m\033[35m. Otherwise, type \033[4m\033[30m'all'\033[0m\033[35m for a list of every door or \033[4m\033[30m'explain'\033[0m\033[35m for the explanation along with the answer!.")

#Varibles
y = 1
ds = "\033[31m\nClosed"
index = 1
vt = 1
opened = 0
orc = "c"

#Code
if NumberForQuestion == "all":
  print("\nOkay, here is a chart of all the doors.")
  while index < 1001:
    while vt < 1001:
      ok = index % vt
      if ok == 0:
        if orc == "c":
          orc = "o"
        else:
          orc = "c"
      vt = vt + 1
    if orc == "o":
      opened = opened + 1
      orc = "\033[1m\033[4m\033[32mOpen\033[0m"
    else:
      orc = "\033[31mClosed\033[39m"
    hg = str(index)
    print(hg + ": " + orc)
    orc = "c"
    vt = 1
    index = index + 1
  opened = str(opened)
  print("So in total, there will be " + '\033[4m' + '\033[32m' + opened + " locker doors\033[0m open.")
elif NumberForQuestion.isnumeric():
  x = int(NumberForQuestion)
  while y != 1001:
    z = x % y
    if z == 0:
      if ds == "\033[31m\nClosed":
        ds = "\033[32m\nOpen"
      else:
        ds = "\033[31m\nClosed"
    y = y + 1
  print(ds)
elif NumberForQuestion == "explain":
  print('\033[32m' + '\033[4m' + "\nThe number of locker doors open is 31.")
  print('\033[0m' + "\nHow do I know this? Well, each locker will be opened or closed by each of its divisors. For example, locker 15 will be opened and closed by students 1, 3, 5 and 15. Which means it is opened then closed, then opened and finally closed. So this means that all lockers with an even amount of divisors will be closed. So in order to have an open locker, it needs to have an odd amount of divisors. In order for a number to have an odd amount of divisors, it has to be a perfect square because a divisor will repeate and a student only interacts with a locker door once or not at all. Then you just need to find all the perfect squares in 1000 which are 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900 and 961 which comes out to 31 open lockers.")
  
else:
      print("\nNumbers have to be in numerical form and anything typed has to be lowercase.")
