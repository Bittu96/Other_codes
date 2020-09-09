a = 'o'

try:
	print(indvsdeg)
	print(int(a))

except IOError:
	print('IOError')

except NameError:
	print('NameError')

except ValueError:
	print('ValueError')

except EOFError:
	print('EOFError')

except ImportError:
	print('ImportError')

except:
	print('bruh what ate you typing!')