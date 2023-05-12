# Chatbot:
# Create a simple chatbot that can answer basic questions using natural language processing.

import nltk
from nltk.chat.util import Chat, reflections

pairs = [  ["hi|hello|hey", ["Hello!", "Hi there!"]],
  ["what is your name?", ["My name is Chatbot.", "I'm Chatbot."]],
  ["how are you?", ["I'm doing well, thank you.", "I'm fine, thanks for asking."]],
  ["what time is it?", ["Sorry, I don't have access to the system clock."]],
  ["bye|goodbye", ["Goodbye!", "See you later!"]]
]

chatbot = Chat(pairs, reflections)
chatbot.converse()
