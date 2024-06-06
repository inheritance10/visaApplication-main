import time
from utilts.emailSmsVerify import getCodefromMail,getCodefromSms

def additionalServices(p,mock_data,shared_variable):
    p.ele(".additionalservices").click()
    p.ele("#btnAppServicesNext").click()
    time.sleep(5)
    p.ele("#mailConfirmCodeControl").input(getCodefromMail())
    time.sleep(2)
    p.ele("#smsConfirmCodeControl").input(getCodefromSms(shared_variable))
