import re
import requests
from docx.styles.style import BaseStyle
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.oxml.xmlchemy import OxmlElement

# deepl的API密钥
API_KEY = 'a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx'#'your_api_key'
# 要翻译的目标语言代码（例如，中文是'zh'）
target_lang = 'en'

#使用deepl的API进行翻译
def translate_paragraph(para):

    
    



    # 构建API请求
    url = 'https://api-free.deepl.com/v2/translate'
    params = {
        'auth_key': API_KEY,
        'text': para.text,
        'target_lang': target_lang
    }
    response = requests.post(url, data=params)
    # 解析API响应并返回翻译结果
    if response.status_code == 200:
        result = response.json()['translations'][0]['text']
        return result
    else:
        print('翻译失败！错误代码：', response.status_code)