#!/use/bin/python3

CityDetails = {
'padmini': 'Mumbai',
'Neelam': 'Mumbai',
'Vini' :'Pune',
'Mini': 'Pune',
}

print(CityDetails)

print(CityDetails['padmini'])


for key in CityDetails :
	print (key,	" : ", CityDetails[key])
	
print(CityDetails.keys())
print(CityDetails.values())

print(max(10,20,40))