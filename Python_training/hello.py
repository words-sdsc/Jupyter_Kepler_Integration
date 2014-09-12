#!/usr/local/bin/python3
print('Hello World')

a,b =  55,1 
#Assigning zero to a and 1 to b
#In python you can assign multiple values at the 
#same time.



if a<b :
#THis is how you write conditional statments.
	print('a({}) is lees than be{}'.format(a,b))
	#This ({}) shows the value of a and be in 
	#The print stamtent
else:
	print('a({}) is NOT less than b({})'.format(a,b))

#One line condional sttatments
print("one" if a<b else "Two")

c,d =  0,1
#while loops
while d<50:
	print(d)
	c,d = d,c+d

#opening a file
fh = open("lines.txt")

#for loops 
for line in fh.readlines():
	print(line)
#Defining the end of the new line 
# to be only space not another new line
fh1 = open('lines.txt')
for line in fh1.readlines():
	print(line, end='')



# C type for loop
for e in range (4,7):
	print('e value is ({})'.format(e))

#Defining Functions
# Be carefull about the : after def,for,if
# use the exact False and True.
#
def isprime(n):
	if n==1:
		print('1 is special')
		return False
	for x in range(2, n):
		if n%x ==0:
			print(n,'is No prime')
			return False
	else:
		print(n,'is Prime')
		return True


for n in range(1,20):
	isprime(n)		

# working with Generator functions
# I have to revisit this part again
def isprimgen(n):
	if n==1:
		return False
	for x in range(2,n):
		if n%x == 0:
			return False
	else:
		return True

def primes(n=1):
	while(True):
#yield is like a return, it returns a value but the next time that the 
# function get called is continue after the yeild.
		if isprimgen(n):
			yield n
			print('yield is called on ',n)
		n +=1
		print("NOT YIELD ",n)
for n in primes():
	if n>100:break
	print('The actual printed ',n)

#Object oriented programming in python
class fibonachi():

	def __init__(self,a,b):
		self.a = a
		self.b = b

	def series(self):
		while (True):
			yield(self.b)
			self.a,self.b = self.b,self.a+self.b
			
f = fibonachi(0,1)
#f.series call the series function in calss fibonachi
for r in f.series():
	if r>100:break
	print (r,end='\n')


#class inheritance and polymorphisem in python

class AnimalActions:
	def quack(self): return self.strings['quack']
	def feathers(self):return self.strings['featehrs']
	def bark(self): return self.strings['bark']
	def fur(self):return self.strings['fur']

class Duck(AnimalActions):
	quack = 'Quaaaaaak'
	featehrs = 'The duck has gray and white feathers'

#Error handling in python
try:
	opfile= open('xlines.txt')
	for line in opfile.readlines():
		print(line)
except IOError as e:
	print("Something is wrong({})".format(e))

print('After badness')

