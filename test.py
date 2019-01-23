def print_params_3(**params):
	print (params)
	
print_params_3(x=1, y=2, z=3)
print_params_3()

def print_param(*params):
	print(params)

print_param("Testing",1)
print_param(1,2,3,4)

def print_params_4(x, y, z=3, *pospar, **keypar):
	print (x, y, z)
	print (pospar)
	print (keypar)
print_params_4(1, 2, 3, 5, 6, 7, foo=1, bar=2)
print_params_4(1, 2)

