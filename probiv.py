import time
import webbrowser
import colorama
import random
import requests

def phone():
    phone = input(colorama.Fore.CYAN + "Enter a phone number: ")
    time.sleep(2)
    print(colorama.Fore.CYAN + "Better let's call to this phone number?")
    time.sleep(2)
    webbrowser.open_new("https://web.telegram.org/")

def email():
    email = input(colorama.Fore.CYAN + "Enter a email: ")
    time.sleep(2)
    print(colorama.Fore.RED + "Error!")
    time.sleep(2)
    webbrowser.open_new("https://python.org/")

def nick():
    name = input(colorama.Fore.CYAN + "Enter a nickname: ")
    time.sleep(2)
    print(colorama.Fore.CYAN + "I don't know, better go to watch YouTube")
    time.sleep(2)
    webbrowser.open_new("https://youtube.com/")
    time.sleep(2)

def ip():
    address = input(colorama.Fore.CYAN + "Enter a IP-Address: ")
    time.sleep(2)
    print(colorama.Fore.CYAN + "No informations, better go to listen music")
    time.sleep(2)
    webbrowser.open_new("https://soundcloud.com/")

def main():
    time.sleep(0.5)
    ASCII = """
     ____  ____   __  ____  __  _  _    ____  _  _
    (  _ \(  _ \ /  \(  _ \(  )/ )( \  (  _ \( \/ )
     ) __/ )   /(  O )) _ ( )( \ \/ /_  ) __/ )  / 
    (__)  (__\_) \__/(____/(__) \__/(_)(__)  (__/  
    """
    print(colorama.Fore.CYAN + ASCII)
    
    while True:
        time.sleep(2)
        print(colorama.Fore.CYAN + "1. IP-Address")
        time.sleep(0.5)
        print(colorama.Fore.CYAN + "2. Nickname")
        time.sleep(0.5)
        print(colorama.Fore.CYAN + "3. Email")
        time.sleep(0.5)
        print(colorama.Fore.CYAN + "4. Phone number")
        time.sleep(0.5)
        print(colorama.Fore.CYAN + "5. Quit")
        time.sleep(0.5)
        main_1 = input(colorama.Fore.CYAN + "Choice: ")
        
        if main_1 == "1":
            time.sleep(2)
            ip()
            break
        elif main_1 == "2":
            time.sleep(2)
            nick()
            break
        elif main_1 == "3":
            time.sleep(2)
            email()
            break
        elif main_1 == "4":
            time.sleep(2)
            phone()
            break
        elif main_1 == "5":
            time.sleep(2)
            return
        else:
            print(colorama.Fore.RED + "Please, enter a number, from 1 to 5: ")
    

if __name__ == "__main__":
    main()
