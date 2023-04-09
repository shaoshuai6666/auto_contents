from docx.oxml.xmlchemy import OxmlElement
from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
from docx.shared import Cm
from docx.text.paragraph import Paragraph

# 在当前段落后面插入段落
def insert_paragraph_after(paragraph, text=None, style=None,tab_stops_position=None):
    """Insert a new paragraph after the given paragraph."""
    new_p = OxmlElement("w:p")
    paragraph._p.addnext(new_p)
    new_para = Paragraph(new_p, paragraph._parent)
    if text:
        new_para.add_run(text)
    if style is not None:
        new_para.style = style
    if tab_stops_position is not None:
        new_para.paragraph_format.tab_stops.add_tab_stop(tab_stops_position,alignment = WD_TAB_ALIGNMENT.RIGHT, leader = WD_TAB_LEADER.DOTS)
    return new_para

# 删除
def delete_paragraph(paragraph):
    p = paragraph._element
    p.getparent().remove(p)
    paragraph._p = paragraph._element = None


