import tensorflow as tf
import numpy as np
from sklearn import model_selection, preprocessing, metrics
from tensorflow.python.keras.preprocessing import sequence
from tensorflow.python.keras.preprocessing import text

# I'm using the IMDB 50k reviews dataset, which is split 50:50 into positive and negative reviews, with 25k of each
# you can find the data sets here: (about 65MB)

print('> loading data')
with open('./full_data.txt') as f:
  data = [line for line in f]

with open('./full_scores.txt') as f:
  scores = [int(line) for line in f]
print('> data loaded')

# Split our data into a train and test set - training is 80% of original
train_X, test_X, train_Y, test_Y = model_selection.train_test_split(data, scores, random_state=1, test_size=0.2)

# Fit a tokenizer to our text. According to some research, 20,000 is about the sweet spot
# for english
tokenizer = text.Tokenizer(num_words=20000)
tokenizer.fit_on_texts(train_X)

encoder = preprocessing.LabelEncoder()
train_Y = encoder.fit_transform(train_Y)
test_Y = encoder.fit_transform(test_Y)

train_X = tokenizer.texts_to_sequences(train_X)
test_X = tokenizer.texts_to_sequences(test_X)

# using the longest example for the length, and padding everything shorter
max_length = len(max(train_X, key=len))
train_X = sequence.pad_sequences(train_X, maxlen=max_length)
test_X = sequence.pad_sequences(test_X, maxlen=max_length)

# build the model, going embedding -> CNN -> Pooling -> Dense(16) -> Dense(1)
model = tf.keras.Sequential()
model.add(tf.keras.layers.Embedding(len(tokenizer.word_index) + 1, 50))
model.add(tf.keras.layers.Conv1D(filters=64, kernel_size=5, activation='relu'))
model.add(tf.keras.layers.GlobalAveragePooling1D())
model.add(tf.keras.layers.Dense(16, activation='relu'))
model.add(tf.keras.layers.Dense(1, activation='sigmoid'))

print(model.summary())

model.compile(optimizer='adam', loss=tf.keras.losses.BinaryCrossentropy(), metrics=['accuracy'])

# Train our model - using 25% of the training set for validation
model.fit(train_X, train_Y, epochs=10, validation_split=0.25, batch_size=512, validation_batch_size=512, verbose=1)

results = model.evaluate(test_X, test_Y, verbose=2)

for name, value in zip(model.metrics_names, results):
  print("%s: %.3f" % (name, value))

model.save('cnn_1')