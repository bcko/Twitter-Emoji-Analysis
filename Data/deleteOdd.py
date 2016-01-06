def main():
	infile = open("canada.txt")
	isOdd = False
	isHeading = True
	for line in infile:
		line.rstrip('\n')
		if isHeading == True :
			print(line, end="")
			isHeading = False
		elif isOdd == False :		
			print(line, end="")
			isOdd = True
		elif isOdd == True :
			isOdd = False
		else :
			pass
	infile.close()

main()
