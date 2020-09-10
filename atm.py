# Welcome message
# Enter the card
# Language selection - English, Hindi, Marathi
# Enter Pin
# services - Withdraw, Chnage Pin, Check balance
#   Withdraw -  Emter Amount 
#               Enetr OTP
#               collect cash
#               Print Receipt option - Y/N
#   change pin - Re-enter your pin
#                Enetr new pin 
#                Re-enter your new pin
#                pin changed
#   Check balance - display balance
# Back to welcome message

import time
import random
from users import users



while True:
    print("\nwelcome to SBI ATM")
    ins = input("please press 'I' to insert your card  >>> ")

    if ins == "I":
        print("please select language")
        languages = ["English", "Hindi", "Marathi"]
        for lang_idx, language in enumerate(languages, start=1):
            print(f"{lang_idx}. {language}")
        lang = input("Choose the number for language: ")

        if lang == "2" or lang == "3":
            print("Sorry for the inconvenience, we could not set Hindi/Marathi as your preffered language.\n English would be set by default  ")
        
        attempt = 1

        while attempt <= 3:
            user_pin = int(input("please enter your 4 digit ATM pin >>> "))
            
            if user_pin in users:
                first_name = users[user_pin]["first_name"]
                last_name = users[user_pin]["last_name"]
                account_no = users[user_pin]["account_no"]
                balance = users[user_pin]["balance"]
                currency = users[user_pin]["currency"]
                print(f" Hello {first_name} {last_name[0]}.\n what would you like to do?")
                options = ["withdraw", "change pin", "check balance"]

                for opt_idx, option in enumerate(options, start=1):
                    print(f"{opt_idx}. {option}")

                opt_inp = int(input("please select from the above options >>> "))

                while True:
                    if opt_inp in [1, 2, 3]:
                        if opt_inp == 3:
                            print("please wait...")
                            time.sleep(1.0)
                            print("we're fetching your account details")
                            time.sleep(2.0)
                            print(f"Your account balance is {currency}{balance}")
                        elif opt_inp == 1:
                            print("please wait...")
                            time.sleep(1.0)
                            wdw_inp = int(input(" Enter amount >>> "))
                            if wdw_inp > balance:
                                    print("Cannot withdraw amount greater than account balance!")
                            elif wdw_inp > 30000:
                                otp = random.randint(1111, 9999)
                                print(f"\nHINT: {otp}\n")
                                otp_inp = int(input("An OTP is sent to your "
                                                    "phone XXX-XXX-1234. "
                                                    "Please enter the OTP to "
                                                    "proceed with your "
                                                    "transaction >>> "))
                                if otp == otp_inp:
                                    balance -= wdw_inp
                                    print("\nProcessing...\n")
                                    time.sleep(2.0)
                                    print("Please collect your cash...")
                                    print("Your account balance is "
                                          f"{currency}{balance}")
                                    receipt = input("Press 'Y' for printing "
                                                    "transaction receipt >>> ")
                            else:
                                time.sleep(2.0)
                                print("Collect your cash")
                                time.sleep(3.0)
                                am_1, am_2 = balance, wdw_inp
                                total = am_1 - am_2
                                print(f"Your account balance is {total}\nThanks for visiting SBI ATM \nHave a good day!")
                        elif opt_inp == 2:
                            print("please wait...")
                            time.sleep(1.0)
                            user_pin1 = int(input("please re-enter your 4 digit ATM pin >>> "))
                            if user_pin1 in users:
                                new_pin = int(input("please enter your new pin >>> "))
                                new_pin1 = int(input("please re-enter your new pin >>> "))
                                if new_pin == new_pin1:
                                    print("please wait ...")
                                    if len(str(new_pin1)) == 4:
                                        temp = users[user_pin1]
                                        del users[user_pin1]
                                        users[new_pin1] = temp
                                    
                                        print("Pin changed successfully!")
                                        time.sleep(3.0)
                                        print("Thanks for visiting SBI ATM \nHave a good day!")
                                else:
                                    print("New pin mismatched\nThanks for visiting SBI ATM \nHave a good day!")
                            else:
                                print("invalid pin\nPlease try again")
                                time.sleep(3.0)
                                print("Thanks for visiting SBI ATM \nHave a good day!")
                    
                        else:
                            pass
                        break
                        
                    else:
                        print("please select a valid option!")
                    break
                break
            else:
                attempt += 1
                print(f"invalid pin. You have {4 - attempt} attempts remaining.")
        
        
    else:
        print("Card not inserted!\nThanks for visiting....Have a good day!")
