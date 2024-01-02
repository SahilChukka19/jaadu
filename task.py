import datetime
from logging.config import listen
import cv2
from speak import speak
import mediapipe as mp
import pyautogui
import pyjokes
import wikipedia
import pywhatkit
import smtplib as s
from keyboard import *





def Time():
    time = datetime.datetime.now().strftime("%H:%M")
    speak(time)

def Date():
    date = datetime.date.today()
    speak(date)

def Day():
    day = datetime.datetime.now().strftime("%A")
    speak(day)

def joke():
    jokes = pyjokes.get_joke()
    speak(jokes)

def screenshot():
    press_and_release('windows + SHIFT + s')

def eye_cursor():
    cam = cv2.VideoCapture(0)
    face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
    screen_w, screen_h = pyautogui.size()
    while True:
        _, frame = cam.read()
        frame = cv2.flip(frame, 1)
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        output = face_mesh.process(rgb_frame)
        landmark_points = output.multi_face_landmarks
        frame_h, frame_w, _ = frame.shape
        if landmark_points:
            landmarks = landmark_points[0].landmark
            for id, landmark in enumerate(landmarks[474:478]):
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 0))
                if id == 1:
                    screen_x = screen_w * landmark.x
                    screen_y = screen_h * landmark.y
                    pyautogui.moveTo(screen_x, screen_y)
            left = [landmarks[145], landmarks[159]]
            for landmark in left:
                x = int(landmark.x * frame_w)
                y = int(landmark.y * frame_h)
                cv2.circle(frame, (x, y), 3, (0, 255, 255))
            if (left[0].y - left[1].y) < 0.004:
                pyautogui.click()
                pyautogui.sleep(1)
        cv2.imshow('Eye Controlled Mouse', frame)
        cv2.waitKey(1)


def NonInputExecution(query):
    query = str(query)

    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
    elif "cursor" in query:
        eye_cursor()
    elif "joke" in query:
        joke()
    elif "screenshot" in query:
        screenshot()


#INPUT
def sendEmail(to, content):
    server = s.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('ella.ai.bot@gmail.com', 'hmgnwqyzdzstlovh')
    server.sendmail("ella.ai.bot@gmail.com", to, content)
    server.close()


def InputExecution(tag,query):
    if "wikipedia" in tag:
        try:
            name = str(query).replace("who is","").replace("about","").replace("wikipedia","")
            result  = wikipedia.summary(name, sentences = 4)
            speak(result)
        except:
            speak("Didn't get that")
        
    elif "google" in tag:
        query = str(query).replace("google","")
        query = query.replace("search","")
        pywhatkit.search(query)

    elif 'email' in tag:
        try:
            speak("what should i send")
            content = listen()
            to = ['sahil.chukka@gmail.com','vjagtap20ite@student.mes.ac.in','pmane20ite@student.mes.ac.in']
            sendEmail(to, content)
            speak("Email has been sent!!!")
        except Exception as e:
                print(e)
    
    elif "play" in tag:
        query = str(query).replace("play","")
        pywhatkit.playonyt(query)
    