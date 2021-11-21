import HelloWorld

def test():

	assert HelloWorld.multiply(5, 10) == 50
	
	assert HelloWorld.multiply(5, -10) == -50

if __name__ == "__main__":
	test()
	print("Passed!")
