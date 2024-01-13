#!/usr/bin/env python3
# Your Python code goes here
import sys
import random
import string

class Color:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    WHITE = '\033[97m'

inp_count=int(len(sys.argv[1]))
print(f"{Color.PURPLE}The length of your input is "+str(inp_count)+f"{Color.RESET}\n")
user_input=input(f"{Color.GREEN}Enter your input Do you want to replace with \n1.int\n2.str\n3.Special Characters\n4.Mix Characters\n{Color.RESET}")

if(user_input.lower()=="int" or user_input=="1"):
  z=''.join(str(random.randint(0,9)) for _ in range(inp_count))
  print(z)
elif(user_input.lower()=="str" or user_input=="2"):
  alp=string.ascii_letters
  random_alphabet = ''.join(random.choice(alp) for _ in range(inp_count))
  print(random_alphabet)
elif(user_input.lower()=="random" or user_input=="3"):
  z=string.punctuation
  out=''.join(random.choice(z) for _ in range(inp_count))
  print(out)
elif(user_input.lower()=="mix" or user_input=="4"):
  z=string.ascii_letters+string.punctuation
  out=''.join(random.choice(z) for _ in range(inp_count))
  print(out)
  
else:
  print("Please enter valid option")