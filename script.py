from docx import Document
from docx.shared import Pt

def text_changer(file_names):
    for name in file_names:
        file_path = f'{name}'
        new_file_path = f'{name[:-5]}_new.docx'
        document = Document(file_path)
        for paragraph in document.paragraphs:
            paragraph.style.font.name = 'Times New Roman'
            paragraph.style.paragraph_format.line_spacing = 1.5
            paragraph.style.font.size = Pt(14)
        document.save(new_file_path)

file_names = ['1.docx', '2.docx', '3.docx', '4.docx', '5.docx']
text_changer(file_names)