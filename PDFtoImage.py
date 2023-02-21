from pdf2image import convert_from_path 
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError
)
import pytesseract
from PIL import Image
from datetime import datetime
import os
from GetPath import get_form_folder_path, get_converted_img_path, get_tesseract_exe,get_poppler_bin
import EventLog


def pdf_to_image():
    pytesseract.pytesseract.tesseract_cmd = get_tesseract_exe()
    pdf_doc_count = 0
    pdf_folder_path=get_form_folder_path()
    pdf_to_img_folder = get_converted_img_path()
    #Taking the first page of the PDF with the title
    pg_cntr = 1

    #Code is kept in try catch block in case of poppler not installed or 
    # the correct poppler bin path is not defined
    try:
        for pdf_doc in os.listdir(pdf_folder_path):
            pdf_doc_count +=1
            full_path = pdf_folder_path + '\\' + pdf_doc
            #This will convert the PDF into a image.
            converted_img=convert_from_path(full_path, poppler_path = get_poppler_bin()) 
            filename = "temp_img_"+pdf_doc.replace('.pdf','.jpg') 
            #Here we are going to take the first image of the converted images (incase of more than one page in PDF) 
            # and will move it to the temporary image folder
            for temp, tempImg in enumerate(converted_img):
                if temp == 0:
                    tempImg.save(pdf_to_img_folder+filename)
        EventLog.EventLogger.write("TOTAL SCANNED DOCUMENTS: "+str(pdf_doc_count)+"\n")
    except OSError:
        EventLog.EventLogger.write("pdf2image EXCEPTION, PDFInfoNotInstalledError"+"\n")
        raise PDFInfoNotInstalledError

    except ValueError:
        EventLog.EventLogger.write("Value Error, PDF page count error"+"\n")
        raise PDFPageCountError