from translation import translate_paragraph
from utils import insert_paragraph_after, delete_paragraph
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.shared import Cm
import re
# 删除已经存在的abstract

def delete_abstract(paragraphs):
    found_abstract = False
    for i,paragraph in enumerate(paragraphs):
        text = paragraph.text.strip()
        if text.startswith("Abstract"):
            abstract_index = i
            found_abstract = True
        elif found_abstract and "Figure" in text and "Table" in text and "Reference" in text:
            insert_paragraph_after(paragraphs[abstract_index], text=" ", style=None,tab_stops_position=None)
            break
        elif found_abstract:
            delete_paragraph(paragraph)
            
    return abstract_index  

def translate_abstract(doc,translation_service):
    abstract_index = delete_abstract(doc.paragraphs)

    paragraphs = doc.paragraphs  # 获取所有段落
    
    # 初始化标志变量
    is_contents = False
    found_zhaiyao = False
    for i, para in enumerate(paragraphs):
        # 找到摘要
        if para.text.find("摘　　要") != -1:
            found_zhaiyao = True
            # print("found_zhaiyao = ",found_zhaiyao)
            continue
        # 判断段落样式
        elif found_zhaiyao  and re.match(r'^图\s*\d+\s*表\s*\d+\s*参\s*\d+$',para.text.strip()):
            found_zhaiyao =False
            break
        elif found_zhaiyao :
            # print(para.style)
            print(para.text)
            result = translate_paragraph(para,translation_service)
            print(result)
            Contents_style = doc.styles["Normal"]
            paragraphs[abstract_index+1].insert_paragraph_before(result, Contents_style)

        