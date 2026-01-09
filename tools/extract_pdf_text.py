from PyPDF2 import PdfReader
import sys
from pathlib import Path

pdf_path = Path(__file__).resolve().parents[1] / 'resume' / 'Manpreet Kaur Analyst Detailed CV.pdf'
out_path = Path(__file__).resolve().parents[1] / 'resume' / 'resume_text.txt'

if not pdf_path.exists():
    print(f'PDF not found at {pdf_path}')
    sys.exit(1)

reader = PdfReader(str(pdf_path))
text_parts = []
for page in reader.pages:
    try:
        text_parts.append(page.extract_text() or '')
    except Exception as e:
        text_parts.append('')

full_text = '\n\n'.join(text_parts)
with open(out_path, 'w', encoding='utf-8') as f:
    f.write(full_text)

print(f'Extracted text written to: {out_path}')
