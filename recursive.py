#!/usr/bin/env python
# Result list
stuff = []
print("Write out a recursive function to show the \n\
	total of the integers in this list:\n\
	[[0, \"dub\"], 2, ['Stuff', 2], [4], [1, 2]]")

def get_total_integers(elements):
	"""Get the total of integers in a given list"""

	## If we got a list
	if isinstance(elements, (list, )):
		## For each element in the elements parameter
		for element in elements:
			# If we got a list as parameter
			if isinstance(element,(list,)):
				# Run de function again
				get_total_integers(element)
			# If the element is an integer
			elif isinstance(element, (int, )):
				# Notify to the user: we're adding the element
				print(f"Appending element: {element}")
				# Appending the element to the result list
				stuff.append(element)
			# De lo contrario
			else:
				# Notify to the user: We're not adding the element
				print(f"Excluding element: {element}")
	# Else: we don't have a list as parameter
	else:
		# Exit the program and raise and exception
		raise ValueError("This function needs a list.")
	# return the result list
	return len(stuff)

# Get all the integers in a given list
t = get_total_integers([[0, "Stuff"], 2, [None, 2], [4, {'one':'1'}], [1, 2]])
# Printing results
print(f"total of integers is: {t}")


if __name__ == '__main__':
  pass
