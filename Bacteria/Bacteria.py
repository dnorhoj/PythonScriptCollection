year = 100 #Years you want to calculate
days = 0 #Days you want to calculate




Repeat = 1 #Creating times varible that tells the code how many times to repeat




Number = 1 #Creating Number varible that keeps track of how many times it has been repeated
i = 1 #Creating i to get the result

if (year > 0): # If year is set to a value calculate to how many times to repeat
	Repeat = 26280 * (year) #Calculation how many times to repeat
elif (days > 0): # Or if days is set to a value calculate how many times to repeat
	Repeat = 72 * (days) #Calculation on how many times to repeat

else: #Else tell that there is an error and you haven't set a time
	print ("Failed, did you fill out the Days/Years") #Tells in the console that there is an error
	quit() #Stops the program

while True: #Repeats until it has reached how many times it should be repeated     
		i = i * 2  # Doubles i (To find out how many times the cells has duplicated  
		Number = Number + 1 # Keeps track on how many times it has been repeated          
		if(Number > Repeat): #If it has repeated the right amout of times then
			print (i) # Show in the console how many times the have duplicated
			file = open('testfile2.txt', 'w') #Open a file
			file.write(str(i)) #Write in the result in the file
			file.close()	#Close the file		
			break # Stop the loop