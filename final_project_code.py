import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import pyjokes
import pywhatkit
import time
import ctypes

engine = pyttsx3.init('sapi5')
engine.setProperty('voice', engine.getProperty('voices')[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")  

    speak("I am Genius . Please tell me how may I help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    my_email = open("email.txt").readline()
    my_password = open("password.txt").readline()
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(my_email,my_password)
    server.sendmail(my_email , to, content)
    server.close()

def timer(h,m,s): 
    if h==0 and  m==0 :
        while s>=0 :
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
            print(timer, end="\r")
            time.sleep(1)
            s -= 1
    elif h==0 and m>0 :
        while s>=0:
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
            print(timer, end="\r")
            time.sleep(1)
            s -= 1
            if s<0 and m >0:
                s += 60
                m -= 1
    elif h>0 :
        while s>=0:
            timer = '{:02d}:{:02d}:{:02d}'.format(h, m, s)
            print(timer, end="\r")
            time.sleep(1)
            s -= 1
            if s<0 and m >0:
                s += 60
                m -= 1
            elif s<0 and m==0 and h>0:
                s += 60
                m += 59
                h -= 1
                
    print('Time up !!') 
    speak('Time up !!') 


if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'tell about' in query or 'tell me about' in query or 'tell' in query:
            speak('Searching...')
            query = query.replace("tell about", "")
            query = query.replace("tell", "")
            query = query.replace("tell me about", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to my database")
                print(results)
                speak(results)
            except Exception as e:
                speak("No such result is found !!")
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")
        
        elif 'open iit roorkee' in query:
            webbrowser.open("iitr.ac.in")

        elif 'joke' in query:
            jokes = pyjokes.get_joke()
            print(jokes)
            speak(jokes)

        elif 'play' in query:
            song = query.replace('play','')
            speak('playing ' + song)
            pywhatkit.playonyt(song)

        elif 'music' in query:
            music_dir = 'C:\\Users\\Ashwani Kumar\\Music'
            songs = os.listdir(music_dir) 
            os.startfile(os.path.join(music_dir, songs[1]))

        elif 'time' in query:
            Time = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {Time}")

        elif 'date' in query:
            Date = datetime.datetime.now().strftime("%A:%d:%B:%Y")
            speak(f"Sir, the date is {Date}")
        
        elif 'open powerpoint' in query:
            codePath = "C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE"
            os.startfile(codePath)

        elif 'email' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = input("Enter email id : ")
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                speak("Sorry, I am not able to send this email")    
        
        elif 'news' in query:
            news = webbrowser.open_new_tab("https://timesofindia.indiatimes.com/home/headlines")
            speak('Here are some headlines from the Times of India... , Happy Reading')
            time.sleep(5)

        elif 'set' in query:
            speak("Enter hours")
            HOUR = int(input("Enter hours : ")) 
            speak("Enter minutes")
            MIN = int(input("Enter minutes : ")) 
            speak("Enter seconds")
            SEC = int(input("Enter seconds : ")) 
            print("\n")
            timer(HOUR,MIN,SEC)




        elif 'protein' in  query:
            mydict ={
                    "UUU":"Phenylalanine",
                    "UUC":"Phenylalanine",
                    "UUA":"Leucine",
                    "UUG":"Leucine",
                    "CUU":"Leucine",
                    "CUC":"Leucine",
                    "CUA":"Leucine",
                    "CUG":"Leucine",
                    "AUG":"Methionine",
                    "AUU":"Isoleucine",
                    "AUC":"Isoleucine",
                    "AUA":"Isoleucine",
                    "GUU":"Valine",
                    "GUC":"Valine",
                    "GUA":"Valine",
                    "GUG":"Valine",
                    "UCU":"Serine",
                    "UCC":"Serine",
                    "UCA":"Serine",
                    "UCG":"Serine",
                    "CCU":"Proline",
                    "CCC":"Proline",
                    "CCA":"Proline",
                    "CCG":"Proline",
                    "ACU":"Threonine",
                    "ACC":"Threonine",
                    "ACA":"Threonine",
                    "GCU":"Alanine",
                    "GCC":"Alanine",
                    "GCA":"Alanine",
                    "GCG":"Alanine",
                    "UAU":"Tyrosine",
                    "UAC":"Tyrosine",
                    "CAU":"Histidine",
                    "CAC":"Histidine",
                    "CAA":"Glutamine",
                    "CAG":"Glutamine",
                    "AAU":"Asparagine",
                    "AAC":"Asparagine",
                    "AAA":"Lysine",
                    "AAG":"Lysine",
                    "GAU":"Aspartic Acid",
                    "GAC":"Aspartic Acid",
                    "GAA":"Glutamic Acid",
                    "GAG":"Glutamic Acid",
                    "UGU":"Cystine",
                    "UGC":"Cystine",
                    "UGG":"Tryptophan",
                    "CGU":"Arginine",
                    "CGC":"Arginine",
                    "CGA":"Arginine",
                    "CGG":"Arginine",
                    "AGU":"Serine",
                    "AGC":"Serine",
                    "AGA":"Arginine",
                    "AGG":"Arginine",
                    "GGU":"Glycine",
                    "GGC":"Glycine",
                    "GGA":"Glycine",
                    "GGG":"Glycine"}
            speak("type total number of codon")
            n = int(input("TOTAL NUMBER OF CODONS : "))
            i=0
            c=[]
            while (i<n) :
                i=i+1
                speak("what do you want; speak ,or type")
                cod = takeCommand()
                if 'speak' in cod:
                    print('SPEAK NUCLEOTIDE SEQUENCE NUMBER '+ str(i))
                    speak("speak your codon")
                    codon_s1 = takeCommand().upper().strip()
                    codon_s = codon_s1.replace(" ","")

                    if codon_s in mydict:
                        print('THE AMINO ACID FORMED BY THIS NUCLEOTIDE SEQUENCE IS :\t '+ mydict.get(codon_s))
                        speak(f'THE AMINO ACID FORMED BY THIS NUCLEOTIDE SEQUENCE is {mydict.get(codon_s)}')
                        c.append(mydict.get(codon_s))
                        if n>1:
                            print("WHAT DO YOU WANT \'THE DEFINITION OF ABOVE AMINO ACID\' OR \'WANT TO GIVE NEW COMMAND\' OR \'SEARCH FOR NEXT CODON SEQUENCE\'")
                            speak("WHAT YOU WANT; THE DEFINITION OF ABOVE AMINO ACID, OR WANT TO GIVE NEW COMMAND, OR SEARCH FOR NEXT CODON SEQUENCE")
                            def_newcom_s = takeCommand()
                            if 'definition' in def_newcom_s:
                                definition = wikipedia.summary(mydict.get(codon_s), sentences=2)
                                print(definition)
                                speak(definition)
                            elif 'command' in def_newcom_s:
                                break
                            elif 'sequence' or 'codon' in def_newcom_s:
                                pass
                        elif n==1:
                            print("WHAT DO YOU WANT \'THE DEFINITION OF ABOVE AMINO ACID\' OR \'WANT TO GIVE NEW COMMAND\'")
                            speak("WHAT YOU WANT; THE DEFINITION OF ABOVE AMINO ACID, OR WANT TO GIVE NEW COMMAND")
                            def_newcom_s = takeCommand()
                            if 'definition' in def_newcom_s:
                                definition = wikipedia.summary(mydict.get(codon_s), sentences=2)
                                print(definition)
                                speak(definition)
                            elif 'command' in def_newcom_s:
                                break
                    elif codon_s == "UGA" or "UAG" or "UAA":
                        print('THIS IS A STOP CODON')
                        speak('This is a stop codon')
                        c.append("Stop")
                        if n>1:
                            print("WHAT DO YOU WANT \'THE DEFINITION OF ABOVE AMINO ACID\' OR \'WANT TO GIVE NEW COMMAND\' OR \'SEARCH FOR NEXT CODON SEQUENCE\'")
                            speak("WHAT YOU WANT; THE DEFINITION OF ABOVE AMINO ACID, OR WANT TO GIVE NEW COMMAND, OR SEARCH FOR NEXT CODON SEQUENCE")
                            def_newcom_s = takeCommand()
                            if 'definition' in def_newcom_s:
                                definition = ''' In molecular biology (specifically protein biosynthesis),a stop codon
 (or termination codon) is a codon (nucleotide triplet within messenger RNA) 
 that signals the termination of the translation process of the current protein.'''
                                print(definition)
                                speak(definition)
                            elif 'command' in def_newcom_s:
                                break
                            elif 'sequence' or 'codon' in def_newcom_s:
                                pass
                        elif n==1:
                            print("WHAT DO YOU WANT \'THE DEFINITION OF ABOVE AMINO ACID\' OR \'WANT TO GIVE NEW COMMAND\'")
                            speak("WHAT YOU WANT; THE DEFINITION OF ABOVE AMINO ACID, OR WANT TO GIVE NEW COMMAND")
                            def_newcom_s = takeCommand()
                            if 'definition' in def_newcom_s:
                                definition = ''' In molecular biology (specifically protein biosynthesis),a stop codon
 (or termination codon) is a codon (nucleotide triplet within messenger RNA) 
 that signals the termination of the translation process of the current protein.'''
                                print(definition)
                                speak(definition)
                            elif 'command' in def_newcom_s:
                                break
                    else:
                        print('THIS IS NOT A CODON')
                else:
                    speak("Enter your codon here")
                    codon_w =( input("Enter your codon here: " ))
                    if codon_w in mydict:
                        print('THE AMINO ACID FORMED BY THIS NUCLEOTIDE SEQUENCE IS :\t '+ mydict.get(codon_w))
                        speak(f'THE AMINO ACID FORMED BY THIS NUCLEOTIDE SEQUENCE is {mydict.get(codon_w)}')
                        c.append(mydict.get(codon_w))
                        if n>1:
                            def_newcom_w = int(input('''WHAT YOU WANT 
                            \'THE DEFINITION OF ABOVE AMINO ACID\'  --  ENTER 1
                            \'WANT TO GIVE NEW COMMAND\'  --  ENTER 2
                            \'SEARCH FOR NEXT CODON SEQUENCE\'  --  ENTER 3\n'''))
                            if def_newcom_w == 1:
                                definition = wikipedia.summary(mydict.get(codon_w), sentences=2)
                                print(definition)
                                speak(definition)
                            elif def_newcom_w == 2:
                                break   
                            elif def_newcom_w == 3:
                                pass
                        elif n==1:
                            def_newcom_w = int(input('''WHAT YOU WANT 
                            \'THE DEFINITION OF ABOVE AMINO ACID\'  --  ENTER 1
                            \'WANT TO GIVE NEW COMMAND\'  --  ENTER 2\n'''))
                            if def_newcom_w == 1:
                                definition = wikipedia.summary(mydict.get(codon_w), sentences=2)
                                print(definition)
                                speak(definition)
                            elif def_newcom_w == 2:
                                break   
                    elif codon_w == "UGA" or "UAG" or "UAA":
                        print('THIS IS A STOP CODON')
                        speak('This is a stop codon')
                        c.append("Stop")
                        if n>1:
                            def_newcom_w = int(input('''WHAT YOU WANT 
                            \'THE DEFINITION OF ABOVE AMINO ACID\'  --  ENTER 1
                            \'WANT TO GIVE NEW COMMAND\'  --  ENTER 2
                            \'SEARCH FOR NEXT CODON SEQUENCE\'  --  ENTER 3\n'''))
                            if def_newcom_w == 1:
                                definition = ''' In molecular biology (specifically protein biosynthesis),a stop codon
 (or termination codon) is a codon (nucleotide triplet within messenger RNA) 
 that signals the termination of the translation process of the current protein.'''
                                print(definition)
                                speak(definition)
                            elif def_newcom_w == 2:
                                break   
                            elif def_newcom_w == 3:
                                pass
                        elif n==1:
                            def_newcom_w = int(input('''WHAT YOU WANT 
                            \'THE DEFINITION OF ABOVE AMINO ACID\'  --  ENTER 1
                            \'WANT TO GIVE NEW COMMAND\'  --  ENTER 2\n'''))
                            if def_newcom_w == 1:
                                definition = ''' In molecular biology (specifically protein biosynthesis),a stop codon
 (or termination codon) is a codon (nucleotide triplet within messenger RNA) 
 that signals the termination of the translation process of the current protein.'''
                                print(definition)
                                speak(definition)
                            elif def_newcom_w == 2:
                                break   

                    else:
                        print('THIS IS NOT A CODON')

            speak("PROTEIN formed by The following codon sequence would consist these AMINO ACIDS")
            print("\nPROTEIN formed by The following codon sequence would consist these AMINO ACIDS:- \n")
            j = 0
            while j < len(c):
                print(c[j],"-",end=" ")
                j += 1
            print("\n")


        elif 'write a note' in query:
            speak("On which name do I save the file")
            note_name = takeCommand()
            file = open(note_name, 'w')
            speak("Sir, Should i include date and time")
            in_dt_or_not = takeCommand()
            speak("What should I write, sir")
            note = takeCommand()
            if 'yes' or 'sure' or 'ofcourse' in in_dt_or_not:
                note_time = datetime.datetime.now().strftime("%H:%M:%S")    
                file.write(note_time)
                file.write(" :- ")
                file.write(note)
                speak("noted, sir")
            else:
                file.write(note)
                speak("noted, sir")
       
        elif "restart" in query:
            speak("Hold On a Second ! Your system is on its way to restart")
            os.system("shutdown /r /t 1")
            exit()

        elif 'shutdown' in query:
            speak("Hold On a Second ! Your system is on its way to shut down")
            os.system("shutdown /s /t 1")
            exit()

        elif 'lock window' in query:
            speak("locking the device")
            ctypes.windll.user32.LockWorkStation()
            exit()

        elif 'thank you' in query or 'exit' in query or 'close' in query:
            speak("Thanks for giving me your time")
            exit()