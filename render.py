import os
from dotenv import load_dotenv
from weasyprint import HTML

load_dotenv()

try:
    os.makedirs("./render")
except:
    None

try:
    os.remove("./render/resume-DEI.pdf")
except:
    None

html = HTML(filename="./index.html")
html.write_pdf(target="./render/resume-DEI.pdf")

html.write_pdf(target=os.path.join(os.environ['RENDER_TO'], "./resume-DEI.pdf"))
