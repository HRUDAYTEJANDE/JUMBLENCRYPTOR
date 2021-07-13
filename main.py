import time
import winsound
import random

# function for choosing random word.

version = 1.0


def sound():
    frequency = 200  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 250  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 300  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    time.sleep(1)


def endsound():
    frequency = 300  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 250  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)
    frequency = 200  # Set Frequency To 2500 Hertz
    duration = 50  # Set Duration To 1000 ms == 1 second
    winsound.Beep(frequency, duration)


def jumble(word):
    # sample() method shuffling the characters of the word
    random_word = random.sample(word, len(word))
    jumbled = ''.join(random_word)
    print(jumbled)
    return jumbled


def choose():
    # choice() method randomly choose
    # any word from the list.
    pick = random.choice(message)

    return pick


print('==========Secret Message Generator', version, '=============')
sound()
message = input('What message would you like to encrypt?')
sound()
Jumbled = jumble(message)
sound()
Hint = input('What is the hint for this message?')
sound()
print('' * 2)
print('Details')
print('Message is', message)
print('Encoded message is', Jumbled)
print('Hint is', Hint)
yesorno = input('Load .txt file? (y/n)')
sound()
file = input('File name?')
if yesorno == 'y':
    f = open(file + '.txt', 'w')
    text_list = message+'|'+Jumbled+'|'+Hint
    f.write(text_list)
    f.close()

    # open and read the file after the appending:
    f = open(file+'.txt', "r")
    print(f.read())
    endsound()
if yesorno == 'n':
    print('Ending process...')
    time.sleep(2)
    endsound()
