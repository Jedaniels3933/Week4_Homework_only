def main():
    while True:
        mood = input("How are you today? Please choose from the following..?  \nHappy, Sad, Mad , Nervous or Depressed: ")
        mood = mood.lower()
        if mood == "happy":
            print(f" It is great to see you {mood} for once!")
        elif mood == "sad":
            print(f" If you are {mood} please don't cry!")
        elif mood == "mad":
            print(f" Why you so {mood}, chill maybe?") 
        elif mood == "nervous":
            print(f" How {mood} are you maybe you need some meds")
        elif mood == "depressed":
                print(f" If you are {mood} you might be a Browns fan.")
        else:
            print(" I'm sorry, I didn't understand that,please choose from the options given.")
        continue
main()