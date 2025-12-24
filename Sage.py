import speech_recognition as sr 
import pyttsx3
import logging
import os
import datetime
import wikipedia
import webbrowser
import random
import subprocess

LOGS_DIR = "logs"
LOG_FILE_NAME = "application.log"
os.makedirs(LOGS_DIR, exist_ok=True)
log_path = os.path.join(LOGS_DIR,LOG_FILE_NAME)
# print(log_path)

logging.basicConfig(
    filename=log_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# Activating voice from our system.

engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')       
engine.setProperty('voice', voices[0].id)
rate = engine.getProperty('rate')                           
engine.setProperty('rate', 175)  
volume = engine.getProperty('volume')                          
engine.setProperty('volume',1.0)

# Speak Function :

def speak(text) :

    """
      This function coverts text to voice.
      Args : text
      Returns : voice

    """
    engine.say(text)
    engine.runAndWait()



# This function recognize the speech and convert it to text

def Commands():

    """
       This function takes command and recognize

       Returns: Text as query
    """

    Command = sr.Recognizer()

    with sr.Microphone() as source :
       print("Sage is here......")
       speak("Sage is here")
       Command.pause_threshold = 1
       audio = Command.listen(source)
    
    try :
        print("Recognizing...")
        speak("Recognizing")
        query = Command.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
        return query

    except Exception as e:
        logging.info(e)
        print("Please say it again")
        speak("Please say it again")
        # return None

def Search():

    """
       This function takes command and recognize

       Returns: Text as query
    """

    Command = sr.Recognizer()

    with sr.Microphone() as source :
       print("What do you wanna search sir")
       speak("What do you wanna search sir?")
       Command.pause_threshold = 1
       audio = Command.listen(source)
    
    try :
        print("Recognizing...")
        speak("Recognizing")
        query = Command.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
        return query

    except Exception as e:
        logging.info(e)
        print("Please say it again")
        speak("Please say it again")
        # return None

def Select():

    """
       This function takes command and recognize

       Returns: Text as query
    """

    Command = sr.Recognizer()

    with sr.Microphone() as source :
       Command.pause_threshold = 1
       audio = Command.listen(source)
    
    try :
        print("Recognizing...")
        speak("Recognizing")
        query = Command.recognize_google(audio, language='en-in')
        print(f"User said : {query}\n")
        return query

    except Exception as e:
        logging.info(e)
        # return None


def GuessNumber() :
    
    x = random.choice(range(0,101))
    c = 7
    speak("Guess the number and type it It is between 1 to 100 You've gotten 7 chances")
    y=int(input("Guess the number and type it(It is between 1 to 100.You've gotten 7 chances):"))
    while True :

        if y > x :
            speak("Guessed number is greater than the real number")
            c-=1
        
        elif y < x :
            speak("Guessed number is less than the real number")
            c-=1
        
        elif y == x :
            speak("Huurah You've won the game")
            return None
        speak(f"You've gotten {c} chances")
        if c == 0 :
            break
        y=int(input(f"You've gotten {c} chances):"))
        
    speak("You've lost the game")
    return None


def play_audio() :
    music_dir = "C:\\SAGE-Voice-Assistant-System\\music"
    try :
        lis = os.listdir(music_dir)
        if lis :
            song = random.choice(lis)
            os.startfile(os.path.join(music_dir,song))
        else:
            speak("no song found")
    except Exception :
            speak("no directory found")

# Tic-Tac-Toe Game

import random

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([spot == player for spot in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def player_move(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if row not in range(3) or col not in range(3) or board[row][col] != " ":
                print("Invalid move, try again.")
                continue
            return row, col
        except ValueError:
            print("Please enter numbers only.")

def ai_move(board):
    # Simple AI: choose a random empty spot
    empty_spots = [(r, c) for r in range(3) for c in range(3) if board[r][c] == " "]
    return random.choice(empty_spots)

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)

        if current_player == "X":
            row, col = player_move(board)
        else:
            row, col = ai_move(board)
            print(f"AI chooses row {row}, column {col}.")

        board[row][col] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            break

        current_player = "O" if current_player == "X" else "X"

    print("Game over.")


# Greeting function :

def Greeting():

    time = datetime.datetime.now().hour

    if  6 <= time and time < 12:
        print("Good Morning sir")
        speak("Good Morning sir")

    elif  12 <= time and time <= 15:
        print("Good Noon sir")
        speak("Good Noon sir")
    
    elif  15 <= time and time <= 17:
        print("Good Afternoon sir")
        speak("Good Afternoon sir")

    elif  17 <= time and time <= 19:
        print("Good Evening sir")
        speak("Good Evening sir")
    
    else :
        print("Welcome sir...")
        speak("Welcome sir...")

Greeting()

while True :
   
    
    say = Commands()

    if say != None :
        say = say.lower()   
    else:
        continue

    if say == "exit":
        speak("Have a good day,sir.")
        logging.info("User asked to exit")
        break
        
    elif "your name" in say :
        speak("My name is Sage")
        logging.info("User asked name")

    elif say == "who created you" :
        speak("Yeaser Mustabi created me")
        logging.info("User asked creator name")

    elif say == "how are you" :
        speak("I'm fine what about you?")
        logging.info("User asked how am I")

    elif  "thank you" in say :
        speak("My pleasure sir")
        logging.info("User asked how am I")

    elif "time" in say :
        hour = datetime.datetime.now().hour
        munite = datetime.datetime.now().minute
        form = "am"
        if hour >= 12 :
            form = "pm"
        if hour > 12 :
            hour -= 12
        speak(f"It is {hour} {munite} {form}")
        print(f"It is {hour}:{munite} {form}")
        logging.info("User asked time")
    
    # Calculator
    elif "open calculator" in say :
        speak("Openning Claculator")
        print("Openning Claculator.....")
        subprocess.Popen("calc.exe")
        logging.info("User opened calculator")
    
    # Notepad 

    elif "open notepad" in say :
        speak("Openning Notepad")
        print("Openning Notepad.....")
        subprocess.Popen("notepad.exe")
        logging.info("User opened notepad")

    # Whatsapp 

    elif "open whatsapp" in say :
        speak("Openning Whatsapp")
        print("Openning Whatsapp.....")
        os.startfile("whatsapp://")
        logging.info("User opened whatsapp")


    # Command Promt
    elif "open command prompt" in say :
        speak("Openning Command Prompt")
        print("Openning Command Prompt.....")
        subprocess.Popen("cmd.exe",creationflags=subprocess.CREATE_NEW_CONSOLE)
        logging.info("User opened command prompt")
    
    # Google :
    elif "open google" in say :
        speak("Openning Google")
        print("Openning Google.....")
        say = Search()
        webbrowser.open(f"https://www.google.com/search?q={say}")
        logging.info("User opened google")

    # Wikipedia :
    elif "open wikipedia" in say :
        speak("Openning Wikipedia")
        print("Openning Wikipedia.....")
        say = Search()
        results = wikipedia.summary(say,sentences=10)
        speak("According to Wikipedia")
        speak(results)
        logging.info("User opened Wikipedia")

    # Youtube

    elif "open youtube" in say:
       speak("Opening YouTube")
       print("Opening YouTube.....") 
       say = Search()
       webbrowser.open(f"https://www.youtube.com/results?search_query={say}")
       logging.info("User opened YouTube")
    
    # Facebook

    elif "open facebook" in say:
        speak("Opening Facebook")
        print("Opening Facebook.....")
        os.startfile("https://www.facebook.com")
        logging.info("User opened Facebook")

    # Jokes

    elif "joke" in say:
        jokes = [
            "Why did the scarecrow get promoted? Because he was outstanding in his field.",
            "I told my dog to fetch a stick. He came back with a receipt.",
            "Why don’t eggs tell jokes? They’d crack up.",
            "I tried to be normal once. Worst two minutes of my life.",
            "Why did the math book look sad? Too many problems.",
            "I asked my mirror for advice. It just stared back.",
            "Why did the coffee file a police report? It got mugged.",
            "I’m on a seafood diet. I see food and I eat it.",
            "Why don’t skeletons fight each other? They don’t have the guts.",
            "I told my phone a joke. Now it won’t stop laughing at me.",
            "Why was the computer tired? It needed a rest.",
            "I wanted to lose weight, but it keeps finding me.",
            "Why did the bicycle fall over? It was two tired.",
            "I told my friend she drew her eyebrows too high. She looked surprised.",
            "Why did the student eat his homework? The teacher said it was a piece of cake.",
            "I tried to read a book on procrastination. I’ll finish it later.",
            "Why don’t some couples go to the gym? Because some relationships don’t work out.",
            "I asked the librarian if books about paranoia exist. She whispered, ‘They’re behind you.’",
            "Why did the tomato turn red? It saw the salad dressing.",
            "I don’t trust stairs. They’re always up to something.",
            "Why did the golfer bring two pairs of pants? In case he got a hole in one.",
            "I told my shadow a joke. It followed me everywhere laughing.",
            "Why was the calendar afraid? Its days were numbered.",
            "I tried exercise, but I kept losing my balance… on the couch.",
            "Why don’t oysters donate to charity? Because they are shellfish.",
            "I started a diet, but my fridge keeps calling me.",
            "Why did the chicken join a band? Because it had the drumsticks.",
            "I talk to myself because sometimes I need expert advice.",
            "Why was the math teacher late? She took the wrong angle.",
            "I bought a belt made of watches. It was a waist of time.",
            "Why don’t cows have social media? Too many mooo-d swings.",
            "I told my bed a joke. It hasn’t let me go since.",
            "Why did the cookie go to the doctor? It felt crummy.",
            "I tried to be productive today. Tomorrow sounds better.",
            "Why did the picture go to jail? It was framed.",
            "I gave up on learning how to cook. Smoke alarm won.",
            "Why did the banana go to the doctor? It wasn’t peeling well.",
            "I tried yoga. Turns out falling asleep is my pose.",
            "Why don’t elephants use computers? They’re afraid of the mouse.",
            "I asked my wallet for money. It laughed.",
            "Why was the stadium so cool? It was full of fans.",
            "I cleaned my room once. Never found it again.",
            "Why did the man run around his bed? To catch up on sleep.",
            "I told my alarm clock a joke. It ignored me.",
            "Why did the shoe go to school? To become smarter.",
            "I tried to eat healthy, but pizza understood me better.",
            "Why was the broom late? It swept in.",
            "I opened the fridge to think. Didn’t help, but snacks did.",
            "Why did the kid bring a ladder to school? To go to high school.",
            "I wanted to be organized, but chaos chose me.",
            "Why did the orange stop rolling? It ran out of juice.",
            "I tried to save money, but it escaped.",
            "Why was the belt arrested? It was holding up pants.",
            "I don’t need a therapist. I have my pillow.",
            "Why did the music teacher need a ladder? To reach the high notes.",
            "I told my brain to focus. It went on vacation.",
            "Why did the candle stop working? It burned out.",
            "I tried to wake up early. My bed said no.",
            "Why did the clock get kicked out of class? It kept ticking.",
            "I asked my phone for motivation. It suggested sleep.",
            "Why did the sandwich go to therapy? Too much filling inside.",
            "I cleaned my phone screen. Still blurry life.",
            "Why did the student bring string to school? To tie up loose ends.",
            "I tried to think positive. My bank account disagreed.",
            "Why was the math problem afraid? It knew it had no solution.",
            "I tried to be on time. Time wasn’t ready.",
            "Why did the pillow look tired? It was overworked.",
            "I don’t argue. I explain loudly.",
            "Why did the door feel proud? It had good handles on life.",
            "I planned to do nothing today. Still busy.",
            "Why did the chair sit quietly? It didn’t want to make a scene.",
            "I tried multitasking. Now I’m tired twice.",
            "Why did the ice cream cry? It melted under pressure.",
            "I told my shoes to run. They refused.",
            "Why did the student bring sunglasses to class? Too bright ideas.",
            "I tried to relax. My thoughts didn’t.",
            "Why did the pillow break up with the blanket? Too clingy.",
            "I asked my future for answers. It said ‘loading’.",
            "Why did the notebook feel important? It had many pages.",
            "I woke up early today. By accident.",
            "Why did the fridge look happy? It was full.",
            "I tried to plan my life. Life laughed.",
            "Why did the spoon feel useless? No one stirred things up.",
            "I smiled today. My face was confused.",
            "Why did the shoe feel confident? It had good support."
        ]

        joke = random.choice(jokes)
        print(joke)
        speak(joke)

    
    # Game

    elif "play a game" in say:
        speak("What game would you like to play sir 1) Guess the number 2) Tic-Tac-Toe")
        print("""What game would you like to play sir?\n
                 1) Guess the number\n
                 2) Tic-Tac-Toe""")
        
        say = Select()

        if say in ['one','guess','guess the','guess the number','the','the number','number',"guess number"] :
            GuessNumber()
            logging.info("User plays game")

        elif say in ['two','tic','tic-tac','tic-tac-toe','tac','tac-toe','toe','tic-toe'] :
            tic_tac_toe()
            logging.info("User plays game")

        else :
            speak("Wrong selection sir")
    
    # Play Ausdio
    
    elif say in ["play music","play a song","play song"]:
        speak("Playing Music")
        play_audio()
        logging.info("User plays music")
    



    # Google Calendar

    elif "open calendar" in say:
       speak("Opening Google Calendar")
       print("Opening Google Calendar.....")
       webbrowser.open("https://calendar.google.com")
       logging.info("User opened Google Calendar")


    # Telegram
    elif "open telegram" in say :
        speak("Openning telegram")
        print("Openning telegram.....")
        os.startfile("tg://")
        logging.info("User opened telegram")


    # Github
    elif "open github" in say :
        speak("Openning Github")
        print("Openning Github.....")
        webbrowser.open("github.com")
        logging.info("User opened Github")

    # Linkedin
    elif "open linkedin" in say :
        speak("Openning Linkedin")
        print("Openning Linkedin.....")
        os.startfile("Linkedin://")
        logging.info("User opened Linkedin")

    # Date

    elif "date" in say :
        day = datetime.datetime.now().date
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

        months = [
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        
        if day == 1 :
            day = str(day) + "st"
        elif day == 2 :
            day = str(day) + "nd"
        elif day == 3 :
            day = str(day) + "rd"
        else :
            day = str(day) + "th"

        print(f"Today is {day} {months[month-1]} {year} .....")
        speak(f"Today is {day} {months[month-1]} {year} .....")
        
        logging.info("User opened Linkedin")
    
    else :
        speak("Sorry sir I can't help you with that")
    