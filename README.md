# auto_contents 自动生成英文目录
Auto_Contents是一个Python脚本，它基于学位论文的中文目录自动生成**英文目录**。该脚本还包括自动生成**英文摘要**和**英文图表标题**的功能。

## 用法：
1. 安装依赖

在运行该项目前，请先安装python-docx库。
```shell
pip install python-docx 
```
2. 替换文件路径和选择翻译器

在运行main.py之前，需要将main.py中的文件路径替换为你的学位论文的路径。在main.py中，将以下代码中的/path/to/your/thesis.docx替换为你的论文路径。

```python
doc = docx.Document(r"/path/to/your/thesis.docx")
```
然后选择翻译器，如果使用谷歌则使用'google'，如果使用deepl则使用'deepl'。
```python
translation_service='deepl'
```
3. 运行项目

在替换文件路径和API密钥之后，直接运行main.py即可。运行完毕后，会生成一个新的Word文档translated_docx_file.docx，其中包含了翻译后的内容。而且代码是只读的，所以不用担心会对原文档进行修改。
```python
python main.py
```
## 注意事项
 - 本项目有谷歌和deepl两种翻译器，如果选择deepl需要使用你自己的deepl API密钥。

 将translation.py中的API密钥（如下a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx）替换为你自己的API密钥。

 ```python
 'auth_key': 'a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx',# deepl的API密钥
 ```
 
 如果没有deepl API密钥，请先到deepl官网注册并获取API密钥。

 - 本项目目前只支持将中文翻译为英语。如果需要将其他语言翻译为某个语言，需要修改translation.py中的源语言和目标语言参数。

 - 在运行本项目时，请确保网络连接正常。

## 未来：

1. 一开始我只是想要能够根据中文目录自动生成英文目录，后来又加入了自动生成英文摘要和英文图表标题的功能。未来会加入更多功能。

2. 目前只是针对我所在学校的学位论文模板，不一定适用你的学校的学位论文，可以根据我的代码进行修改，里面的注释很详细。

3. 未来准备使用openai的翻译，也就是接入chatgpt。
