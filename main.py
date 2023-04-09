import docx
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.shared import Cm
from translation_deepl import translate_paragraph
from utils import insert_paragraph_after, delete_paragraph
from auto_chart_titles import translate_fig_table_title
from auto_contents import translate_contents
from auto_abstract import translate_abstract
#翻译英文图表标题
fig_table = False

# 输入Word文档
doc = docx.Document(r"")

#翻译摘要
print("开始翻译摘要")
translate_abstract(doc)

#翻译目录
print("开始翻译目录")
translate_contents(doc)

#翻译图表标题
print("翻译图表标题")
translate_fig_table_title(doc)

# 保存修改后的文档
doc.save("translated_docx_file.docx")
print("翻译后的word保存为：translated_docx_file.docx")

