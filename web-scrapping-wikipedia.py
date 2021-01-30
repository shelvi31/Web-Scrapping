import re
import nltk
import urllib
import bs4
from nltk.corpus import stopwords
nltk.download("stopwords")
nltk.download('punkt')
from nltk import word_tokenize,sent_tokenize

#getting the data source
source = urllib.request.urlopen("https://en.wikipedia.org/wiki/Climate_change").read()

#parsing data / creating beautiful soup object
soup = bs4.BeautifulSoup(source,"html.parser")

#fetching the data
text = ""
for paragraph in soup.find_all("p"):
    text += paragraph.text

#preprocessing the data, removing other insignificant 
text = text.lower()
text = re.sub(r"\[[0-9]*\]","",text)

#removing extra spaces
text = re.sub(r"\s+"," ",text)

#parsing as sentences
sentences = nltk.sent_tokenize(text)

#parsing as words
sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
print(sentences)


