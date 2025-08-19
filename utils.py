import pdfplumber
import warnings
import pytesseract
import unicodedata
from PIL import Image
from pathlib import Path
from pdf2image import convert_from_path

warnings.filterwarnings("ignore")


def read_pdf(file_path, start_page, as_img: bool):
    """
    reads the pdf and saves as txt files or images
    """
    pdf_path = Path(file_path)
    dest_path_img = Path("pdf_img")
    dest_path_txt = Path("pdf_txt")

    if as_img == False:
        dest_path_txt.mkdir(exist_ok=True)
        with pdfplumber.open(pdf_path, repair=True) as pdf:
            for page in pdf.pages:
                if page.page_number <= start_page: 
                    pass
                else:
                    file = Path(dest_path_txt/f"page_{page.page_number}.txt")
                    file.touch()
                    file.write_text(page.extract_text())
    else:
        dest_path_img.mkdir(exist_ok=True)
        convert_from_path("bini_dict.pdf", output_folder=dest_path_img, fmt="png")
                

def prepare_normalized():
    """
    prepare normalized NFC text for training tesseract model
    """
    with open("bini_training.txt", "r", encoding="utf-8") as f:
        text = f.read()

    with open("normalized_training.txt", "w", encoding="utf-8") as f:
        normalized = unicodedata.normalize("NFC", text)
        f.write(normalized)


def write_txt_from_image():
    """
    write the contents read from the pdf images with post trained tesseract model
    """
    i = 0
    for img in Path("bini_pdf_as_img").glob("*.png"):
        img = Image.open(img)
        test = Path(f"proper_{i}.txt")
        test.touch()
        text = pytesseract.image_to_string(img)
        test.write_text(text)
        i += 1


if __name__ == "__main__":
    pass