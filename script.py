#!/usr/bin/python

def removeAll(a,item):
	new_a = []
	for el in a:
		if el != item:
			new_a.append(el)
	return new_a

a= [2,1,2,3,3,4,2,2,1]
print removeAll([2,1,2,3,3,4,2,2,1],2)

