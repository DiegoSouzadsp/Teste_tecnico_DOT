import sys
import os

pdf_path = "Prova - Backend IA.pdf"

if not os.path.exists(pdf_path):
    print(f"File not found: {pdf_path}")
    sys.exit(1)

try:
    import pypdf
    reader = pypdf.PdfReader(pdf_path)
    text = ""
    for page in reader.pages:
        text += page.extract_text() + "\n"
    # Write to a file to avoid console encoding issues
    with open("pdf_content.txt", "w", encoding="utf-8") as f:
        f.write(text)
    print("SUCCESS")
except ImportError:
    try:
        import PyPDF2
        reader = PyPDF2.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        with open("pdf_content.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("SUCCESS")
    except ImportError:
        print("MISSING_LIBS")
    except Exception as e:
        print(f"ERROR: {e}")
except Exception as e:
    print(f"ERROR: {e}")
