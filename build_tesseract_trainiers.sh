git clone https://github.com/tesseract-ocr/tesseract.git
cd tesseract

./autogen.sh
./configure
make
sudo make install
sudo ldconfig
make training
sudo make training-install
