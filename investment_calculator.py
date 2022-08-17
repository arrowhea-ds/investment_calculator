# variables
startingAmount = "0"
returnRate = "0"
howLong = "0"
additionalContribution = "0"
endingInterest = "0"
# essential input from user
input("investment calculator")
startingAmount = int(input("Starting amount: "))
returnRate = int(input("Return rate: "))
#howLong = int(input("Length in years: "))
#additionalContribution = int(input("Additional contribution: "))
endingInterest = ((startingAmount * returnRate)/100)
total = (endingInterest + startingAmount)
print("Interest earned: $" + str(int(endingInterest)) + "\nTotal: " + str(total))
input("end")
# calculations
# while howLong > 0:
