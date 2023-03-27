import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import sklearn


def transform_text(text):
    # converting to lower case
    text = text.lower()
    # Word tokenization:
    text = nltk.word_tokenize(text)
    # Removing special characters:
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    # Removing stop words and punctuations
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    # Stemming the sentences
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return ' '.join(y)


ps = PorterStemmer()
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

st.title('SMS/E-Mail Spam detecter:')

input_sms = st.text_area('Enter the message')

if st.button('Predict'):
    # 1. Preprocess:
    transformed_sms = transform_text(input_sms)

    # 2. Vectorize:
    vector_input = tfidf.transform([transformed_sms])

    # 3.Predict:
    result = model.predict(vector_input)[0]

    # 4. Display:

    if result == 1:
        st.header("SPAM!!!")

    else:
        st.header('Not Spam !!!')
