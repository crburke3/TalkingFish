import nltk

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
                    mouthPosition = mouthPosition + ':1'
                elif sound[-1] == '1':
                    mouthPosition = mouthPosition + ':4'
                else:
                    mouthPosition = mouthPosition + ':3'
            else:
                mouthPosition = mouthPosition + ':2'
            oAndC.append(mouthPosition)

        return oAndC

    def convertTextToCommands(self, text: str):
        phoneticBreakdown = TextToCommands.phoneticBreakdown(text)
        print("Phonetic breakdown: " + str(phoneticBreakdown))
        commands = TextToCommands.convertToOandC(phoneticBreakdown)
        print("Open/Close + durations: " + str(commands))
        return str(commands)


