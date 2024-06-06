import time

def fillTextfield(p, data):
    if isinstance(data, list) and len(data) > 0:
        first_element = data[0]
        p.ele("#city").select(first_element["city"])
        p.ele("#office").select(first_element["office"])
        p.ele("#getapplicationtype").select(first_element["getapplicationtype"])
        p.ele("#officetype").select(first_element["officetype"])
        p.ele("#totalPerson").select(len(data) + 1)  # Dizi boyutuna göre kişi sayısı
        time.sleep(2)
        p.ele("#btnAppCountNext").click()
    elif isinstance(data, dict):
        p.ele("#city").select(data["city"])
        p.ele("#office").select(data["office"])
        p.ele("#getapplicationtype").select(data["getapplicationtype"])
        p.ele("#officetype").select(data["officetype"])
        p.ele("#totalPerson").select(2)
        time.sleep(2)
        p.ele("#btnAppCountNext").click()
    else:
        print("Data değeri ne liste ne de sözlük.")
