from tkinter import *
from translate import Translator

# Initialize the main window
Screen = Tk()
Screen.title("Language Translator Application ")
Screen.config(bg="#FFC0CB")  # Use a pleasant pink

# Variables to hold language choices and text
InputLanguageChoice = StringVar()
TranslateLanguageChoice = StringVar()
TextVar = StringVar()
OutputVar = StringVar()

# Set default language choices
InputLanguageChoice.set('English')
TranslateLanguageChoice.set('Indonesian')

# Define the available language choices
LanguageChoices = ['Chinese', 'Russian', 'Indonesian', 'English', 'French', 'German', 'Spanish', 'Korean', 'Japanese']

# Function to perform translation
def Translate():
    translator = Translator(from_lang=InputLanguageChoice.get(), to_lang=TranslateLanguageChoice.get())
    Translation = translator.translate(TextVar.get())
    OutputVar.set(Translation)

# Create and place widgets
Label(Screen, text="Select Input Language", bg="#FFC0CB", fg="white", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky=W)
InputLanguageChoiceMenu = OptionMenu(Screen, InputLanguageChoice, *LanguageChoices)
InputLanguageChoiceMenu.config(bg="#FF69B4", fg="white", font=("Arial", 10))
InputLanguageChoiceMenu.grid(row=1, column=0, padx=10, pady=10, sticky=W)

Label(Screen, text="Select Output Language", bg="#FFC0CB", fg="white", font=("Arial", 12)).grid(row=0, column=1, padx=10, pady=10, sticky=W)
NewLanguageChoiceMenu = OptionMenu(Screen, TranslateLanguageChoice, *LanguageChoices)
NewLanguageChoiceMenu.config(bg="#FF69B4", fg="white", font=("Arial", 10))
NewLanguageChoiceMenu.grid(row=1, column=1, padx=10, pady=10, sticky=W)

Label(Screen, text="Enter Text", bg="#FFC0CB", fg="white", font=("Arial", 12)).grid(row=2, column=0, padx=10, pady=10, sticky=W)
Entry(Screen, textvariable=TextVar, bg="#FFB6C1", fg="black", font=("Arial", 10)).grid(row=2, column=1, padx=10, pady=10, sticky=W)

Label(Screen, text="Translated Text", bg="#FFC0CB", fg="white", font=("Arial", 12)).grid(row=3, column=0, padx=10, pady=10, sticky=W)
Entry(Screen, textvariable=OutputVar, bg="#FFB6C1", fg="black", font=("Arial", 10)).grid(row=3, column=1, padx=10, pady=10, sticky=W)

Button(Screen, text="Translate", command=Translate, relief=GROOVE, bg="#FF69B4", fg="white", font=("Arial", 12)).grid(row=4, column=0, columnspan=2, pady=20)

# Run the main loop
mainloop()
