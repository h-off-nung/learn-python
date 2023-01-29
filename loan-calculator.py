import argparse
import math

parser = argparse.ArgumentParser(description='Loan calculator.')

parser.add_argument("--type", type=str)
parser.add_argument("--payment", type=float)
parser.add_argument("--principal", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)

args = parser.parse_args()

if args.type is None or args.interest is None:
    print("Incorrect parameters")
    exit()
if args.payment is None and args.principal is None:
    print("Incorrect parameters")
    exit()
if (args.payment is None or args.principal is None) and args.periods is None:
    print("Incorrect parameters")
    exit()

n = args.periods
it = args.interest
overpay = 0

match args.type:
    case "annuity":
        i = it / 12 / 100
        if args.payment is None:
            if args.principal < 0 or args.periods < 0:
                print("Incorrect parameters")
                exit()
            p = args.principal
            monthly_pay = math.ceil(p * ((i * (1 + i) ** n) / ((1 + i) ** n - 1)))
            overpay = int(monthly_pay * n - p)
            print(f"Your monthly payment = {monthly_pay}!")
            print(f"Overpayment = {overpay}")
        if args.principal is None:
            if args.payment < 0 or args.periods < 0:
                print("Incorrect parameters")
                exit()
            pay = args.payment
            # solve the formula in two steps because of two fractions
            in_fraction = (i * (1 + i) ** n) / ((1 + i) ** n - 1)
            loan_principal = math.floor(pay / in_fraction)
            print("Your loan principal = {}!".format(loan_principal))
            overpay = int(pay * n - loan_principal)
            print(f"Overpayment = {overpay}")
        if args.periods is None:
            p = args.principal
            pay = args.payment
            number = math.ceil(math.log(pay / (pay - i * p), 1 + i))
            year = number // 12
            month = number % 12
            if year == 1 and month == 1:
                print("It will take 1 year and 1 month to repay this loan!")
            if year > 1 and month > 1:
                print("It will take {} years and {} months to repay this loan!".format(year, month))
            if year == 0 and month == 1:
                print("It will take 1 month to repay this loan!")
            if year == 0 and month > 1:
                print("It will take {} months to repay this loan!".format(month))
            if year == 1 and month == 0:
                print("It will take 1 year to repay this loan!")
            if year > 1 and month == 0:
                print("It will take {} years to repay this loan!".format(year))
            overpay = int(pay * number - p)
            print(f"Overpayment = {overpay}")

    case "diff":
        ir = it / 12 / 100
        p = args.principal
        for i in range(1, n + 1):
            dif_pay = math.ceil(p / n + ir * (p - ((p * (i - 1)) / n)))
            overpay += dif_pay
            print(f"Month {i}: payment is {dif_pay}")
        print()
        print(f"Overpayment = {math.floor(overpay - p)}")
    case other:
        print("Incorrect parameters")
