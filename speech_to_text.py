import speech_recognition as sr
def main():
    sound="sampleaudio.wav"
    r=sr.Recognizer()
    with sr.AudioFile(sound) as source:
        r.adjust_for_ambient_noise(source)
        print("Converting Audio File To Text... ")
        audio=r.record(source)
        try:
            print("Converting Audio Is : \n " + r.recognize_google(audio))
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

