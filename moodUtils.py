import random as random

responses = {
    "negative" : ["I am sorry to hear that.", "I hope you feel better!"],
    "positive" : ["I'm glad!", "Great!"]
}


def moodResponse(mood):
    word_set = set(mood.split(" "))
    possible_responses = []
    if word_set.intersection(["sad", "unhappy", "bad"]):
        possible_responses = responses.get("negative")
    elif word_set.intersection(["happy", "good", "great", "alright"]):
        possible_responses = responses.get("positive")
    if len(possible_responses) > 1:
        print(possible_responses[random.randint(1, len(possible_responses))-1])
    elif len(possible_responses) == 1:
        print(possible_responses[0])
    elif len(possible_responses) == 0:
        print("Okay, well thanks for the chat!")