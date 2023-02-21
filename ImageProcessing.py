import os
from GetPath import get_converted_img_path, get_form_folder_path, get_exception_pdf_path
import shutil
from identifyingMRZ import identify_MRZ

converted_img_path = get_converted_img_path()

#Method to move the PDF to the respective folder, it takes 3 parameters:
#  1.Image name
#  2.exception_pdf:A bool value to check whether any exception was raised while identifying the MRZ
#  3.new_path: it will be empty in case of the exception
def move_pdf(image_name, exception_pdf,new_path):
    source=''
    destination=''
    print("inside move_pdf ",image_name," ",new_path," flag ",exception_pdf)
    pdf_file_name = get_pdf_name(image_name)
    #incase of any exception, we will move the PDF to exception folder 
    # else it will be moved to the new path returned by MRZ
    if exception_pdf:
       source = get_form_folder_path()+"\\{}.pdf".format(pdf_file_name)
       destination = get_exception_pdf_path()+"\\{}.pdf".format(pdf_file_name) 
    else:
        source = get_form_folder_path()+"\\{}.pdf".format(pdf_file_name)
        destination = new_path+"\\{}.pdf".format(pdf_file_name)
    shutil.move(source,destination)

#To get the original PDF name by removing the prefix and suffix from the image name.
def get_pdf_name(image_name):
    pdf_file_name = image_name.removeprefix("temp_img_").removesuffix(".jpg")
    return pdf_file_name

#Call to identify the MRZ is sent from here, then the file is moved to the path 
# returned by the identify_MRZ method
def image_processing():
    new_path=''
    for img in os.listdir(converted_img_path):
        try:
            new_path = identify_MRZ(img)
            print(img," ",new_path)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            
            move_pdf(img,False, new_path)
        except:
            move_pdf(img,True,'')