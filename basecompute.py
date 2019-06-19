class Base(object):
	"""Base class group functions to compute a number from base 10 
	to n-base"""
		
	def base10toN(n_input, n_base):
		"""This function will compute from Base-10 to Base-N"""
		a = n_input//n_base
		b = n_input%n_base
		return a, b 
		# Returns a Tuple (a, b) ('a' will be compute for the next digit, 
		# 'b' is the reminder)

	def baseNto10(n_input, n_base):	
		"""This function will compute from Base-N to Base-10"""
		a = n_input*n_base
	# 	b = n_input%n_base #?????
		return a # , b # Returns a Tuple (a, b)

#TEST
print("base10toN")
print("Base 20: ", Base.base10toN(50, 20))
print("Base 18: ", Base.base10toN(50, 18))
print("baseNto10")
print("Base 20: ", Base.baseNto10(60, 20))
print("Base 18: ", Base.baseNto10(40, 18))