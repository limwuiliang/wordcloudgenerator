{\rtf1\ansi\ansicpg1252\cocoartf2759
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;\red0\green0\blue0;\red255\green255\blue255;}
{\*\expandedcolortbl;;\cssrgb\c0\c0\c0;\cssrgb\c100000\c100000\c100000\c50196;}
\paperw11900\paperh16840\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\deftab720
\pard\pardeftab720\partightenfactor0

\f0\fs24 \cf2 \expnd0\expndtw0\kerning0
# -*- coding: utf-8 -*-\
\pard\pardeftab720\partightenfactor0
\cf2 \uc0\u8232 \
import streamlit as st\
import pandas as pd\
import spacy\
from wordcloud import WordCloud\
import matplotlib.pyplot as plt\
\uc0\u8232 \
# Load the English tokenizer, tagger, parser, NER, and word vectors\
nlp = spacy.load("en_core_web_sm")\
\uc0\u8232 \
def generate_word_cloud(data, column_name):\
    # Concatenate all descriptions into one text\
    text = ' '.join(data[column_name].dropna())\
    \
    # Process the text\
    doc = nlp(text)\
    \
    # Words to ignore\
    ignore_words = \{'vector', 'illustration', 'background', 'line', 'icon', 'template', 'abstract', \
                    'mockup', '3D', 'photo', 'image', 'banner', 'presentation', 'picture', \
                    'concept', 'print', 'label', 'tile', 'graphic'\}\
    \
    # Filter words\
    words = [token.text.lower() for token in doc if (token.pos_ in ['NOUN', 'ADJ'] or \
             (token.dep_ == 'amod' and token.pos_ == 'ADJ')) and token.text.lower() not in ignore_words]\
    \
    # Generate a word cloud\
    wordcloud = WordCloud(width = 800, height = 400, background_color ='white').generate(' '.join(set(words)))\
    \
    # Display the word cloud using matplotlib\
    plt.figure(figsize = (10, 5), facecolor = None)\
    plt.imshow(wordcloud)\
    plt.axis("off")\
    plt.tight_layout(pad = 0)\
    \
    # Save plot to a temporary buffer\
    buf = io.BytesIO()\
    plt.savefig(buf, format="png")\
    plt.close()\
    buf.seek(0)\
    return buf\
\uc0\u8232 \
# Streamlit application layout\
st.title('Word Cloud Generator')\
\uc0\u8232 \
# File uploader allows user to add their own CSV\
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")\
if uploaded_file is not None:\
    data = pd.read_csv(uploaded_file)\
    if st.button('Generate Word Cloud'):\
        # Assuming the column with text is named 'Description'\
        buffer = generate_word_cloud(data, 'Description')\
        st.image(buffer, use_column_width=True)\
}