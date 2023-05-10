import re
import requests
from docx.styles.style import BaseStyle
from docx.document import Document
from docx.text.paragraph import Paragraph
from docx.oxml.xmlchemy import OxmlElement
from googletrans import Translator

def translate_paragraph(para, translation_service='google'):
    if translation_service == 'deepl':
        # 使用deepl翻译
        url = 'https://api-free.deepl.com/v2/translate'
        params = {
            'auth_key': 'a8da6371-ffa2-ba70-9aa1-d1fa6577d8b8:fx',# deepl的API密钥
            'text': para.text,
            'target_lang': 'EN',
            'source_lang': 'ZH'
        }
        response = requests.post(url, data=params)
        if response.status_code == 200:
            result = response.json()['translations'][0]['text']
            return result
        else:
            print('翻译失败！错误代码：', response.status_code)
    elif translation_service == 'google':
        # 使用谷歌翻译
        translator = Translator()
        result = translator.translate(para.text, src='zh-cn', dest='en')
        return result.text
    else:
        print('不支持的翻译服务！')