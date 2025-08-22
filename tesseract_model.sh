#!/bin/bash

# install tesseract and others for linux
# sudo apt install tesseract-ocr -y
# sudo apt install tesseract-ocr-eng -y
# sudo apt install tesseract-ocr-script-latn -y
# sudo apt install tesseract-ocr-script-grek -y
# sudo apt install training-tools -y # you'll have to build from source via

# creating training images
# courier prime sans cannot render the fonts hence noto sans for now is the way forward
text2image \
    --text tessa_data/bini.training_text \
    --outputbase bini.exp0 \
    --font "Noto Sans" \
    --strip_unrenderable_words false \
    --D ./tessa_data/ \
    --U bini.unicharset \
    --unicharset_file bini.unicharset \
    --fonts_dir /usr/share/fonts \
    

# creating training data
tesseract bini.exp0.tif bini.exp0 --psm 6 lstm.train

# train with tesseract
combine_lang_model \
    --lang bini \
    --output_dir /. \
    --training_text bini.training_text \
    --wordlist bini.training_wordlist \
    --input_unicharset bini.unicharset \
    --fonts_dir /usr/share/fonts \
    --langdata_dir /usr/share/tesseract-ocr/4.00/tessdata \
    --tessdata_dir /usr/share/tesseract-ocr/4.00/tessdata_best \
    --script_dir /usr/share/tesseract-ocr/4.00/tessdata \