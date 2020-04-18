# ================ BEGIN Lybrary Imports: ========================#

from nltk.tokenize import word_tokenize,sent_tokenize
from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.stem.snowball import SnowballStemmer
from string import punctuation

# ================ END Lybrary Imports: =========================#

# ================ BEGIN Tokenization Tests: ====================#

# Split words:

text = "Bom dia! O meu nome e Eric, gostei bastante do servico e das comidas. Apesar de peixe ser uma comida nao recomenada nas segundas. Nao gosto de peixe"

setences = sent_tokenize(text)
words = word_tokenize(text.lower())

#print('text: ',text,'\n')
#print('setences: ',setences,'\n')
#print('words: ',words,'\n')


# Stopwords
stopwords = set(stopwords.words('portuguese') + list(punctuation))
#print(stopwords,"\n")

words_without_stopwords = [word for word in words if word not in stopwords ]

print('WORDS WITHOUT STOPWORDS:')
print(words_without_stopwords)

# Frequency of distribuition 

frequency = FreqDist(words_without_stopwords)
print('frequency: ',frequency)

# Stemming

stemmer = SnowballStemmer('portuguese')
#print(stemmer.stem("correndo pulando e alegria"))
print(stemmer.stem("corrida"))
print(stemmer.stem("pulando"))
print(stemmer.stem("pular"))
#print(stemmer.stem(words_without_stopwords))

# Lema 

# ================ END Tokenization Tests: =====================#