import random
import sys
import os

# ASCII sentence encoding
sentences=[
    'Birds sing sweetly',
    'Learning a new language can open up a world of opportunities for travel and cultural understanding.',
    'The sky is blue',
    'Cooking a homemade meal from scratch can be both satisfying and delicious.',
    'The ocean waves crash',
    'Mountains covered in snow offer some of the most stunning vistas for avid skiers.',
    'The mountain is tall',
    'Exploring historical landmarks can provide a deeper connection to the past.',
    'Music soothes me.',
    'Listening to your favorite music can transport you to different times and places.',
    'Time flies quickly',
    'Artistic expression comes in many forms, from painting to dance to poetry.',
    'Helping others in times of need can be one of the most rewarding experiences in life.',
    'We danced all night',
    'Taking a long walk in nature can clear the mind and rejuvenate the spirit.',
    'I love chocolate ice cream',
    'Technology has revolutionized the way we communicate and connect with one another.',
    'The cat chased the ball',
    'Traveling to new countries exposes you to diverse cultures and cuisines.',
    'Sunsets are beautiful'
    ]

# Function to convert sentence to ASCII binary encoded message
def sentence_to_binary(sentence):
    binary_message = ""
    for char in sentence:
        ascii_value = ord(char)
        binary_value = bin(ascii_value)[2:].zfill(8)
        binary_message += binary_value
    return binary_message

'''for sentence in sentences:
    binary_encoded_message = sentence_to_binary(sentence)
    print(binary_encoded_message)'''

# Function to generate random encoded sentences
def random_sentence_generation(sentences):
    random_token=random.randint(0,len(sentences)-1)
    random_sentence=sentences[random_token]
    random_encoded_sentence=sentence_to_binary(random_sentence)
    return random_encoded_sentence


for _ in range(10):
    print(random_sentence_generation(sentences))
    
