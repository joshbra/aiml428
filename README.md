AIML428 Assignment.

Part 1:
To run the program, you will need the libraries listed in requirements.txt. These can be installed with
    pip install -r requirements.txt
and are probably default on the ECS machines.

The data set is the IMDB movie reviews, which is from https://ai.stanford.edu/~amaas/data/sentiment/. 
This set contains 50,000 reviews, half each positive and negative.

All code, data, and a trained model is available at https://github.com/joshbra/aiml428

I have merged the complete data set into a file located at https://raw.githubusercontent.com/joshbra/aiml428/master/full_data.txt,
(about 65MB) and all the scores are available at https://raw.githubusercontent.com/joshbra/aiml428/master/full_scores.txt.

If those files are saved into this folder as full_data.txt and full_scores.txt, the program should run fine.

Additionally, you can just load in the trained model by downloading it from https://github.com/joshbra/aiml428/blob/master/model.h5?raw=true

To run the program on an ECS machine:

    - Download the full_data.txt and full_scores.txt

    - pip install -r requirements.txt
    
    - python3 assignment_p1.py

This will load in the data, train the model, test it, and print out the resultant loss and accuracy.

Example output:

    $ python3 assignment_p1.py
    > loading data
    > data loaded
    Model: "sequential"
    _________________________________________________________________
    Layer (type)                 Output Shape              Param #
    =================================================================
    embedding (Embedding)        (None, None, 50)          5608700
    _________________________________________________________________
    conv1d (Conv1D)              (None, None, 64)          16064
    _________________________________________________________________
    global_average_pooling1d (Gl (None, 64)                0
    _________________________________________________________________
    dense (Dense)                (None, 16)                1040
    _________________________________________________________________
    dense_1 (Dense)              (None, 1)                 17
    =================================================================
    Total params: 5,625,821
    Trainable params: 5,625,821
    Non-trainable params: 0
    _________________________________________________________________

    Epoch 1/10
    59/59 [==============================] - 133s 2s/step - loss: 0.6932 - accuracy: 0.5010 - val_loss: 0.6907 - val_accuracy: 0.5648
    Epoch 2/10
    59/59 [==============================] - 135s 2s/step - loss: 0.6792 - accuracy: 0.6393 - val_loss: 0.5736 - val_accuracy: 0.7820
    Epoch 3/10
    59/59 [==============================] - 132s 2s/step - loss: 0.4971 - accuracy: 0.8260 - val_loss: 0.3503 - val_accuracy: 0.8667
    Epoch 4/10
    59/59 [==============================] - 147s 3s/step - loss: 0.2942 - accuracy: 0.8937 - val_loss: 0.2948 - val_accuracy: 0.8848
    Epoch 5/10
    59/59 [==============================] - 126s 2s/step - loss: 0.2198 - accuracy: 0.9211 - val_loss: 0.2770 - val_accuracy: 0.8924
    Epoch 6/10
    59/59 [==============================] - 115s 2s/step - loss: 0.1747 - accuracy: 0.9380 - val_loss: 0.2759 - val_accuracy: 0.8935
    Epoch 7/10
    59/59 [==============================] - 109s 2s/step - loss: 0.1439 - accuracy: 0.9517 - val_loss: 0.2788 - val_accuracy: 0.8942
    Epoch 8/10
    59/59 [==============================] - 109s 2s/step - loss: 0.1210 - accuracy: 0.9608 - val_loss: 0.2882 - val_accuracy: 0.8927
    Epoch 9/10
    59/59 [==============================] - 110s 2s/step - loss: 0.1028 - accuracy: 0.9664 - val_loss: 0.3014 - val_accuracy: 0.8913
    Epoch 10/10
    59/59 [==============================] - 109s 2s/step - loss: 0.0864 - accuracy: 0.9737 - val_loss: 0.3165 - val_accuracy: 0.8911
    313/313 - 9s - loss: 0.3134 - accuracy: 0.8920
    loss: 0.313
    accuracy: 0.892