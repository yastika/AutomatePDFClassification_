from GetPath import log_file_path
import datetime
import os
from datetime import datetime

class EventLogger:
    @staticmethod
    def write(message):
        is_log_file = os.path.isfile(log_file_path())
        
        if is_log_file:
            create_timestamp = os.stat(log_file_path()).st_ctime
            create_datetime = datetime.fromtimestamp(create_timestamp)
            create_date = create_datetime.strftime('%Y-%m-%d')
            today_date = datetime.today().strftime('%Y-%m-%d')
            if create_date < today_date:
                 old_file = log_file_path()
                 file_path,empty_val = old_file.split('.txt')
                 date_time = create_date.replace('-','')
                 new_file = file_path+'_'+str(date_time)+'.txt'
                 if os.path.isfile(new_file)== False:
                    os.rename(old_file,new_file)
            # print(message)
            file = open(log_file_path(),"a")
            file.write(message)
            file.close()
        else:
            file = open(log_file_path(),"a")
            file.write(message)
            file.close()        

                 


