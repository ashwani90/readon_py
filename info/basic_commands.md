Launch the project 

python3 manage.py runserver

create super user
python3 manage.py createsuperuser

create new app
python3 manage.py startapp readpro

Generate and Run migrations 

    python manage.py makemigrations readpro
    python manage.py migrate

Register your models for admin in admin.py file to show them in admin

We are using pytesseract library to read text fromimages

pip install pytesseract (We need to install pil and image first)

Code to read text from image file 

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
print(pytesseract.image_to_string(r'D:\examplepdf2image.png'))

Now to implement in django we need to first install OCR in our server or system

sudo apt install tesseract-ocr
sudo apt install libtesseract-dev

