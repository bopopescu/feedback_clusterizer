import spacy
# from nltk.tokenize import word_tokenize as wt, sent_tokenize as st

spa_nlp = spacy.load('pt_core_news_sm') #instalar modulo de lingua portuguesa no terminal $ python -m spacy download pt

texto = 'Hoje fui a feira comprar lindas maçãs. Depois fui ao mercado comprar cerveja. Como é um lindo dia, bebi a cerveja e levei o cachorro para passear.'


doc = spa_nlp(texto)

print(doc.text.split()) #simplestemente quebra o texto dividido por espacço(' ')

for t in doc:
    print(t.orth_) # como string
    print(t) # tipo token

for t in doc:
    if not t.is_punct: # .is_punct classificacao do token como pontuacao
        print(t.orth_)

tokens = [token for token in doc] # if not token.is_punct] # tira as pontuaçoes
#
for i in range(len(tokens)):
    print (i, end = " ")
    print (tokens[i])
    print('clsse gramatical= ',tokens[i].pos_) # .po_ devolve classe gramatical
    print('lema = ',tokens[i].lemma_)
    print('dep = ', tokens[i].dep_)
#
print(tokens[14].similarity(tokens[6]))  # analise de similaridade semantica

doc2 = spa_nlp(u'encontrar lixo')

t_list = [token for token in doc2]

print(t_list[0].is_ancestor(t_list[1]))  #devolve true/false se [0] é raiz de [1], nesse caso

doc3 = spa_nlp(u'Jair Bolsonaro é um pessimo presidente para o Brasil.')
print(doc3.ents)

ents = [entity for entity in doc3.ents]

for k in range(len(ents)):
    print(ents[k], ents[k].label_)
