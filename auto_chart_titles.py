import re
import docx
import requests
from docx import Document
from docx.text.paragraph import Paragraph
from docx.oxml.xmlchemy import OxmlElement
from utils import insert_paragraph_after
from translation import translate_paragraph



# 遍历段落并删除已经存在的英文图表标题
def remove_existing_fig_table_title(doc):
    fig_pattern = re.compile(r'^Fig\.\s*\d+')
    table_pattern = re.compile(r'^Table\s*\d+')
    for para in doc.paragraphs:
        if fig_pattern.match(para.text) or table_pattern.match(para.text):
            p = para._element
            p.getparent().remove(p)
            p._p = p._element = None

def translate_fig_table_title(doc,translation_service):
    remove_existing_fig_table_title(doc)
    # 获取所有段落
    paragraphs = doc.paragraphs

    # 遍历所有段落
    for para in paragraphs:
        #跳过“图55 表15 参 80”
        if para.text.find("图") != -1 and para.text.find("表") != -1 and para.text.find("参") != -1:
            continue
        # 判断段落是否以“图”或“表”开头
        if (para.text.startswith("图") or para.text.startswith("表")) and not para.text[-1].isdigit():
            # 段落不以“。”或“.”或“页码”结尾
            if not para.text.endswith("。") and not para.text.endswith(".") :
                print(para.text)
                result = translate_paragraph(para,translation_service)
                # 把“Figure 1”替换为“Fig.1”
                if re.match(r'^Figure\s*\d+', result):
                        result = re.sub(r'^Figure\s*', 'Fig.', result)
                # 把“Table 1”替换为“Table1”
                if re.match(r'^Table\s*\d+', result):
                        result = re.sub(r'^Table\s*', 'Table', result)      
                print(result)
                Chart_Title_style = doc.styles['图表标题']
                insert_paragraph_after(para,text=result,style=Chart_Title_style)
                # para.insert_paragraph_before(result)
            
    


