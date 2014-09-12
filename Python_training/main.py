#!/usr/local/bin/python3

#In order to call the functions after they called we have to use main functon
def main():
	print('Calling function before it defined')
	test()
		
def test():
	print('Hello test after fuction call')

if __name__ == "__main__":	main()