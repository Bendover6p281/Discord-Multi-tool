import requests
from colorama import Fore
from dhooks import Webhook
import os
import time

os.system("cls")

menu = (f"""{Fore.BLUE}
______  _________ _______  _______  _______  _______  ______    _________ _______  _______  _       
(  __  \ \__   __/(  ____ \(  ____ \(  ___  )(  ____ )(  __  \   \__   __/(  ___  )(  ___  )( \      
| (  \  )   ) (   | (    \/| (    \/| (   ) || (    )|| (  \  )     ) (   | (   ) || (   ) || (      
| |   ) |   | |   | (_____ | |      | |   | || (____)|| |   ) |     | |   | |   | || |   | || |      
| |   | |   | |   (_____  )| |      | |   | ||     __)| |   | |     | |   | |   | || |   | || |      
| |   ) |   | |         ) || |      | |   | || (\ (   | |   ) |     | |   | |   | || |   | || |      
| (__/  )___) (___/\____) || (____/\| (___) || ) \ \__| (__/  )     | |   | (___) || (___) || (____/
(______/ \_______/\_______)(_______/(_______)|/   \__/(______/      )_(   (_______)(_______)(_______/
                                                                                                    """)

print(menu)

option1 = (f"{Fore.LIGHTYELLOW_EX}[1] Spam Webhook")
option2 = ("[2] Send Message Through Webhook")
option3 = ("[3] Delete Webhook")

print()
print()
print()
print()

print(option1)
print(option2)
print(option3)

choice = input("Choice: ")

if choice == "1":
    webhookurl = Webhook(input("Webhook URL: "))
    message = input("Message: ")
    delay = float(input("Delay: "))

    while True:
        time.sleep(delay)
        webhookurl.send(message)
        print(f"{Fore.GREEN} [+] Sent Message")
elif choice == "2":
    webhookurl = Webhook(input("Webhook URL: "))
    message = input("Message: ")

    webhookurl.send(message)
    print(f"{Fore.GREEN} [+] Sent Message " + message)
    time.sleep(1)
    os.system("cls")
    print(menu)
    print()
    print()
    print()
    print()
    print(option1)
    print(option2)
    print(option3)
    choice = input("Choice: ")

elif choice == "3":
    webhookurl = Webhook(input("Webhook URL: "))

    webhookurl.delete()
    print(f"{Fore.RED} [-] Deleted Webhook")
    time.sleep(1)
    os.system("cls")
    print(menu)
    print()
    print()
    print()
    print()
    print(option1)
    print(option2)
    print(option3)
    choice = input("Choice: ")