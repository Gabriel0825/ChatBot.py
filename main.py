import random
import re
from Respuestas import responsesBot

#ELIMINANDO CARACTERES
def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_messages(split_message)
    return str(response)

#CALCULANDO LA PROBABILIDAD
def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty += 1

    percentage = float(message_certainty) / float (len(recognized_words))

    for palabra in required_word:
        if palabra not in user_message:
            has_required_words = False
            break

    if has_required_words or single_response:
        return int(percentage*100)
    else:
        return 0

#VERIFICANDO LOS MENSAJES
def check_messages(message):
        highest_prob = {}

        def response(chatbot_response, list_words, single_message=False, required_word=[]):
            nonlocal highest_prob
            highest_prob[chatbot_response] = message_probability(message, list_words, single_message,required_word)

        responsesBot(response)

        best_match = max(highest_prob, key = highest_prob.get)
        print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match


def unknown():
    response = ['No comprendo bien lo que dijiste', 'Tengo problemas para entenderte', 'No te he entendido, por favor, intenta de nuevo'][random.randrange(3)]

while True:
    print("Bot: " + get_response(input('User: ')))