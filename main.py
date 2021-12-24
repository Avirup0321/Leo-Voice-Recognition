import pyttsx3 #pip install pyttsx3
import speech_recognition as sr  #pip install speechRecognition
import datetime
import wikipedia    
# import os
# import smtplib
import webbrowser 

print ("Initializing Leo")
MASTER="Avirup"


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)

# Speak function will pronounce the string which is passed to it
def speak(text):
    engine.say(text)
    engine.runAndWait()

def wishMe():           #step1 it will wish you as per the current time 

    hour = int(datetime.datetime.now().hour)
    

    if hour >=0 and hour <12:
        speak("Good Morning" +MASTER)
    elif hour>=13 and hour<18:
        speak("Good Afternoon") 
    else:
        speak("Good Evening" +MASTER)
    

    speak("How May I help You?")

def takecommand(): #this will take command from user
    r=sr.Recognizer()
    with sr.Microphone()  as source:
        print("Listening....")
        audio = r.listen(source)


    try :
        print("recognizing...")
        query = r.recognize_google(audio,language='en-in')
        print(f"user Said: {query}\n")
    
    except Exception as e:
        speak("can you please repeat")
        query = r.recognize_google(audio,language='en-in')
    return query

def main():
    speak ("Initializing Leo....")
    wishMe()
    query = takecommand()

    if 'wikipedia' in query.lower():
        speak ('Searching wikipedia...')
        query = query.replace('wikipedia',"")
        result = wikipedia.summary(query, sentences =2)
        print(result)
        speak(result)

    elif 'youtube' in query.lower():
        #  webbrowser.open("youtube.com")
        webbrowser.open('https://www.youtube.com', new=1)

    elif 'facebook' in query.lower():
        webbrowser.open('https://www.facebook.com', new=1)

    elif 'instagram' in query.lower():
        webbrowser.open('https://www.instagram.com', new=1)

    elif 'twitter' in query.lower():
        webbrowser.open('https://twitter.com', new=1)

    elif 'linkedin' in query.lower():
        webbrowser.open("https://www.linkedin.com/",new=1)

    elif 'music' in query.lower():
        webbrowser.open('https://music.youtube.com/',new=1)

    elif 'the time' in query.lower():
        strTime = datetime.datetime.now().strftime("%H:%M")
        speak(f"Its almost{strTime}.... ")

    elif 'vs code' in query.lower():
        webbrowser.open('https://vscode.dev/',new=1)

    elif 'gmail' in query.lower():
        webbrowser.open('https://mail.google.com/mail',new=1)

    elif 'google.com' or 'google' in query.lower():
        webbrowser.open("https://www.google.co.in",new=1)
main()

