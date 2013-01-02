from __future__ import division
from random import shuffle, choice
import pyttsx

t = '-> '
tstr = lambda x: "-> %s" % (x)
words = []
with open("words.txt") as f:
    words = f.read().split('\n')
shuffle(words)
speak = pyttsx.init()
speak.setProperty("rate", 150)
speak.setProperty("volume", 1)

print "Welcome to the Spelling Bee Practice Challenge"
com = raw_input(t)

if com.lower() == 'start':
    correct_words = 0
    wrong_words   = 0
    overall_words = 0
    while True:
        word = choice(words)
        speak.say(word)
        speak.runAndWait()
        speak.stop()
        already_said = True
        com = raw_input(tstr("Enter word or command: "))

        if com == 'quit':
            print "Word statistics: "
            print "Words right:     %s/%s" % (correct_words, overall_words)
            print "Words wrong:     %s/%s" % (wrong_words, overall_words)
            print "Percent correct: %d%%"  % (int((correct_words/overall_words) * 100))
            print "Percent wrong:   %d%%"  % (int((wrong_words/overall_words) * 100))
            break
        else:
            new_word = com
            if new_word != word:
                print tstr("Words do not match")
                print t, word
                print t, new_word
                wrong_words += 1
                overall_words += 1
            else:
                print tstr("Words match!")
                correct_words += 1
                overall_words += 1

