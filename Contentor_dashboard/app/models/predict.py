from keras.models import model_from_json, Model
from .ml_model import MLModel
import numpy as np
import pickle
instance = MLModel()
decoder_model = instance.decoder_model
glove_model = instance.glove_model
# import os
# print(os.path.dirname(os.path.abspath(__file__)))
with open("models/int_to_word.pickle", "rb") as a:
    int_to_word = pickle.load(a)

with open("models/word_to_int.pickle", "rb") as b:
    word_to_int = pickle.load(b)

def generate(keywords):
    keywords = keywords.split(",")
    return decode_sequence(keywords)

def decode_sequence(input_seq):
    # Encode the input as state vectors.
    encoding_vector = np.zeros((1,50))
    for word in input_seq:
        try:
            encoding_vector[0] += glove_model[word]
        except:
            continue
    
#     print(encoding_vector.shape)
            
    target_seq = np.zeros((1,59), dtype=int)
    target_seq[0,0] = word_to_int["[START]"]
#     target_seq[0,1] = word_to_int["We"]
#     target_seq[0,2] = word_to_int["are"]
#     target_seq[0,3] = word_to_int[","]
    
#     print(len(target_seq))
    
    stop_condition = False
    decoded_sentence = ''
    counter = 1
    # Sampling loop for a batch of sequences
    # (to simplify, here we assume a batch of size 1).
    while not stop_condition:
        output_tokens, h= decoder_model.predict([encoding_vector, target_seq])
        
        # Sample a token
        sampled_token_index = np.argmax(output_tokens[0, -1, :])
        sampled_char = int_to_word[sampled_token_index]
        decoded_sentence += sampled_char + " "
        
        if (sampled_char == "[END]" or
           len(decoded_sentence.split()) > 37):
            stop_condition = True
        
#         next_word = np.zeros((1,59))
#         next_word[0, counter] = sampled_token_index
        target_seq[0, counter] = sampled_token_index
        counter+=1
    
    
    return decoded_sentence