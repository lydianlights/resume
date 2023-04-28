import os
from weasyprint import HTML

try:
    os.makedirs("./render")
except:
    None

try:
    os.remove("./render/resume.pdf")
except:
    None

html = HTML(filename="./index.html")
html.write_pdf(target="./render/resume.pdf")
