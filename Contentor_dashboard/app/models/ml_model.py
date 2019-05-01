from keras.models import Model, model_from_json
from keras.layers import Dense, Input, GRU
from keras.layers.embeddings import Embedding
from gensim.models.keyedvectors import KeyedVectors

class MLModel():

    def __init__(self):
        word_dim = 50
        num_tokens = 14558#len(word_to_int.keys())

        # Define the layers
        word_vec_input = Input(shape=(word_dim,))
        decoder_inputs = Input(shape=(None,))
        decoder_embed = Embedding(input_dim=num_tokens, output_dim=word_dim, mask_zero=True)
        decoder_gru_1 = GRU(word_dim, return_sequences=True, return_state=False)
        decoder_gru_2 = GRU(word_dim, return_sequences=True, return_state=True)
        decoder_dense = Dense(num_tokens, activation='softmax')

        # Connect the layers
        embedded = decoder_embed(decoder_inputs)
        gru_1_output = decoder_gru_1(embedded, initial_state=word_vec_input)
        gru_2_output, state_h = decoder_gru_2(gru_1_output)
        decoder_outputs = decoder_dense(gru_2_output)

        # Define the model that will be used for training
        #training_model = Model([word_vec_input, decoder_inputs], decoder_outputs)
        # decoder_model = Model([word_vec_input, decoder_inputs], [decoder_outputs, state_h])
        self.training = self.load_model('encoder_model.json', 'encoder_model_weights.h5')
        self.decoder_model = self.load_model('decoder_model.json', 'decoder_model_weights.h5')

        self.glove_model = KeyedVectors.load_word2vec_format("gensim_glove_vectors.txt", binary=False)

    def load_model(self, model_filename, model_weights_filename):
        with open(model_filename, 'r', encoding='utf8') as f:
            model = model_from_json(f.read())
        model.load_weights(model_weights_filename)
        return model

    def get_decoder_model():
        return decoder_model

    def get_glove_model():
        return glove_model