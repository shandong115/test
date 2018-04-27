import jieba
import jieba.analyse
import jieba.posseg as pseg
import codecs, sys

def cut_words(sentence):
	return " ".join(jieba.cut(sentence)).encode('utf-8')

if __name__ == '__main__':
	if len(sys.argv)!=3:
		print("argv!=3")
		sys.exit(1)

	inp,outp = sys.argv[1:3]

	f = codecs.open(inp, 'r', encoding="utf8")
	target = codecs.open(outp, 'w', encoding="utf8")
	print("open files")

	line_num = 1
	line = f.readline()
	while(line):
		print('------processing ', line_num, ' article----------')
		line_seg = " ".join(jieba.cut(line))
#line_seg = cut_words(line)
		target.writelines(line_seg)
		line_num = line_num + 1
		line = f.readline()
	f.close()
	target.close()
	sys.exit()
