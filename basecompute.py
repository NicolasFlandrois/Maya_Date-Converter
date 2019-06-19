class Base(object):
	"""Base class group functions to compute a number from base 10 
	to n-base"""
		
	def base10to20(number):
		"""This function will compute from Base-10 to Base-20"""
		a = number//20
		b = number%20
		return a, b 
		# Returns a Tuple (a, b) ('a' will be compute for the next digit, 
		# 'b' is the reminder)

	def base10to18(number):
			"""This function will compute from Base-10 to Base-18"""
			a = number//18
			b = number%18
			return a, b # Returns a Tuple

	# def base18to10(number):	
	# 	"""This function will compute from Base-18 to Base-10"""
	# 	a = number//xyz
	# 	b = number%xyz
	# 	return a, b # Returns a Tuple

	# def base20to10(number):	
	# 	"""This function will compute from Base-20 to Base-10"""
	# 	a = number//xyz
	# 	b = number%xyz
	# 	return a, b # Returns a Tuple

#TEST
print(Base.base10to20(50))
print(Base.base10to18(50))