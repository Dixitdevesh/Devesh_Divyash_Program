import speech_recognition as sr
import webbrowser
import pyttsx3
import random
import os
import datetime
import time

tell = pyttsx3.init()
r = sr.Recognizer()

def speak(text):
    tell.say(text)
    tell.runAndWait()

def listen():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            audio = r.listen(source, timeout=12, phrase_time_limit=15)
            print("Recognizing...")
            command = r.recognize_google(audio)
            print(f"You Said: {command}")
            return command
    except Exception as e:
        print(f"Error: {e}")
        return ""
def s(x=30):
    time.sleep(x)
def menu():
    speak("Now Menu will Apear So It Take Some time to Initialize Perfectly... ")
    print("\n" + "="*30)
    print("  Jarvis Menu")
    print("="*30)
    print("  **Web Browsing** 📊")
    print("  1. Open Google 🌐")
    print("  2. Open Facebook 👥")
    print("  3. Open Instagram 📸")
    print("  4. Open YouTube 📺")
    print("  5. Open Email 📧")
    print("  6. Open Twitter 🐦")
    print("  7. Open Reddit 📖")
    print("  8. Search on Google 🔍")
    print("  9. Search on YouTube 🎥")
    s(5)
    print("\n  **Entertainment** 🎵")
    print("  10. Play Music 🎶")
    print("  11. Truth and Dare 😜")
    print("  12. Chat with me! 💬")
    print("  13. Play a number guessing game 🎲")
    print("  14. Solve a riddle 🧩")
    print("  15. Play rock-paper-scissors ✊")
    print("  16. Take a quiz 📝")
    s(5)
    print("\n  **Productivity** 📊")
    print("  17. Calculate 📝")
    print("  18. Create a new text file 📄")
    print("  19. View current date and time 🕒")
    print("  20. Set a timer ⏳")
    s(5)
    print("\n  **Applications** 📈")
    print("  21. Open Application 📊")
    print("  22. Close Application ❌")
    s(5)
    print("\n  **Help** 🤔")
    print("  23. Show Help")
    s(2)
    print("\n  **About** 🤔")
    print("  24. About Jarvis")
    s(2)
    print("\n  **Exit** 👋")
    print("  99. Exit Jarvis")
    print("="*30)

def about():
    print("\n" + "="*30)
    print("  About Jarvis")
    print("="*30)
    print("  Created by: Devesh Dixit")
    print("  Assisted by: Sumit Kumar")
    print("  Version: 1.0")
    print("  Jarvis is an AI assistant designed to help you with tasks and keep you company!")
    print("="*30)

def login():
    print("Welcome to Jarvis!")
    speak("Welcome to Jarvis! Please tell me your name.")
    name = listen()
    print(f"Hello, {name}! How can I assist you today?")
    speak(f"Hello, {name}! How can I assist you today?")
    return name

def chat():
    responses = {
        "how are you": "I'm doing fantastic! Thank you for asking. How about you?",
        "what's your name": "I'm Jarvis, your loyal assistant! I'm here to help you with anything you need.",
        "what do you like": "I enjoy chatting with you and helping you with your tasks! It's always fun to assist.",
        "tell me a joke": "Why don't scientists trust atoms? Because they make up everything! Haha, get it?",
        "i love you": "Aww, I love you too! You're the best!",
        "what are you doing": "I'm just hanging out, waiting for you to talk to me! What's on your mind?",
        "what's your favorite color": "I think I'd love blue! It reminds me of the sky on a clear day.",
        "tell me something interesting": "Did you know honey never spoils? Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3000 years old and still perfectly edible!",
        "what's your favorite movie": "I love all the classic sci-fi movies! They always spark my imagination.",
        "what's your favorite food": "I think I'd enjoy pizza. It's so popular! What's yours?",
        "do you have a favorite song": "I think I'd love any song that makes you happy. Music is such a beautiful art!",
        "tell me about yourself": "I'm an AI designed to assist you, learn from you, and entertain you. What about you? Tell me something about yourself!"
    }
    
    speak("I'm here to chat! What would you like to talk about? You can ask me anything or just say 'exit' to stop chatting.")
    while True:
        command = listen().lower()
        if "exit" in command or "stop" in command:
            speak("Alright, I'm here whenever you need me! Just say my name to talk again.")
            break
        
        response = responses.get(command, "I'm not sure how to respond to that. What else would you like to know?")
        speak(response)
        print(f"Jarvis: {response}")

def search_google():
    speak("What do you want to search on Google?")
    query = listen()
    webbrowser.open(f"https://www.google.com/search?q={query}")
    speak(f"Searching Google for {query}")

