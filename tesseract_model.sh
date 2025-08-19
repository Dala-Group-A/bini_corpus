#!/bash

# install tesseract and others for linux
# sudo apt install tesseract-ocr -y
# sudo apt install tesseract-ocr-eng -y
# sudo apt install tesseract-ocr-script-latn -y
# sudo apt install tesseract-ocr-script-grek -y
# sudo apt install training-tools -y # you'll have to build from source via

# creating training images
text2image \
    --fonts_dir=/usr/share/fonts \
    --font="Courier Prime Sans" \
    --text=bini.training_text \
    --outputbase=bini.exp0 \
    # --lang=eng

# creating training data
tesseract bini.exp0.tif bini.exp0 --psm 6 lstm.train

# train with tesseract
combine_lang_model \
    --input_dir . \
    --lang bini \
    --output_dir /. \
    --langdata_dir /usr/share/tesseract-ocr/4.00/tessdata \
    --tessdata_dir /usr/share/tesseract-ocr/4.00/tessdata_best \
    --script_dir /usr/share/tesseract-ocr/4.00/tessdata \
    --training_text bini.training_text \
    --wordlist bini.training_wordlist \
    --fonts_dir /usr/share/fonts