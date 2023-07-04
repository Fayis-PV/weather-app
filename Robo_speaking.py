# Install pyttsx3 module to speak the text : pip install pyttsx3
import pyttsx3

# Provide a function which speaks what it is given. 
def say_command(value):
    return pyttsx3.speak(value)

# Welcome Command using function
say_command(str('Hello friend, I am Robo speaking. Developed by Muhammed Fayis PV'))

# Body of the Robo who can speak the entered text and continue request using while loop.
while True:
    say_command(str('Enter something to speak in English or q for quit'))
    value = input('Enter something to speak in English or q for quit: \n')

    # If you want to quit, you can simply enter the letter 'q', then it will break the while loop.
    if value == 'q':
        end = ('Thank You for supporting me. Have a nice day')
        say_command(end)
        break
    
    # Call to the function to speak the entered text.
    say_command(value)