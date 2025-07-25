# -*- coding: utf-8 -*-
"""SemanticSimilarity_KerasNLP_MRPCData.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1RqCPU4mK0taQGE_gk-ArmMrZIJvVwIo5

Reference link- https://keras.io/examples/nlp/semantic_similarity_with_keras_nlp/

### TODO Recording:

- Please upload the 3 files for training, test, and validation to Colab
"""

!pip install tensorflow-text

!pip install keras-nlp

"""### TODO Recording:

- Please restart the kernel
"""

import numpy as np
import pandas as pd

import keras
import keras_nlp
import tensorflow as tf

"""Loading training, validation, and testing data

- https://www.kaggle.com/datasets/thedevastator/nli-dataset-for-sentence-understanding?select=mrpc_train.csv
- https://www.kaggle.com/datasets/thedevastator/nli-dataset-for-sentence-understanding?select=mrpc_validation.csv
- https://www.kaggle.com/datasets/thedevastator/nli-dataset-for-sentence-understanding?select=mrpc_test.csv

Dataset info-

https://www.tensorflow.org/datasets/catalog/glue#gluemrpc

"""

mrpc_train_data = pd.read_csv("mrpc_train.csv")

mrpc_valid_data = pd.read_csv("mrpc_validation.csv")

mrpc_test_data = pd.read_csv("mrpc_test.csv")

"""### TODO Recording:

- Click on the table next to the data frame results to see the entire text
"""

mrpc_train_data.sample(5)

"""Train Dataset info is obtained. No Null values are found in train data"""

mrpc_train_data.info()

mrpc_valid_data.info()

"""Target balance is checked"""

mrpc_train_data["label"].value_counts()

mrpc_valid_data["label"].value_counts()

mrpc_test_data["label"].value_counts()

"""Creating training,validation and testing datasets from dataframes default, `keras_nlp.models.BertClassifier` will tokenize and pack
together raw strings using a `"[SEP]"` token during training.
"""

train_ds = tf.data.Dataset.from_tensor_slices((
    (mrpc_train_data["sentence1"].values, mrpc_train_data["sentence2"].values),
     mrpc_train_data["label"].values
)).batch(batch_size = 32)

val_ds = tf.data.Dataset.from_tensor_slices((
    (mrpc_valid_data["sentence1"].values, mrpc_valid_data["sentence2"].values),
     mrpc_valid_data["label"].values
)).batch(batch_size = 32)

test_ds = tf.data.Dataset.from_tensor_slices((
    (mrpc_test_data["sentence1"].values, mrpc_test_data["sentence2"].values),
     mrpc_test_data["label"].values
)).batch(batch_size = 32)

"""We can view one batch of training data with both sentence pairs and labels.For example-Pair of 'Yucaipa owned Dominick 's before selling the chain to Safeway in 1998 for $ 2.5 billion ' and "Yucaipa bought Dominick 's in 1995 for $ 693 million and sold it to Safeway for $ 1.8 billion in 1998 ." are not sematically equivalent.But pairs like
The stock rose $ 2.11 , or about 11 percent , to close Friday at $ 21.51 on the New York Stock Exchange .' and 'PG & E Corp. shares jumped $ 1.63 or 8 percent to $ 21.03 on the New York Stock Exchange on Friday .' are semantically equivalent
"""

next(iter(train_ds))

"""Labels are converted into one hot form for this binary classification task and can be seen"""

def preprocess_label(text, label):

    one_hot_label = tf.one_hot(label, depth = 2)

    return text, one_hot_label

train_ds = train_ds.map(preprocess_label)

val_ds = val_ds.map(preprocess_label)

test_ds = test_ds.map(preprocess_label)

_, train_batch_labels = next(iter(train_ds))

train_batch_labels

"""Using the BERT model from KerasNLP to establish a baseline for our semantic similarity task. The keras_nlp.models.BertClassifier class attaches a classification head to the BERT Backbone, mapping the backbone outputs to a logit output suitable for a classification task. This significantly reduces the need for custom code.

KerasNLP models have built-in tokenization capabilities that handle tokenization by default based on the selected model. However, users can also use custom preprocessing techniques as per their specific needs. If we pass a tuple as input, the model will tokenize all the strings and concatenate them with a "[SEP]" separator.

We use this model with pretrained weights, and we can use the from_preset() method to use our own preprocessor. For the MRPC, we set num_classes to 2.
"""

bert_classifier = keras_nlp.models.BertClassifier.from_preset(
    " ", num_classes = 2
)

bert_classifier.summary()

"""As default compilation parameters does not match our case, we are compiling our model explicitly."""

bert_classifier.compile(
    loss = keras.losses.BinaryCrossentropy(from_logits = True),
    optimizer = tf.keras.optimizers.Adam(5e-5),
    metrics = [tf.keras.metrics.BinaryAccuracy(), tf.keras.metrics.Precision(), tf.keras.metrics.Recall()],
)

"""Please note that the BERT Tiny model has only 4,386,307 trainable parameters.

KerasNLP task models come with compilation defaults. We can now train the model we just instantiated by calling the fit() method.

Training the model for 3 epochs
"""

bert_classifier.fit(train_ds, validation_data = val_ds, epochs = 3)

"""Evaluating the performance of the trained model on test data."""

bert_classifier.evaluate(test_ds)

"""Warning is coming while saving the model as Model is compiled with different parameters from default ones.So we would compile the restored model with our parameters for making predictions"""

bert_classifier.save("bert_classifier.keras")

restored_model = keras.models.load_model("bert_classifier.keras")

restored_model.compile(
    loss = keras.losses.BinaryCrossentropy(from_logits = True),
    optimizer = tf.keras.optimizers.Adam(5e-5),
    metrics = [tf.keras.metrics.BinaryAccuracy(), tf.keras.metrics.Precision(), tf.keras.metrics.Recall()],
)

restored_model.evaluate(test_ds)

"""## Performing inference with the model.

Let's see how to perform inference with KerasNLP models
"""

(test_sample_sen1, test_sample_sen2), test_sample_labels = next(iter(test_ds))

"""Convert to Hypothesis-Premise pair, for forward pass through model"""

sample = (test_sample_sen1, test_sample_sen2)

sample

"""The default preprocessor in KerasNLP models handles input tokenization automatically,
so we don't need to perform tokenization explicitly.
"""

predictions = bert_classifier.predict(sample)

predictions

"""Applying the sigmoid activation on logits"""

import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Get the class predictions with maximum probabilities
predictions = sigmoid(predictions)

predictions

"""Comparing actual labels with predictions"""

y_pred = np.argmax(predictions, axis = 1)

y_pred

test_sample_labels

y_test = np.argmax(test_sample_labels, axis = 1)

y_test

import pandas as pd

df = pd.DataFrame()

df['Sentence 1'] = test_sample_sen1

df['Sentence 2'] = test_sample_sen2

df.sample(5)

"""### TODO Recording:

- Click on the table next to the dataframe results so we can see the entire sentences
"""

df['y_test'] = y_test

df['y_pred'] = y_pred

df.sample(10)

