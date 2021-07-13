## Jumble Encryptor

This file can be used to encrypt files(not recommended). It can also be used to make a puzzle.

If you want to make this file yourself, please refer to the repository link below
https://github.com/HRUDAYTEJANDE/JUMBLENCRYPTOR
##Code
The libraries used for the project are
```markdown
import time
#used to delay code
import winsound
#used for sound effects
import random
#for jumbling
```

For the code:
Jumbler(random):
#the jumbler helps to jumble the word that you will input
```markdown
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
```
The code that is used to initialize this
```markdown
def jumble(word)
```
Word is the parameter for the text that you can jumble
Examples:
1
Sound(winsound):
#Used for sound effects.
```markdown
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
```

