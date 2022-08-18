# variables
startingAmount = "0"
returnRate = "0"
howLong = "0"
additionalContribution = "0"
endingInterest = "0"
save = "0"
restart = "1"
while restart == "1":
    # essential input from user
    input("investment calculator")
    startingAmount = int(input("Starting amount: "))
    returnRate = int(input("Return rate: "))
    howLong = int(input("Length in years: "))
    #additionalContribution = int(input("Additional contribution: "))
    endingInterest = ((startingAmount * returnRate)/100)
    total = (endingInterest + startingAmount)
    #print("\n-----------------------------------------------------------\nInterest earned: $" +str(int(endingInterest)) + "\nTotal: $" + str(int(total))+"\n-----------------------------------------------------------")
    # input("end")
    # calculations
    save = str(float((startingAmount*(1+((returnRate/100)/1))**howLong) - startingAmount))
    print("-----------------------------------------------------------\nYour interest earned is: $" + save + "\n-----------------------------------------------------------")
    restart = input("restart? (1 or 0): ")
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")