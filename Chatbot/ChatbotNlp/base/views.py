from django.shortcuts import render
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from nltk.chat.util import Chat, reflections



def chatbot(request):
    responses = [
    (r"hello|hi|hey", ["Hello!", "Hi there!", "Hey!"]),
    (r"what's your name|who are you", ["I am a chatbot.", "Call me ChatGPT."]),
    (r"how are you|how's it going", ["I'm just a bot, but I'm doing fine!", "I'm good, thanks for asking."]),
    (r"bye|goodbye", ["Goodbye!", "Have a great day!", "See you later!"]),
    (r"(.*)", ["I'm sorry, I don't understand.", "Could you please rephrase that?"]),
]

    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        chatbot = Chat(responses, reflections)
        response = chatbot.respond(user_input)
        return render(request, 'chatbot.html', {'user_input': user_input, 'response': response})
    return render(request, 'chatbot.html')
