# This code is creating a GUI using tkinter that monitors user input, and clears the input after 1 second of the
# user not typing. It sets the title of the window and the geometry of the window. It also creates a text box for the
# user to type in, and binds an event to it to update the stoppedTyping variable. Then it creates a
# checkIfStoppedTyping() function to check if the user has stopped typing, and if they have, it clears their input.
# Lastly, it starts the timer and the main loop.

import tkinter as tk

root = tk.Tk()
root.title('Disappearing Text App')
root.geometry("400x250")

# Create a variable used to track if the user has stopped typing
stoppedTyping = False


# Function that updates the stoppedTyping variable if the user stops typing
def TrackUserInput(event):
    global stoppedTyping
    stoppedTyping = False


# Declare a string variable to store user input
userInput = ""

# Create a text box for the user to type in
textBox = tk.Text(root, height=30, width=70)
textBox.config(font=('Times New Roman', 30))
textBox.pack()

# Bind an event that updates the stoppedTyping variable to the text box
textBox.bind("<KeyRelease>", TrackUserInput)


# Create and start a timer to check if the user has stopped typing
def checkIfStoppedTyping():
    global stoppedTyping
    if not stoppedTyping:
        stoppedTyping = True
        global userInput
        userInput = textBox.get(1.0, tk.END)
    else:
        userInput = ""
        textBox.delete(1.0, tk.END)
    root.after(1000, checkIfStoppedTyping)


# Start the timer
checkIfStoppedTyping()

# Start the main loop
root.mainloop()
