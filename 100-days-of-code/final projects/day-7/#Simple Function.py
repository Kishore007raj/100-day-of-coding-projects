#Simple Function
def greet():
  print("Hello Angela")
  print("How do you do Jack Bauer?")
  print("Isn't the weather nice today?")
greet()

#Function that allows for input
def greet_with_name(name):
 print(f"Hello {name}")
 print(f"How do you do {name}?")
greet_with_name("Kishoreraj")

#function with more than one input

def greet_me(name,location):
  print(f"hello {name}")
  print(f"this is arnold from {location}")

greet_me("jack","usa")

#positional arguement 

def greet_me(name,location):
  print(f"hello {name}")
  print(f"this is arnold from {location}")

greet_me("usa","jack")

# functions with keyword argument

def greet_me(name,location):
  print(f"hello {name}")
  print(f"this is arnold from {location}")

greet_me(name="alex",location="usa")
