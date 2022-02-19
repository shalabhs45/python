from typing import List

class TextJustification:
 
    def fullJustify(self, wordList: List[str], length: int) -> List[str]:
        lineList = [] #Array of strings  
        currLine = [] #Array for current words 
        currLength = 0 
        wordIndex = 0
        print(wordList) 
        while wordIndex < len(wordList):
            word = wordList[wordIndex] 
            print (" procesing word ", word)
            if(len(word)+currLength <= length): #Can add the word 
                if(len(word)+currLength+1 <= length): #Can add a space to word (1)
                    currLine.append(word+" ")
                    currLength += len(word)+1
                    print (" procesing currLine ", currLine)
                    print (" procesing currLength ", currLength)
                else: #Cannot add a space and only word. 
                    currLine.append(word)
                    currLength += len(word)
                    print (" procesing currLine ", currLine)
                    print (" procesing currLength ", currLength)
                wordIndex += 1 
                print (" procesing wordIndex ", wordIndex)
            else: 
                spaces = length - currLength       #Amount of extra spaces available
                print (" procesing spaces ", spaces)
                index = 0
                if(currLine[-1][-1] == " "): #Case where line ends in space due to condition (1) above . Should remove that space. 
                    print  (" procesing current line before trimming ", currLine)
                    currLine[-1] = currLine[-1][:-1]
                    print  (" procesing current line after trimming ", currLine)
                    spaces += 1 
                while spaces > 0: #Distributing spaces evenly. 
                    print  (" procesing spaces evenly")
                    currLine[index] += " " 
                    spaces -= 1 
                    index += 1 
                    index %= ((len(currLine)-1) or 1)
                joinedString = ''.join(currLine) #Combining words into one string
                lineList.append(joinedString)
                currLine = [] #Resetting variables. 
                currLength = 0   
        if currLine: 
            spaces = length - currLength  #Amount of extra spaces available
            index = 0
            currLine[-1] += (" " * spaces) #Left justify so only need to add space to end. 
            joinedLine = ''.join(currLine)
            lineList.append(joinedLine)
        return lineList


t = TextJustification
test = t.fullJustify(t,["What","must","be","acknowledgment","shall","be"] , 15)
print(test)
