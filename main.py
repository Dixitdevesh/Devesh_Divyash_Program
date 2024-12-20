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
    print("=" * 70)
    print("🤖 Jarvis AI Menu 🤖".center(70))
    print("Presented in Kanha Makhan Public School".center(70))
    print("Created by: Devesh Dixit (Roll No: ___)".center(70))
    print("Assisted by: Divyash Singh (Roll No: ___)".center(70))
    print("=" * 70)

    print("\n📊 **Web Browsing & Search** 📊")
    print("1. Google 🌐 | 2. Facebook 👥 | 3. Instagram 📸 | 4. YouTube 📺")
    print("5. Email 📧 | 6. Twitter 🐦 | 7. Reddit 📖 | 8. Search Google 🔍")
    print("9. Search YouTube 🎥")
    
    print("\n🎵 **Entertainment** 🎵")
    print("10. Music 🎶 | 11. Chat 💬 | 12. Number Game 🎲 | 13. Riddle 🧩")
    print("14. Rock-Paper ✊ | 15. Quiz 📝")
    
    print("\n📈 **Productivity Tools** 📈")
    print("16. Calculate 📝 | 17. Create File 📄 | 18. Date & Time 🕒")
    print("19. Set Timer ⏳")
    
    print("\n📊 **Applications** 📊")
    print("20. Open App 🖥️ | 21. Close App ❌")
    
    print("\n🤔 **Help & About** 🤔")
    print("22. Help | 23. About Jarvis")
    
    print("\n👋 **Exit** 👋")
    print("99. Exit Jarvis")
    print("=" * 70) 



def about():
    print("\n" + "="*30)
    print("  About Jarvis")
    print("="*30)
    print("  Created by: Devesh Dixit")
    print("  Assisted by: Divyansh Singh")
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
