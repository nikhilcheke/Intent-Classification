#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 12:12:16 2019

@author: nikhildattatraya.c
"""
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
import re
from keras.preprocessing.sequence import pad_sequences
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from keras.utils import to_categorical
from keras.models import Sequential, load_model
from keras.layers import Dense, LSTM, Bidirectional, Embedding, Dropout
from keras.callbacks import ModelCheckpoint

lemmatizer = WordNetLemmatizer()
"""
dataframe = pd.read_csv("/Users/nikhildattatraya.c/Downloads/Intent_Classification-master/Dataset.csv")
dataframe.head()

data = list(dataframe['data'])
label = dataframe['label']
labeluniq = list(set(label))
from ast import literal_eval
d = [literal_eval(item) for item in data]

d = pd.DataFrame(d)
data = d['data']
"""
dataframe = pd.read_csv("/Users/nikhildattatraya.c/Downloads/Intent_Classification-master/Dataset.csv", encoding = "latin1", names = ["Sentence", "Intent"])
print(dataframe.head())
label = dataframe["Intent"]
unique_intent = list(set(label))
data = list(dataframe["Sentence"])


print('Loading word vectors...')
word2vec = {}
embedding = []
idx2word = []
with open('/Users/nikhildattatraya.c/Downloads/glove.6B/glove.6B.50d.txt', encoding='utf-8') as f:
  for line in f:
    values = line.split()
    word = values[0]
    vec = np.asarray(values[1:], dtype='float32')
    word2vec[word] = vec
    embedding.append(vec)
    idx2word.append(word)
    
print('Found %s word vectors.' % len(word2vec))
embedding = np.array(embedding)
V, D = embedding.shape
word2idx = {v:k for k,v in enumerate(idx2word)}

nltk.download('wordnet')

def lemma_clean(sentences):
    words = []
    unknownwords = 0 
    for s in sentences:
        sents = re.sub(r'[^ a-z A-Z 0-9]', " ", s)
        w = word_tokenize(sents)
        w = [lemmatizer.lemmatize(i.lower()) for i in w]
        temp = []
        for i in w:
            if i in word2idx:
                temp.append(word2idx[i])
            else:
                unknownwords =unknownwords+ 1
        words.append(temp)  
    print(unknownwords)
    return words


wordindx = lemma_clean(list(data))
maxlen = 25
train_test_data = pad_sequences(wordindx, maxlen=maxlen, padding='post')

#train_test_label = [one_hot(i, 5) for i in list(label)]
y = dataframe.Intent.values
ohe = OneHotEncoder()
ohe = ohe.fit_transform(y.reshape(-1,1)).toarray()

train_X, val_X, train_Y, val_Y = train_test_split(train_test_data, ohe, shuffle = True, test_size = 0.2)

model = Sequential()

embedding_layer = Embedding(input_dim=embedding.shape[0],
                            output_dim=embedding.shape[1], 
                            input_length=maxlen,
                            weights=[embedding], 
                            trainable=False, 
                            name='embedding_layer')

model.add(embedding_layer)
model.add(Bidirectional(LSTM(128)))
#   model.add(LSTM(128))
model.add(Dense(32, activation = "relu"))
model.add(Dropout(0.5))
model.add(Dense(21, activation = "softmax"))


model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ["accuracy"])
model.summary()


filename = 'model.h5'
checkpoint = ModelCheckpoint(filename, monitor='val_loss', verbose=1, save_best_only=True, mode='min')

hist = model.fit(train_X, train_Y, epochs = 100, batch_size = 32, validation_data = (val_X, val_Y), callbacks = [checkpoint])
