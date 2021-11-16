import nltk
import time
import string
from gtts import gTTS
import os
from pygame import mixer
from mutagen.mp3 import MP3
from structs import server_globals

class TextToCommands:

    # deconstruct a string into arpabet transcription codes
    def phoneticBreakdown(sentence):
        nltk.download('cmudict')
        arpabet = nltk.corpus.cmudict.dict()
        result = []
        out = []
        for word in (sentence.lower().split()):
           result.append(arpabet[word])
        array_length = len(result)

        for x in range(0, array_length):
            word_length = len(result[x][0])
            for y in range(0, word_length):
               out.append(result[x][0][y])
        return out

    # Converts the phoentics into an array of 2 character strings
    #  The first character is an O or a C indicating whether the mouth is open or closed
    #  The second character is a number indicatring how long the mouth should remain in that position
    def convertToOandC(phoentics):
        oAndC = []
        for sound in phoentics:
            mouthPosition = ""
            # Open mouth sounds (vowels)
            if sound[:2] in ('AA', 'AE', 'AH', 'AO', 'AW', 'AX', 'AY', 'EH', 'ER', 'EY', 'IH', 'IX', 'IY', 'OW', 'OY', 'UH', 'UW', 'UX'):
                mouthPosition = "O"
            else:
                mouthPosition = "C"

            # Check the last character for a number indicating stress:
            #   0: no stress
            #   <no number>: neutral stress
            #   1: primary stress
            #   2: secondary stress
            if sound[-1].isnumeric():
                if sound[-1] == '0':
                    mouthPosition = mouthPosition + '1'
                elif sound[-1] == '1':
                    mouthPosition = mouthPosition + '4'
                else:
                    mouthPosition = mouthPosition + '3'
            else:
                mouthPosition = mouthPosition + '2'
            oAndC.append(mouthPosition)

        return oAndC

    # Generate an audio file for the given senetence and return the length of the audio file in seconds
    def textToSpeach(sentence):
        mixer.init()
        soundObj = gTTS(text=sentence, lang='en', slow=False)
        soundObj.save("sentence.mp3")
        audio = MP3("sentence.mp3")
        mixer.music.load("sentence.mp3")
        mixer.music.play()
        return audio.info.length

    # Returns the total amount of time of each open and closed position
    def getTotalMovementTime(oAndC):
        totalTime = 0
        for position in oAndC:
            totalTime = totalTime + int(position[-1])
        return totalTime

    def saySentence(sentence, oAndC):
        # Subtrack 0.5 seconds from audio length to account for dead time
        audioLength = TextToCommands.textToSpeach(sentence) - 0.5
        totalTime = TextToCommands.getTotalMovementTime(oAndC)
        interval = audioLength/totalTime
        for position in oAndC:
            if position[0] == 'C':
                print("Closed")
            if position[0] == 'O':
                print("Open")
            time.sleep(int(position[-1]) * interval)

    def convertTextToCommands(text: str):
        text = text.translate(str.maketrans('', '', string.punctuation))
        phoneticBreakdown = TextToCommands.phoneticBreakdown(text)
        print("Phonetic breakdown: " + str(phoneticBreakdown))
        commands = TextToCommands.convertToOandC(phoneticBreakdown)
        print("Open/Close + durations: " + str(commands))
        return str(commands)


