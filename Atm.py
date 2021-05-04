class atm:
    def __init__(self,pin):
        self.pin = pin

    def checkBalance(self):
        print("Your current balance is INR 50000")

    def withdrawCash(self,amount):
        newAmount = 50000 - amount
        print("You have withdrawn"+str(amount) + ". Your remaining balance is "+ str(newAmount))
        print("Thank you for banking with me :)")

    def depositCash(self,amount):
        newAmount = 50000 + amount
        print("You have deposited " + str(amount) + ". You current balance is " + str(newAmount))
        print("Thank you for banking with me :)")

def main():


    print("")
    print("Welcome to Vibhu's ATM!")

    pin_number  = input("Enter your pin number: ")
    user =  atm(pin_number)

    print("")
    print("Choose: ")
    print("1 for Balance Enquriy")
    print("2 for Cash withdrawal")
    print("3 for cash deposit")
    print("")
    activity = int(input("Enter your activity number: "))

    if (activity == 1):
        user.checkBalance()
    elif (activity == 2):
        print("")
        amount = int(input("Enter the amount to be withdrawn: "))
        user.withdrawCash(amount)
    elif (activity == 3):
        print("")
        amount = int(input("Enter the amount to be deposited: "))
        user.depositCash(amount)
    else:
        print("enter a valid number")


if __name__ == "__main__":
    main()