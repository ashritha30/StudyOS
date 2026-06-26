from pypdf import PdfReader
from skills.summarize_skill import summarize_text

def extract_text_from_pdf(uploaded_file):

    pdf = PdfReader(uploaded_file)

    text = ""

    for page in pdf.pages:

        page_text = page.extract_text()

        if page_text:
            text += page_text + "\n"

    return text


def get_summary(uploaded_file):

    text = extract_text_from_pdf(uploaded_file)

    return summarize_text(text)