def search_youtube():
    speak("What do you want to search on YouTube?")
    query = listen()
    webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
    speak(f"Searching YouTube for {query}")

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    speak("Welcome to the number guessing game! I'm thinking of a number between 1 and 100. Can you guess what it is?")
    print("Number Guessing Game Started! Guess the number between 1 and 100.")
    
    while True:
        speak("Please say your guess.")
        guess = listen()
        attempts += 1
        
        if guess.isdigit():
            guess = int(guess)
            if guess < number_to_guess:
                speak("Too low! Try again.")
                print("Jarvis: Too low! Try again.")
            elif guess > number_to_guess:
                speak("Too high! Try again.")
                print("Jarvis: Too high! Try again.")
            else:
                speak(f"Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                print(f"Jarvis: Congratulations! You've guessed the number {number_to_guess} in {attempts} attempts!")
                break
        else:
            speak("Please say a valid number.")

def solve_riddle():
    riddle, answer = ("I speak without a mouth and hear without ears. I have no body, but I come alive with the wind. What am I?", "echo")
    speak(riddle)
    print(f"Jarvis: {riddle}")
    
    while True:
        speak("What is your answer?")
        user_answer = listen().lower()
        
        if user_answer == answer:
            speak("Correct! You solved the riddle! 🎉")
            print("Jarvis: Correct! You solved the riddle! 🎉")
            break
        else:
            speak("That's not quite right. Try again!")
            print("Jarvis: That's not quite right. Try again.")

def play_rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    speak("Let's play rock-paper-scissors! Say your choice.")
    
    user_choice = listen().lower()
    if user_choice not in options:
        speak("That's not a valid choice. Please say rock, paper, or scissors.")
        return
    
    computer_choice = random.choice(options)
    speak(f"I chose {computer_choice}.")
    
    if user_choice == computer_choice:
        speak("It's a tie! We both chose the same thing.")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        speak("You win! 🎉")
    else:
        speak("I win! Better luck next time!")

def take_quiz():
    questions = {
        "What is the capital of France?": "paris",
        "What is 5 + 7?": "12",
        "Who wrote 'Romeo and Juliet'?": "shakespeare",
        "What is the largest planet in our solar system?": "jupiter",
        "What year did the Titanic sink?": "1912",
        "What is the chemical symbol for water?": "h2o",
        "Who painted the Mona Lisa?": "da vinci",
        "What is the smallest prime number?": "2"
    }
    
    score = 0
    for question, answer in questions.items():
        speak(question)
        print(f"Jarvis: {question}")
        user_answer = listen().lower()
        
        if user_answer == answer:
            speak("Correct! 🎉")
            print("Jarvis: Correct! 🎉")
            score += 1
        else:
            speak(f"Sorry, the correct answer is {answer}.")
            print(f"Jarvis: Sorry, the correct answer is {answer}.")
    
    speak(f"You scored {score} out of {len(questions)}. Thanks for playing the quiz!")

def open_application():
    speak("Which application do you want to open?")
    app_name = listen().lower()
    
    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "paint": "mspaint.exe",
    }
    
    if app_name in apps:
       try:
           os.startfile(apps[app_name])
           speak(f"Opening {app_name}.")
           speak(f"{app_name} Successfully opened")
       except Exception as e :
           speak("Sorry ,Some error occured... ")
    
    else:
        try:
            os.startfile(f"{app_name}.exe")
            speak("Successfully opened")
        except Exception as e :
            print("error occured ")

def close_application():
    speak("Which application do you want to close?")
    app_name = listen().lower()
    if app_name == "notepad":
        os.system(f"taskkill /im notepad.exe")
        speak("Closed Successfully...")
    elif app_name=="calculator":
        os.system(f"taskkill /im calc.exe")
        speak("Closed Successfully")
    elif app_name=="paint":
        os.system(f"taskkill /im mspaint.exe")
        speak("Closed Succesfully")    
    else:
        os.system(f"taskkill /im {app_name}.exe")
        speak(f"Closing {app_name}.")

def calculate():
    speak("What calculation do you want to perform? Please say your expression.")
    expression = listen()
    
    try:
        result = eval(expression)
        speak(f"The result is {result}.")
        print(f"Result is :{result}")
        print(f"Jarvis: The result is {result}.")
    except Exception as e:
        speak("There was an error with your calculation.")
        print(f"Jarvis: There was an error with your calculation. {e}")

def create_text_file():
    speak("What should I name the text file?")
    filename = listen() + ".txt"
    
    with open(filename, "w") as file:
        speak("What content do you want to write in the file?")
        content = listen()
        file.write(content)
    
    speak(f"I have created the file {filename} with your content.")

def view_datetime():
    current_time = datetime.datetime.now()
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
    speak(f"The current date and time is {formatted_time}.")
    print(f"Jarvis: The current date and time is {formatted_time}.")

def set_timer():
    speak("How many seconds do you want to set the timer for?")
    timer_seconds = listen()
    
    if timer_seconds.isdigit():
        timer_seconds = int(timer_seconds)
        speak(f"Setting a timer for {timer_seconds} seconds.")
        time.sleep(timer_seconds)
        speak("Time's up! The timer has finished.")
        print("Jarvis: Time's up! The timer has finished.")
    else:
        speak("Please say a valid number.")
