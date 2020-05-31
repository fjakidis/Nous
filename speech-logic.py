import pyttsx3
import string

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[11].id)

f = open('dialogue', 'w')
saved = []

while True:
    print('\n')
    print('Options: ')
    print(' - 1 - speak')
    print(' - 2 - save a line')
    print(' - 3 - show saved lines')
    print(' - 4 - print a saved text')
    print(' - 5 - speak a saved text')
    print(' - 8 - save prose')
    print(' - 9 - exit')
    print('\n')

    inp = input('Choose an option (integer):  ')
    
    print(inp)
    

    if (inp=='1'):
        while True:
            text = input()
            if (text=='----'):
                break
            else:
                f.write(text+'\n')
                engine.say(text)
                engine.runAndWait()
    elif (inp=='2'):
        print('Saving... ')
        print()
        save = input()
        saved.append(save)
    elif (inp=='3'):
        index = 0
        for i in saved:
            print()
            print('index : {} \t text : {}'.format(index,i))
            index += 1
    elif(inp=='4'):
        print()
        print('Choose an index from 0 to {}'.format(len(saved)))
        print()
        index = int(input('[index] as an integer  '))
        print(saved[index])
    elif(inp=='5'):
        print()
        index = int(input('[index] as an integer:   '))
        print()
        engine.say(saved[index])
        engine.runAndWait()
    elif(inp=='8'):
        f.close()
    elif(inp=='9'):
        f.close()
        break

