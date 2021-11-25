import HelloWorld

def test():

	assert HelloWorld.pythagoras_hyp(5, 12) - 13.0 < 0.001
	
	assert HelloWorld.pythagoras_hyp(6, 8) - 10 < 0.001

if __name__ == "__main__":
	test()
	print("Passed!")
