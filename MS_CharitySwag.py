print("SWAG Budget Program \n \n" + "This program will calculate how many SWAG Items may be purchased for a company from the money budgeted.")

SWAG = input("Enter a Description of the SWAG item: ")
BeforeTaxPrice = float(input("Enter the purchase price of each SWAG Item before tax: $ "))


if BeforeTaxPrice <= 0 :
    print("The Price of the product is invalid")
    exit(0)


TotalAmountOfMoneyRaised = float(input("Enter the total amount of money budgeted: $ "))

HST_RATE = 0.13

PurchasePriceWithTax = round(BeforeTaxPrice * ( 1 + HST_RATE),2)
NumberOfSwags = int( TotalAmountOfMoneyRaised / PurchasePriceWithTax )

TotalPrice = NumberOfSwags * PurchasePriceWithTax
LeftOverMoney = round(TotalAmountOfMoneyRaised - TotalPrice,2)

print(f"With the total funds budgeted of ${TotalAmountOfMoneyRaised} the company can buy {NumberOfSwags} {SWAG} at ${PurchasePriceWithTax} each (including 13% HST) for a total of ${TotalPrice}. There would still be ${LeftOverMoney} leftover")
