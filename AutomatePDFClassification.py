from PDFtoImage import pdf_to_image
from ImageProcessing import image_processing
import EventLog
from datetime import datetime
from folder_auditing import audit_forms

message = "=========AutomatePDFClassification Started: "+ str(datetime.today().strftime('%Y-%m-%d %H:%M:%S')+"========="+ "\n")
EventLog.EventLogger.write(message)


# print('error')
EventLog.EventLogger.write("-----PDF To Image Conversion started-----"+"\n")
pdf_to_image()
EventLog.EventLogger.write("-----PDF To Image Conversion Ended. Image Processing started-----"+"\n")
image_processing()
EventLog.EventLogger.write("-----Image Processing Ended. Auditing Starts-----"+"\n")
audit_forms()
EventLog.EventLogger.write("=========Auditing Ended. If there is any discrepancy in forms count please check Exception Folder.========="+"\n")
print("PROCESS HAS ENDED. PLEASE VALIDATE FILE COUNTS IN LOGS.")

    

    
