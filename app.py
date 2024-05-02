bplist00�_WebMainResource�	
_WebResourceMIMEType_WebResourceTextEncodingName^WebResourceURL_WebResourceFrameName_WebResourceDataYtext/htmlUutf-8_file:///index.htmlPO�<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
  <meta http-equiv="Content-Style-Type" content="text/css">
  <title></title>
  <meta name="Generator" content="Cocoa HTML Writer">
  <meta name="CocoaVersion" content="2487.4">
  <style type="text/css">
    p.p1 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica}
    p.p2 {margin: 0.0px 0.0px 0.0px 0.0px; font: 12.0px Helvetica; min-height: 14.0px}
  </style>
</head>
<body>
<p class="p1">import streamlit as st</p>
<p class="p1">import pandas as pd</p>
<p class="p1">import spacy</p>
<p class="p1">from wordcloud import WordCloud</p>
<p class="p1">import matplotlib.pyplot as plt</p>
<p class="p2"><br></p>
<p class="p1"># Load the English tokenizer, tagger, parser, NER, and word vectors</p>
<p class="p1">nlp = spacy.load("en_core_web_sm")</p>
<p class="p2"><br></p>
<p class="p1">def generate_word_cloud(data, column_name):</p>
<p class="p1"><span class="Apple-converted-space">    </span># Concatenate all descriptions into one text</p>
<p class="p1"><span class="Apple-converted-space">    </span>text = ' '.join(data[column_name].dropna())</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Process the text</p>
<p class="p1"><span class="Apple-converted-space">    </span>doc = nlp(text)</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Words to ignore</p>
<p class="p1"><span class="Apple-converted-space">    </span>ignore_words = {'vector', 'illustration', 'background', 'line', 'icon', 'template', 'abstract',<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">                    </span>'mockup', '3D', 'photo', 'image', 'banner', 'presentation', 'picture',<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">                    </span>'concept', 'print', 'label', 'tile', 'graphic'}</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Filter words</p>
<p class="p1"><span class="Apple-converted-space">    </span>words = [token.text.lower() for token in doc if (token.pos_ in ['NOUN', 'ADJ'] or<span class="Apple-converted-space"> </span></p>
<p class="p1"><span class="Apple-converted-space">             </span>(token.dep_ == 'amod' and token.pos_ == 'ADJ')) and token.text.lower() not in ignore_words]</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Generate a word cloud</p>
<p class="p1"><span class="Apple-converted-space">    </span>wordcloud = WordCloud(width = 800, height = 400, background_color ='white').generate(' '.join(set(words)))</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Display the word cloud using matplotlib</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.figure(figsize = (10, 5), facecolor = None)</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.imshow(wordcloud)</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.axis("off")</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.tight_layout(pad = 0)</p>
<p class="p2"><span class="Apple-converted-space">    </span></p>
<p class="p1"><span class="Apple-converted-space">    </span># Save plot to a temporary buffer</p>
<p class="p1"><span class="Apple-converted-space">    </span>buf = io.BytesIO()</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.savefig(buf, format="png")</p>
<p class="p1"><span class="Apple-converted-space">    </span>plt.close()</p>
<p class="p1"><span class="Apple-converted-space">    </span>buf.seek(0)</p>
<p class="p1"><span class="Apple-converted-space">    </span>return buf</p>
<p class="p2"><br></p>
<p class="p1"># Streamlit application layout</p>
<p class="p1">st.title('Word Cloud Generator')</p>
<p class="p2"><br></p>
<p class="p1"># File uploader allows user to add their own CSV</p>
<p class="p1">uploaded_file = st.file_uploader("Choose a CSV file", type="csv")</p>
<p class="p1">if uploaded_file is not None:</p>
<p class="p1"><span class="Apple-converted-space">    </span>data = pd.read_csv(uploaded_file)</p>
<p class="p1"><span class="Apple-converted-space">    </span>if st.button('Generate Word Cloud'):</p>
<p class="p1"><span class="Apple-converted-space">        </span># Assuming the column with text is named 'Description'</p>
<p class="p1"><span class="Apple-converted-space">        </span>buffer = generate_word_cloud(data, 'Description')</p>
<p class="p1"><span class="Apple-converted-space">        </span>st.image(buffer, use_column_width=True)</p>
</body>
</html>
    ( > \ k � � � � � �                           