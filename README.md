# auto_contents 自动生成英文目录
Auto_Contents是一个Python脚本，它基于学位论文的中文目录自动生成**英文目录**。该脚本还包括自动生成**英文摘要**和**英文图表标题**的功能。

## 用法：
1. 安装依赖

在运行该项目前，请先安装python-docx库。
```shell
pip install python-docx 
```
2. 替换文件路径和API密钥

在运行main.py之前，需要根据自己的实际情况替换两个文件中的路径和API密钥。

将main.py中的文件路径替换为你的学位论文的路径。在main.py中，将以下代码中的/path/to/your/thesis.docx替换为你的论文路径。
```shellgit
doc = docx.Document(r"/path/to/your/thesis.docx")
```
将translation_deepl.py中的API密钥替换为你自己的API密钥。在translation_deepl.py中，将以下代码中的a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx替换为你的API密钥。
```shell
API_KEY = 'a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx'#'your_api_key'
```
3. 运行项目

在替换文件路径和API密钥之后，直接运行main.py即可。运行完毕后，会生成一个新的Word文档translated_docx_file.docx，其中包含了翻译后的内容。而且代码是只读的，所以不用担心会对原文档进行修改。
```shell
python main.py
```
## 注意事项
 - 本项目使用deepl API进行翻译，因此需要使用deepl API密钥。如果没有deepl API密钥，请先到deepl官网注册并获取API密钥。

 - 本项目目前只支持将中文翻译为英语。如果需要将其他语言翻译为某个语言，需要修改translation_deepl.py中的源语言和目标语言参数。

 - 在运行本项目时，请确保网络连接正常。

## 未来：

1. 一开始我只是想要能够根据中文目录自动生成英文目录，后来又加入了自动生成英文摘要和英文图表标题的功能。未来会加入更多功能。

2. 目前只是针对我所在学校的学位论文模板，不一定适用你的学校的学位论文，可以根据我的代码进行修改，里面的注释很详细。

3.  还有使用的是deepl的翻译api，未来准备使用openai的翻译，也就是接入chatgpt。
