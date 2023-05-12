import atmMenu
import atmOprations as ao
import atmExceptions as ae
import time

while True:
    atmMenu.menu()
    ch = int(input("Enter Your Choice: "))
    match ch:
        case 1:
            try:
                ao.deposit()
                time.sleep(5)
            except ae.depositError:
                print("Can't Deposit Zero or less amount.")
                time.sleep(5)
            except ValueError:
                print("Can't accept any alfa numeric, symbol etc...")
                time.sleep(5)
            except:
                print("Wrong input")
                time.sleep(5)
        case 2:
            try:
                ao.withdraw()
                time.sleep(5)
            except ae.withdrawError:
                print("Can't Withdraw Zero or less amount.")
                time.sleep(5)
            except ae.insufficientFundError:
                print("Can't Withdraw due to insufficient Balance.")
                time.sleep(5)
            except ValueError:
                print("Can't accept any alfa numeric, symbol etc...")
                time.sleep(5)
            except:
                print("Wrong input")
                time.sleep(5)
        case 3:
            ao.balenq()
            time.sleep(5)
        case 4:
            print("Thanks for using this program.")
            time.sleep(5)
            exit()
        case _:
            print("Wrong input. Please Try Again...")
            time.sleep(5)
