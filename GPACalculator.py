def gpaCalculator():
	totalpoints = 0
	totalcredits = 0
	numclass = int(raw_input("How many classes are you taking? "))
	for i in range(0, numclass):
		if i == 0:
			credit = float(raw_input("How many credits was the first class? "))
		else:
			credit = float(raw_input("How many credits was the next class? "))
		grade = float(raw_input("What grade did you get in the class (in terms of number, ie: A = 4, A- = 3.666...)? "))
		totalpoints += totalpoints + (credit * grade)
		totalcredits += totalcredits + credit
	return totalpoints / totalcredits

print gpaCalculator()	