import nltk
nltk.download('punkt')

import nltk
from nltk.chat.util import Chat, reflections
from tkinter import *

class ChatBot:
    def __init__(self, root):
        self.root = root
        self.root.title("ChatBot")
        self.root.geometry("400x500")
        
        # Setting up the chat window
        self.chat_log = Text(self.root, bd=1, bg="white", height="8", width="50", font="Arial")
        self.chat_log.config(state=DISABLED)

        # Scroll bar
        self.scrollbar = Scrollbar(self.root, command=self.chat_log.yview)
        self.chat_log['yscrollcommand'] = self.scrollbar.set

        # Message box
        self.entry_box = Text(self.root, bd=1, bg="white", width="29", height="5", font="Arial")

        # Buttons
        self.send_button = Button(self.root, text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b", font="Arial", command=self.send_message)

        # Layout
        self.scrollbar.place(x=376, y=6, height=386)
        self.chat_log.place(x=6, y=6, height=386, width=370)
        self.entry_box.place(x=128, y=401, height=90, width=265)
        self.send_button.place(x=6, y=401, height=90)

        self.chat_pairs = [
            [r"hi|hello|hey", ["Hello, how can I assist you today?", "Hi there!"]],
            [r"what is your name?", ["I'm a simple chatbot built using Python."]],
            [r"how are you?", ["I'm doing great! How about you?"]],
            [r"(.*) your favorite (.*)", ["I really enjoy helping people with their questions."]],
            [r"(.*) (created|developed|made) you?", ["I was developed by a Python programmer!"]],
            [r"bye|exit", ["Goodbye! Have a great day ahead!", "See you soon!"]],
            [r"(.*)", ["Sorry, I don't understand that. Can you try asking something else?"]]
        ]
        self.chatbot = Chat(self.chat_pairs, reflections)

    def send_message(self):
        user_input = self.entry_box.get("1.0", "end-1c").strip()

        if user_input != '':
            self.chat_log.config(state=NORMAL)
            self.chat_log.insert(END, "You: " + user_input + '\n\n')
            self.chat_log.config(foreground="#442265", font=("Verdana", 12))

            # Get the bot's response
            response = self.chatbot.respond(user_input)
            self.chat_log.insert(END, "Bot: " + response + '\n\n')

            self.chat_log.config(state=DISABLED)
            self.chat_log.yview(END)

        # Clear the entry box after sending the message
        self.entry_box.delete("1.0", END)

# Creating the main window for the chatbot
root = Tk()
chatbot = ChatBot(root)
root.mainloop()
