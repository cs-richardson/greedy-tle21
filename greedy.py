while True: #If the user enters a non-valid input, the program reprompts them to answer the right input and loops until the input is valid. 
    try:
        user_input = float(input("How much money is owed? ($): ")) 
        if user_input <0: #If user enters a negative value
            print("Invalid amount, please enter a valid amount")
            continue
        break
    except ValueError: #If user enters anything other than a float
        print("Invalid amount, please enter a valid amount")


owed_money = ((round(user_input,2)) * 100) #Multiplying input by 100

amount_of_quarters = (owed_money)//25 #Amount of quarters needed 
remain10 = (owed_money)%25 #Remainder to be divided by 10
print ("You need", int(amount_of_quarters), "quarter(s)") 

amount_of_dime = (remain10)//10 #Amount of dimes needed
remain5 = (remain10)%10 #Remainder to be divided by 5
print ("You need", int(amount_of_dime), "dime(s)")

amount_of_nickel = (remain5)//5 #Amount of nickels needed
remain1 = (remain5)%5 #Remainder to be divided by 1
print ("You need", int(amount_of_nickel), "nickel(s)")

amount_of_penny = (remain1)//1 #Amount of pennies needed 
print ("You need", int(amount_of_penny), "penny(ies)")

total_coins = amount_of_penny + amount_of_nickel + amount_of_dime + amount_of_quarters 

print ("You need", total_coins , "coins in total") #Calculates the total number of coins needed 


                     
                    
