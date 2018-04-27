# -*- coding: utf-8 -*-
from opencc import OpenCC
import codecs,sys
import logging
logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s', level=logging.INFO)
'''
    extract data from wiki dumps(*articles.xml.bz2) by gensim.
    @chenbingjin 2016-05-11
'''
def help():
    print("Usage: python fan2jian.py zhwiki-tw.txt wiki.zh.txt")

if __name__ == '__main__':
    if len(sys.argv) < 3:
        help()
        sys.exit(1)
    logging.info("running %s" % ' '.join(sys.argv))
    inp, outp = sys.argv[1:3]
    i = 0

    f = codecs.open(inp, 'r', encoding="utf8")
    output = open(outp, 'w')
    c = OpenCC('t2s')
    line= f.readline()
    while(line):
        new_line = c.convert(line)
        output.write(new_line)
        line = f.readline()
        i = i + 1
        if (i % 10000 == 0):
            logging.info("Save "+str(i) + " articles")
    output.close()
    logging.info("Finished saved "+str(i) + "articles")
