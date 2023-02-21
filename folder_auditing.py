from identifyingMRZ import forms
import os
import EventLog
from GetPath import get_forms


def audit_forms():
    # print(forms)
    forms=get_forms()
    for key in forms:
        count = 0
        for form in os.listdir(forms[key]):
            count+=1
        
        EventLog.EventLogger.write('Total '+key+': ' +str(count)+"\n")

# audit_forms()     