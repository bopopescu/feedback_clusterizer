import pandas as pd
import spacy
from spacy.matcher import Matcher
from spacy.lang.pt import Portuguese

data_raw = pd.read_excel('data1.xlsm',sheet_name='Result',index_col=0)
# print(data_raw.columns)

content = data_raw[['Content']].dropna()
# print(content.head())

# spacy_nlp = spacy.load('pt_core_news_sm')
spacy_nlp = Portuguese()
# doc = spacy_nlp(content.iloc[0]['Content'])

# for token in doc:
#     print(f'text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, head text: {token.head.text}')
# ent -> ent.text, ent.label_
# creating
# spacy.explain('x') - explica o que significa tal classificação ex.: 'dobj' - firect object
# print(spacy.explain('PROPN'))


doc1 = list(spacy_nlp.pipe(content['Content']))

# for d in doc1:
#     print(d)
#     for token in d:
#         print(f'text: {token.text}, pos: {token.pos_}, dep: {token.dep_}, head text: {token.head.text}')


matcher = Matcher(spacy_nlp.vocab)
pattern1 = [{'LOWER': 'ambiente'},{'LOWER':'muito','OP':'?'},{'LOWER':'bom'}]
matcher.add('Ambiente bom', None, pattern1)
pattern2 = [{'LOWER':'otima','OP':'?'},{'LOWER': 'bebida'},{'LOWER':'é','OP':'?'},{'LOWER':'boa','OP':'?'},{'LOWER':'bem','OP':'?'},{'LOWER':'gelada','OP':'?'}]
matcher.add('bebida boa', None, pattern2)

for doc in doc1:
    list=[doc[start:end] for match_id, start, end in matcher(doc)]
    if list:
        print(list,sep=',')


stop_words=spacy.lang.pt.stop_words
#print(stop_words.STOP_WORDS)

# for doc in doc1:
#     print(doc)
#     tokens = [token.text for token in doc if not (token.is_stop and token.is_punct and token.is_space)]
#     print(tokens)
