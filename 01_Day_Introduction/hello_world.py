#EERCISE LEVEL 1

a= 3
b= 4
def add():
    print(a+b)
def subtraction():
    print(a-b)
def multiplication():
    print(a*b)
def modulus():
    print(a%b)
def division():
    print(a/b)
def exponential():
    print(a**b)
def floor_division_operator():
    print(a//b)

#EXERCISE 2

name = "Mpho"
surname = "Mofokeng"
country = "South Africa"
print(name, "\n",surname,"\n",country,"\n","I am enjoying 30 days of python")

print(type(10))
print(type(9.8))
print(type(3.14))
print(type(4-4j))
print(type(['Asabeneh', 'Python', 'Finland']))
print(type("MPHO"))
print(type("MOFOKENG"))
print(type("South Africa"))

#Exercize level 3
#Finding a eucledian distance between two points 
#Eucledian distance can be found using pythagorus theorem 
# pythagorus theorem says that r =x**2 +y**2 +so how to go about it is:

def pythagorus_theorem(x,y):
    distance = y**2 +x**2
    return distance
print(pythagorus_theorem(2,3)) 
print(pythagorus_theorem(10,8))