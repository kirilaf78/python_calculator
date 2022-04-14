import argparse


import math


#python C:\working.py --type annuity --principal 1000000 --periods 60 --interest 10


parser = argparse.ArgumentParser(description="This program is a calculator.")

parser.add_argument('--type')
parser.add_argument('--principal', type = int)       
parser.add_argument('--payment', type = int)
parser.add_argument('--interest', type = float)
parser.add_argument('--periods', type = int)

args = parser.parse_args()

parameters = [args.type, args.principal, args.payment, args.interest, args.periods]

i = 0
count = 0
negative_value = 0
a = 1

for element in parameters:
        if parameters[i] != None:
            i += 1
        else:
            count += 1
            i += 1
        
                    
if count >= 2:
        print('Incorrect parameters')


while a < len(parameters): 
        if parameters[a] == None or parameters[a] >= 0:
                a += 1
                       
        else:
            negative_value += 1
            a += 1
if negative_value >= 1:
        print('Incorrect parameters')


               

elif args.type != 'annuity' and args.type != 'diff' or args.type == None:
        print('Incorrect parameters')
  


elif args.interest == None:
        print('Incorrect parameters')        

     

elif args.type == 'annuity' and args.periods == None:
        nominal_interest_rate = args.interest / (12 * 100)
        a = args.payment / (args.payment - nominal_interest_rate * args.principal )
        b = 1 + nominal_interest_rate
        number_of_monthes = math.log(a, b)
        number_of_monthes = math.ceil(number_of_monthes)
        years = number_of_monthes // 12
        months = number_of_monthes % 12
        overpayment = (args.payment * number_of_monthes) - args.principal  
                     
        if years == 0 and months == 1:
                    print(f'It will take {months} month to repay this loan!')
        elif years < 1: 
                    print(f'It will take {months} months to repay this loan!')
        elif years == 1 and months == 0:
                    print(f'It will take {years} year to repay this loan!')
        elif years > 1 and months == 0:
                    print(f'It will take {years} years to repay this loan!')
        else: 
                    print(f'It will take {years} years and {months} months to repay this loan!')
        
        print(f'Overpayment = {overpayment}')    
               
       



    
elif args.type == 'annuity' and args.payment == None:
       
        nominal_interest_rate = args.interest / (12 * 100)
        in_pow = pow(1 + nominal_interest_rate, args.periods )
        args.payment = args.principal * ((nominal_interest_rate * in_pow) / (in_pow - 1))
        args.payment = math.ceil(args.payment)
        print(f'Your annuity payment = {args.payment}!')
        overpayment = (args.payment * args.periods) - args.principal
        print(f'Overpayment = {overpayment}')
        
elif args.type == 'annuity' and args.principal == None:
        nominal_interest_rate = args.interest / (12 * 100)
        in_pow = pow(1 + nominal_interest_rate, args.periods )
        loan_principal = args.payment / ((nominal_interest_rate * in_pow) / (in_pow - 1))
        loan_principal = math.floor(loan_principal)
        print(f'Your loan principal = {loan_principal}!')
        overpayment = (args.payment * args.periods) - loan_principal
        overpayment = round(overpayment)
        print(f'Overpayment = {overpayment}')        
        
elif args.type == 'diff' and args.payment == None:
        nominal_interest_rate = args.interest / (12 * 100)
        counter = 1
        total_paid = 0
        
        while counter <= args.periods:
                monthly_payment = args.principal / args.periods + nominal_interest_rate * (args.principal - ((args.principal * (counter - 1) / args.periods )))
                monthly_payment = math.ceil(monthly_payment)
                print(f'Month {counter}: payment is {monthly_payment}')
                total_paid += monthly_payment
                counter += 1
   
        overpayment = total_paid - args.principal    
        print(f'Overpayment = {overpayment}')         
