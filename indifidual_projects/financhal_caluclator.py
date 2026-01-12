"""
requierments
  ☐  ☑
       ☐How long it will take to save for a goal based on a weekly or monthly deposit
       ☐Compound Interest Calculator
       ☐Budget Allocator (use set percentages to divide an income into spending categories like savings, entertainment, and food)
       ☐Sale Price Calculator (apply discounts to prices)
       ☐Tip Calculator

steps

       ☐create a main function that will run the user interface
       ☐using project decomposition to figure out what other functions you need and how they interact with each other
       ☐implement at least one inner function within one of your main calculation functions. This inner function should handle a specific sub-task of the main function.
       ☐sure that your inner function demonstrates proper scope usage, accessing variables from its outer function if necessary.
       ☐Comment your code to explain the purpose and functionality of your inner function.
       ☐Create your functions
       ☐Have at least 2 people test your code to make sure it works

sudocode

import utill functions
 define main function
   repeat forever
       output "0 to quit, 1 for saveing calculator, 2 for copmpound intrest calculator, 3 for budget allocator, 4 for sale price calculator, 5 for tip calculator"
       user input = utill function input "what do you want to use" intager 0-5
       if user input = 0
           output "goodbye"
           return
       else if user input = 1
           run fucntion saveing calculator
       else if user input = 2
           run fucntion compound intrest calculator
       else if user input = 3
           run fucntion buget alocator
       else if user input = 4
           run fucntion sails price calculator
       else if user input = 5
           run fucntion tip calculator
define saveing calculator
   while True:
       if util input "0 to go back 1 to continue" =0
           return
      starting amount= util input "what is the starting amount"
      incrementation= util input "what is your deposit"
       delay= util input "how oftan will you deposit in days"
       goal= util input "what is your goal"
       amount=starting amount
       days=0
       while amount<goal 
          amount+=incrementation
          days+=delay
       output it will take "days" day(s) to get to "goal"
define compounding calc
    while true
        if util input "0 to go back 1 to continue" =0
            return
        amount=rounded to the second decimal util input "what is the starting amount"
        incrementation= util input "what is your deposit"
        delay= util input "how oftan will you deposit in days"
        intrest= util input "what is the intrest rate"
        intrest delay= util input "what is the intrist delay in days"
        time stop= util input "what is the day that is the end of the calculation"
        reapeat  time stop times
            if delay is multipule of repetition
                amount+=incrementation
            if intrest dlay is multipule of repetition
                amount *+(1+inttirist)
        output after "time stop" days with intrist of "itrest you will have $"amount" in the bank
define buget alocator
    while true
        if util input "0 to go back 1 to continue" =0
            return
        income= util input "what is your income"
        amount of items= util input "what are the amount of things you are saveing for"
        items=[]
        persentage=[]
        persent remaning=100
        reapeate amount of items
            add util input "what is item 'iteration'" to items
            choise=101
            while choise>persentage remaing
                choise= util input "what is perentage for that item persentage remaning:'persentage remaning', 0 to end adding items"
                if choise=0
                    brake
            if choise=0
                items remove last item
                brake
            add choies to persentage
        repeat lenght of items
            output "item":"persentage":"income/(persentage/100)
define sails
    while true
        if util input "0 to go back 1 to continue" =0
            return
        cost=util input"what is the cost"
        discont=util input "what is the discount in persentage (input like this: "5" for 5%)"
        output "the dicounted cost is "cost/(discont/100)"
define tip
    while true
        if util input "0 to go back 1 to continue" =0
            return
        bill= util input "what is the bill"
        tips=util input "what is your tip persent"
        output "the cost +you tip is "cost*(discont/100)"
if the curent file active is this file
    run main fucntion
"""
import utill_functions
def main():
    while True:
        user_input=utill_functions.get_valid_type(int,"0 to quit\n 1 for saveing calculator\n 2 for copmpound intrest calculator\n 3 for budget allocator\n 4 for sale price calculator\n 5 for tip calculator\nwhat do you want: ",valid=(0,5))
        if user_input==0:
            print("goodbye")
            return
        elif user_input==1:
            saveing()
        elif user_input==2:
            compond()
        elif user_input==3:
            budget()
        elif user_input==4:
            sails()
        elif user_input==5:
            tip()
def saveing():
    while True:
        if utill_functions.get_valid_type(int,"0 to go back\n1 to continue\nwhat do you want: ",valid=(0,1))==0:
            return
        start=utill_functions.get_valid_type(int,"what is your starting amount: ")
        delay=utill_functions.get_valid_type(int,"what is the delay between deposits: ")
        incrementation=utill_functions.get_valid_type(int,f"how much will you deposit every {delay} day(s): ")
        goal=utill_functions.get_valid_type(int,"what is your goal: ")
        days=0
        while start<goal:
            strat+=incrementation
            days+=delay
        print(f"it will take {days} day(s) to get to {goal}")
def compond():
    while True:
        if utill_functions.get_valid_type(int,"0 to go back\n1 to continue\nwhat do you want: ",valid=(0,1))==0:
            return
        amount=utill_functions.get_valid_type(int,"what is your starting amount: ")
        delay=utill_functions.get_valid_type(int,"what is the delay between deposits: ")
        incrementation=utill_functions.get_valid_type(int,f"how much will you deposit every {delay} day(s): ")
        intrest=utill_functions.get_valid_type(int,"what is the intrest rate: ")
        intrest_delay=utill_functions.get_valid_type(int,"what is the intrest delay: ")
        time_stop=utill_functions.get_valid_type(int,"what is the day that is the end of the calculation: ")
        for x in range(time_stop+1):
            if x%delay==0:
                amount+=incrementation
            if x%intrest_delay==0:
                amount*(1+intrest)
        print(f"after {time_stop} days with {intrest} intrest you will have ${amount}")
def budget():
    while True:
        if utill_functions.get_valid_type(int,"0 to go back\n1 to continue\nwhat do you want: ",valid=(0,1))==0:
            return
        income=utill_functions.get_valid_type(int,"what is your income: ")
        c_item=utill_functions.get_valid_type(int,"what are the amount of things you are saveing for: ")
        items=[]
        persentage=[]
        persent_remaning=100
        for x in range(c_item+1):
            items.append(utill_functions.get_valid_type(int,f"what is item {x+1} of items"))
            choise=101
            while choise>persent_remaning:
                choise=utill_functions.get_valid_type(int,f"what is perentage for that item\npersentage remaning:{persent_remaning}\n0 to end adding items: ")
                if choise==0:
                    break
            if choise==0:
                items.pop()
                break
            persentage.append(choise)
        print("item:persentage alocated:amount of monney")
        for x,y in enumerate(items):
            print(f"{y}:{persentage[x]}:{income&(persentage[x]/100)}")
def sails():
    while True:
        if utill_functions.get_valid_type(int,"0 to go back\n1 to continue\nwhat do you want: ",valid=(0,1))==0:
            return
        cost=utill_functions.get_valid_type(int,"what is the cost: ")
        discount=utill_functions.get_valid_type(int,"what is the discount (input like this: '5' for 5%): ")
        print(f"the discounted cost is {cost*(discount/100)}")
def tip():
    while True:
        if utill_functions.get_valid_type(int,"0 to go back\n1 to continue\nwhat do you want: ",valid=(0,1))==0:
            return
        bill=utill_functions.get_valid_type(int,"what is the bill: ")
        tips=utill_functions.get_valid_type(int,"what is the tip (input like this: '5' for 5%): ")
        print(f"the discounted cost is {bill*((tips/100+1))}")
            
if __name__=="__main__":
    main()