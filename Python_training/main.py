#!/usr/local/bin/python3

#In order to call the functions after they called we have to use main functon
def main():
	print('Calling function before it defined')
	a = 'one'
#In order to find the type of variabel we should use tyep(variable) function
	print('A is :',type(a))
	b = 5
	print('B is :',type(b))
	test()
		
def test():
	print('Hello test after fuction call')

if __name__ == "__main__":	main()