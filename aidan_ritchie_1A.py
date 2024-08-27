#Write an application to pre-sell a limited number of cinema tickets.
# Each buyer can buy up to 4 tickets. No more than 20 tickets can be sold total.
# Prompt the user for the desired number of tickets and then display the number
# of remaining tickets after their purchase. Repeat until all tickets have been sold.
# Then display the total number of buyers.

#create function and initialize variables so that they are accumulated properly

def ticketgenerator():
    total_tickets = 20

    remaining_tickets = total_tickets

    total_buyers = 0

#create a while loop that registers amount of tickets remaining, asks user how many tickets
#they'd like, and caps the amount they can buy at four using an if statement.

    while remaining_tickets > 0:

#print remaining tickets so buyer knows how many tickets are left

       print(f"There are currently {remaining_tickets} tickets remaining.")

       num_tickets = int(input("How many tickets would you like to purchase? "))

       if num_tickets > 4:

           print("Sorry, you cannot purchase more than 4 tickets.")

           continue

#create elif statement to alert customer if there are not enough tickets

       elif num_tickets > remaining_tickets:
           print("Sorry, there are not enough tickets for your order.")

           continue
#accumulate remaining tickets if transaction is successful, as well as total number of buyers
#after all tickets are sold.
       else:

           remaining_tickets -= num_tickets

           total_buyers += 1

    print(f"The total number of buyers was {total_buyers}.")

#call function

ticketgenerator()