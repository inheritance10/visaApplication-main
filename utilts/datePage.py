import time


def datePage(p,data):
    p.ele(".form-control flightDate").click()
    p.eles(".day")[len(p.eles(".day")) - 1].click()
    p.ele(".form-control calendarinput").click()
    p.eles(".day enabled-day")[0].click()
    time.sleep(1)
    p.eles(".btn btn-warning getdatebtnhour form-control noPrime")[0].click()
    p.ele("#btnAppCalendarNext").click()