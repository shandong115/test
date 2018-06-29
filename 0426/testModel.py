from gensim.models import Word2Vec
import sys

model = sys.argv[1]
word2vec_model = Word2Vec.load(model)

testwords = ['苹果','数学','学术','白痴','篮球','中国','汽车','水杯','china','大有']

for i in range(len(testwords)):
	res = word2vec_model.most_similar(testwords[i])
	print("word:%s" % testwords[i])
	print("res:%s" % res)
