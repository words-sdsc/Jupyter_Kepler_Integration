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


#class inheritance 
class AnimalActions():
	def quack(self): return self.strings['quacks']
	def feathers(self):return self.strings['featehrs']
	def bark(self): return self.strings['bark']
	def fur(self):return self.strings['fur']
	def testing(self): print('Testing')

class Duck(AnimalActions):
#we can access the parent class functions by
# using super keyword.
	quacks = 'Quaaaaaak'
	featehrs = 'The duck has gray and white feathers'
	def testing(self):
		super().testing()
		print ("Additional testing")

donald = Duck()
donald.testing()
#print(donald.quack())
#raising custom exception
def readfile(filename):
	if filename.endswith('.txt'):
		opfile= open(filename)
		return opfile.readlines()
	else:
		raise ValueError('File extension should be .txt')


#Error handling in python
try:
	
	for line in readfile('lines.doc'):
		print(line)
except IOError as e:
	print("Something is wrong({})".format(e))
except ValueError as e:
	print('File extension is not right({})'.format(e))

print('After badness')


# working with numbers
h = 42
print(type(h), h)
h=42.0
print(type(h),h)
h = 42/9
print(type(h),h)
h = 42//9 
print(type(h),h)
h = round(42/9)
print(type(h),h)
h = round(42/9,2)
print(type(h),h)
h = divmod(42,9)
print(h)

# working with strings 
# srings are imutable objects
s = "This is a \n string"
print(s)
k = r"This is a string \n with charachter scaping"
print(k)

# string formatting
n = 54
# This fromat is for python 3, better to use this one
s = "This is a {} string ".format(n)
print(s)
#In python 2 we use this format, but dont use it
s = "This is a %s string"%n
print(s)
# if we have couple of lines of text we should use triple quote
s='''\
This is a string with 
line and
lines of
text
'''
print(s)

#working with tuples,and it is immutable
x =(2,5,7,8)
print(type(x),x)
#Working with lists, and it is mutable
x= [3,4,8,9]
# To append to the end of the list
x.append(5)
# to inser at the middle of the list.
x.insert(1,1000)
print(type(x),x)
print('Print 0 and 1 and 2 items in list')
print(x[0:3])
print('This one gives me every second elemnt')
print(x[0:3:2])
#Strings are another type of sequense and it is immutable
x= 'string'
print(type(x),x[2])
#slicing the string
#The way slices work on python is that they don't return the last element
print(x[2:4])
# All these sequence types can be used as iterators
x =(2,5,7,8)
for i in x:
	print(i)
x= 'string'
for i in x:
	print(i)
# dictionaries in python
d = {'one':1,'two':2,'three':3}
print(type(d),d)
for i in d:
	print(i,d[i])
print('\n')
# if we want to get the sorted dictionry when iterating we should use sorted function then they will be in
# alphebetical order by the keys
for i in sorted(d.keys()):
	print(i,d[i])

#Another way to define dictionary
d = dict(
	one = 1,
	two = 2,
	three = 3,
	four = 4,
	five = 5


	)
# you can add a new item to the dictionary:
d['seven'] = 7
for i in sorted(d.keys()):
	print(i,d[i])

# useing case statments in python
choices = dict(
	one = 1,
	two = 2,
	three = 3,
	four = 4,
	five = 5

	)

v = 'three'
print(v,":",choices[v])

# in the case that the choise does not exist or we do want to have a defult choise
v = 'Seven'
print(choices.get(v,'Default result'))


# Iterating using enumerators
fh = open('lines.txt')
for index,line in enumerate(fh.readlines()):
	print('Index is:',index, ' Line is : ',line)
#Passing aribitury arguments to the functions
#*args means arbitury arguments,this type of argument is tuple
def test(this,that,other,*args):
	print(this,that,other)
	for n in args:
		print(n)

test(1,234,545,6,3,5,6,7)

#working with strings
print('this is a string'.upper())
print('this is a string'.capitalize())
print('This Is a String'.swapcase())
print('this is a string'.find('is'))
print('this is a string'.replace('this','that'))
print('this is a string       '.rstrip())
print('this is a string\n'.rstrip('\n'))
print('this is a string       '.strip())