def truth_and_dare():
    speak("Welcome to the Truth and Dare game!")
    
    speak("How many players are playing the game? Please Type ")
    num_players= input(":").strip()
    players = []

    num_players=int(num_players)
    for i in range(num_players):
        speak(f"Player {i+1}, what is your name?")
        print(f"Player {i+1}, please enter your name:")
        player_name = listen()
        players.append(player_name)
    player = random.choice(players)
    speak(f"{player}, it's your turn!")
    print(f"{player}, it's your turn!")
    def ch(player):
      speak(f"{player}, would you like to choose truth or dare on your own, or would you like Jarvis to help you?")
      print(f"{player}, do you want help from Jarvis? (yes/no)")
    
      choice = listen().lower()
            
      if "yes" in choice:
            speak("Jarvis is helping you choose. Let's pick a random truth or dare!")
            print(f"Jarvis is helping {player}...")
            
            speak("Jarvis gives you two options: truth or dare. Please choose one.")
            print("Choose 'truth' or 'dare'.")
            
            player_choice = listen().lower()

            if "truth" in player_choice:
                truth_questions = [
                    "What is your biggest fear?",
                    "What is the most embarrassing thing you've ever done?",
                    "What is your most awkward moment?",
                    "What is something you’ve never told anyone?"
                ]
                question = random.choice(truth_questions)
                speak(f"Your truth question is: {question}")
                print(f"Truth: {question}")

                answer = listen()
                result = f"{player} answered: {answer}"

            elif "dare" in player_choice:
                dare_challenges = [
                    "Do 10 pushups.",
                    "Dance for 30 seconds.",
                    "Act like a monkey for one minute.",
                    "Sing a song loudly.",
                    "Do an impression of someone you know."
                ]
                challenge = random.choice(dare_challenges)
                speak(f"Your dare is: {challenge}")
                print(f"Dare: {challenge}")

                response = listen().lower()
                if "done" in response:
                    result = f"{player} completed the dare: {challenge}"
                else:
                    result = f"{player} skipped the dare: {challenge}"

            else:
                speak("Invalid choice. Please choose 'truth' or 'dare'.")
                print(f"{player}, please choose 'truth' or 'dare'.")
                return
            with open("truth_and_dare_log.txt", "a") as file:
                file.write(f"{datetime.datetime.now()} - {player} chose: {player_choice if 'truth' in player_choice or 'dare' in player_choice else 'truth or dare'} - {result}\n")
                speak(f"I have saved your response, {player}")
      else:
            speak(f"Alright, {player}, make your choice. Truth or dare? , And complete this Round Without me ")
            s(20)
            speak("If this ROund is Completed then Shall be begin ..")
            c=listen().lower()
            if c=="yes":
                pass
            else :
                command=listen().lower()
    ch(player)            
    

def main():
    name = login()
    menu()
    speak("Listening.....")
    while True:
        
        command = listen().lower()
        
        if "open google" in command:
            webbrowser.open("https://www.google.com")
            speak("Opening Google.")
        elif "open facebook" in command:
            webbrowser.open("https://www.facebook.com")
            speak("Opening Facebook.")
        elif "open instagram" in command:
            webbrowser.open("https://www.instagram.com")
            speak("Opening Instagram.")
        elif "open youtube" in command:
            webbrowser.open("https://www.youtube.com")
            speak("Opening YouTube.")
        elif "open email" in command:
            webbrowser.open("https://www.gmail.com")
            speak("Opening Email.")
        elif "open twitter" in command:
            webbrowser.open("https://www.twitter.com")
            speak("Opening Twitter.")
        elif "open reddit" in command:
            webbrowser.open("https://www.reddit.com")
            speak("Opening Reddit.")
        elif "search on google" in command:
            search_google()
        elif "search on youtube" in command:
            search_youtube()
        elif "play music" in command:
            speak("What song do you want to play?")
            song_name = listen()
            webbrowser.open(f"https://www.youtube.com/results?search_query={song_name}")
            speak(f"Playing {song_name} on YouTube.")
        elif "truth and dare" in command:
            speak("Let's play Truth and Dare! .")
            truth_and_dare()
        elif "chat with me" in command:
            chat()
        elif "play a number guessing game" in command:
            number_guessing_game()
        elif "solve a riddle" in command:
            solve_riddle()
        elif "play rock paper scissors" in command:
            play_rock_paper_scissors()
        elif "take a quiz" in command:
            take_quiz()
        elif "calculate" in command:
            calculate()
            s(10)
        elif "create a new text file" in command:
            create_text_file()
        elif "view current date and time" in command:
            view_datetime()
        elif "set a timer" in command:
            set_timer()
        elif "open application" in command:
            open_application()
        elif "close application" in command:
            close_application()
        elif "show help" in command:
            speak("This is the help menu.")
            print("Help menu options...")
            menu()
        elif "about" in command:
            about()
        elif "exit" in command:
            speak("Goodbye! Have a great day!")
            break
        else:
            print("I'm sorry, I didn't understand that.")

    
if __name__ == "__main__":
    main()
