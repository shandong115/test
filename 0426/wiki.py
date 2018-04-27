from gensim.corpora.wikicorpus import extract_pages,filter_wiki
import bz2file
import re
from opencc import OpenCC
from tqdm import tqdm
import codecs
import sys

if len(sys.argv)<3:
	print("argc less 3")
	sys.exit(1)

inp, outp = sys.argv[1:3]
print("inp file:%s" % inp)
print("outp file:%s" % outp)

wiki = extract_pages(bz2file.open(inp))
c = OpenCC('t2s')

def wiki_replace(d):
	s = d[1]
	s = re.sub(':*{\|[\s\S]*?\|}', '', s)
	s = re.sub('<gallery>[\s\S]*?</gallery>', '', s)
	s = re.sub('(.){{([^{}\n]*?\|[^{}\n]*?)}}', '\\1[[\\2]]', s)
	s = filter_wiki(s)
	s = re.sub('\* *\n|\'{2,}', '', s)
	s = re.sub('\n+', '\n', s)
	s = re.sub('\n[:;]|\n +', '\n', s)
	s = re.sub('\n==', '\n\n==', s)
	s = u'【' + d[0] + u'】\n' + s
#print("string:%s" % s)
#return opencc.convert(s).strip()
	return c.convert(s).strip()

i = 0
f = codecs.open(outp, 'w', encoding='utf-8')
w = tqdm(wiki, desc=u'已获取0篇文章')
for d in w:
	if not re.findall('^[a-zA-Z]+:', d[0]) and d[0] and not re.findall(u'^#', d[1]):
		s = wiki_replace(d)
		f.write(s+'\n\n\n')
		i += 1
		if i % 100 == 0:
			w.set_description(u'已获取%s篇文章'%i)

f.close()


#pip install gensim
#pip install opencc-python-reimplemented
#pip install tqdm
#python wiki.py zhwiki-20180401-pages-articles-multistream.xml.bz2 wiki_zh_tw.txt
