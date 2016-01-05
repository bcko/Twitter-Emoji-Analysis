def main():
	infile = open("korea.txt")
	isEven = False
	for line in infile:
		line.rstrip('\n')
		if isEven == False :		
			print(line, end="")
			isEven = True
		elif isEven == True :
			isEven = False
		else :
			pass
	infile.close()

main()
