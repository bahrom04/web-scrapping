import json 
from PyPDF2 import PdfReader
from pdfminer.high_level import extract_text as fallback_text_extraction

text = ""
try:
    reader = PdfReader("dtm.pdf")
    for page in reader.pages:
        text += page.extract_text()
except Exception as exc:
    text = fallback_text_extraction("dtm.pdf")


student_data = [
    "ID",
    "F.I.Sh.:",
    "Pasport:",
    "Tug‘ilgan sana:",
    "Test topshirish fanlari:",
    "Test sinovi topshirish hududi va hududga kelish vaqti:",
    "Test topshirish manzili:",
    "Test topshirish joyi nomi:",
    "Smena:",
    "Sektor raqami:",
    "Guruh raqami:",
    "Ta'lim shakli:",
    "Ta'lim tili:",
    "Test topshirish alifbosi:",
]


result = {}
for i in range(0, len(student_data) - 1, 1):
    start_index = text.index(student_data[i])
    end_index = text.index(student_data[i+1])
    row = text[start_index:end_index].replace(student_data[i], "").replace('\n', '')
    result[student_data[i]] = row


with open("sample.json", "a") as outfile: 
    json.dump(result, outfile)
