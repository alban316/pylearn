#!/usr/bin/env python

# hangman.py

# _____
# |   |
# |   O
# |  /|\
# |  / \
# |_______

gallows = [[0 for cols in range(5)] for rows in range(7)]

gallows[0] = [' _____', ' |   |', ' |', ' |', ' |', ' |_______']
gallows[1] = [' _____', ' |   |', ' |   O', ' |', ' |', ' |_______']
gallows[2] = [' _____', ' |   |', ' |   O', ' |  /', ' |', ' |_______']
gallows[3] = [' _____', ' |   |', ' |   O', ' |  / \\', ' |', ' |_______']
gallows[4] = [' _____', ' |   |', ' |   O', ' |  /|\\', ' |', ' |_______']
gallows[5] = [' _____', ' |   |', ' |   O', ' |  /|\\', ' |  / ', ' |_______']
gallows[6] = [' _____', ' |   |', ' |   O', ' |  /|\\', ' |  / \\', ' |_______']




class Game():
    def __init__(self):
        self.reset()
 
    def reset(self):
        print "Welcome to Hangman!"
        self.word = self.nextWord()
        self.mask = self.maskWord(self.word)
        self.maxGuesses = 6
        self.numGuesses = self.maxGuesses    
  
    def loop(self):
        self.printGallows()
        while (self.numGuesses > 0):
            print self.mask
          
            playerGuess = raw_input("Guess a letter: ")
            if not (self.unmask(playerGuess)):
                self.numGuesses -= 1
                self.printGallows()
                if (self.numGuesses == 0):
                    print "Too bad!"

            elif self.mask == self.word:
                print "You win!"
                self.numGuesses = 0
                
        playAgain = raw_input("Play again? [y/N]: ")
        if (playAgain == "y"):
            return True
            
        return False
        
    def nextWord(self):
        return "hangman"
        
    def maskWord(self,word):
        mask = ''
        for letters in word:
            mask += '-'
        return mask
        
    def unmask(self,letter):
        result = False
        i = 0;
        for l in self.word:
            if l == letter:
                self.mask = left(self.mask, i) + l + right(self.mask, i + 1)
                result = True
            i += 1
        return result
        
    def printGallows(self):
        for gallowsLine in gallows[self.maxGuesses - self.numGuesses]:
            print gallowsLine

        
def left(sstring, n):
    if n < 0:
        return ""
    else:
        return sstring[:n] 

        
def right(sstring, n):
    if n > len(sstring):
        return ""
    else:
        return sstring[n:]


def main():
    game = Game()
    loop = game.loop()
    while (loop):
        game.reset()
        loop = game.loop()
        
        
if __name__ == '__main__':
    main()
    





