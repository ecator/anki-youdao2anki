#coding=utf-8
import re

f=open('English.txt')
content=f.read()
f.close()

def handleText(matched):
	#print matched.groups()
	return matched.group().replace(' ','<br>',1)

patt=r'( (adj\.))|( (n\.))|( (adv\.))|( (prep\.))|( (pron\.))|( (v\.))|( (conj\.))|( (vi\.))|( (vt\.))|( (pl\.))|( (c\.))|( (num\.))'
print re.sub(patt,handleText,content)