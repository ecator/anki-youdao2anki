# -*- coding: UTF-8 -*-

import xml.sax
import sys
import re
from xml.dom.minidom import parse
import xml.dom.minidom
reload(sys)  
sys.setdefaultencoding('utf8')

origin='origin.xml'
print sys.argv
if len(sys.argv)>1 and sys.argv[1]!='': origin=sys.argv[1]
# 使用minidom解析器打开 XML 文档
DOMTree = xml.dom.minidom.parse(origin)
collection = DOMTree.documentElement

# 在集合中获取所有item
items = collection.getElementsByTagName("item")

# 遍历每个item的详细信息
Items=''
for item in items:
   Word=Phonetic=Trans=''
   word = item.getElementsByTagName('word')[0]
   if word.hasChildNodes(): Word = word.firstChild.data.replace('\n','<br>')
   phonetic = item.getElementsByTagName('phonetic')[0]
   if phonetic.hasChildNodes(): Phonetic = phonetic.firstChild.data.replace('\n','<br>')
   trans = item.getElementsByTagName('trans')[0]
   if trans.hasChildNodes(): Trans = trans.firstChild.data.replace('\n','<br>')
   Item=Word+'\t'+Phonetic+'\t'+Trans
   print '解析 %s'%Item
   if Items=='':
      Items=Item
   else:
      Items+='\n'+Item

#处理换行符，替换不同词性之间添加<br>标签
def handleBrTag(matched):
   #print matched.group()
   return matched.group().replace(' ','<br>',1)

patt=r'( (adj\.))|( (n\.))|( (adv\.))|( (prep\.))|( (pron\.))|( (v\.))|( (conj\.))|( (vi\.))|( (vt\.))|( (pl\.))|( (c\.))|( (num\.))'
Items=re.sub(patt,handleBrTag,Items)

#保存文件
print '解析完成，一共解析 %d 条数据'%len(items)
fileName=raw_input('请输入保存文件名(不输入则保存为out.txt)：')
if not fileName:
	fileName="out.txt"
try:
   f=open(fileName,'w')
   f.write(Items)
except Exception as e:
   print '保存文件 %s 失败'%fileName
else:
   print '保存文件 %s 成功'%fileName
finally:
   f.close()
sys.exit(0)