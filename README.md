# youdao2anki.py

此脚本可以批量转换有道词典导出的xml格式生词本到Anki格式的纯文本文件

## 运行环境

Python环境，推荐linux系统

## 使用方法

将有道词典导出的xml文件和本脚本放入同一目录，然后运行

```
python youdao2anki.py filename
```

后面的filename是可选参数，为需要转换的xml文件名，默认为origin.xml，之后脚本会自动解析，最后提示输入保存的文件名后即可完成转换

> 推荐最后保存为.txt文件

## 提取字段

本脚本只提取三个字段，以制表符分隔每个字段

- word 单词
- phonetic 音标
- trans 译文

# index.html

此为youdao2anki的web版本全平台通用:smile:

[YD2Anki传送门](http://yd2anki.nocode.site)

> web版本只有一个index.html文件，只用一个静态服务器甚至本地就能运行:clap:

