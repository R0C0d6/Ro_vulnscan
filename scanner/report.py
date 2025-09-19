# scanner/report.py
import jinja2
import pdfkit
from datetime import datetime
import os

TEMPLATE_DIR = os.path.join(os.path.dirname(__file__), "..", "templates")

def render_html(report_data, out_path="report.html"):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    tpl = env.get_template("report_template.html")
    html = tpl.render(report=report_data, generated_at=datetime.utcnow().isoformat()+"Z")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(html)
    return out_path

def render_pdf(html_path, pdf_path="report.pdf"):
    # requires wkhtmltopdf installed or configured for pdfkit
    pdfkit.from_file(html_path, pdf_path)
    return pdf_path
