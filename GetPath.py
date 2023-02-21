import os

# Module to retrieve the paths 
#tesseract executable
def get_tesseract_exe():
    return r'C:\Users\dell\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

#poppler binary path
def get_poppler_bin():
    return r'C:\poppler-0.68.0_x86\poppler-0.68.0\bin'

#Main storage of the PDF files
def get_form_folder_path():
    path = 'C:\\Users\\dell\\Documents\\Capstone\\Capstone'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

#path to store the converted PDF to JPG
def get_converted_img_path():
    path = 'C://Users//dell//Documents//Capstone//TempImgs//'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

#path to move PDF incase of exception
def get_exception_pdf_path():
    path = 'C://Users//dell//Documents//Capstone//Exception//'
    if not os.path.exists(path):
        os.makedirs(path)
    return path

def log_file_path():
    return 'C://Users//dell//Documents//Capstone//Logs//Log.txt'

def get_forms():
    forms = {
    "Cancellation Form": "C:\\Users\\dell\\Documents\\Capstone\\Cancellation",
    "Quotation Form" : "C:\\Users\\dell\\Documents\\Capstone\\Quotation",
    "Client Data Form" : "C:\\Users\\dell\\Documents\\Capstone\\ClientData",
    "Referral Form" : "C:\\Users\\dell\\Documents\\Capstone\\Referral"
    }
    return forms

def get_form_types():
    forms_types = ["Cancellation Form","Quotation Form","Client Data Form","Referral Form"]
    return forms_types