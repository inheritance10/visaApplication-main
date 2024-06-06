import time

def personelInfoPage(p, data):
    if isinstance(data, list) and len(data) > 0:
        for i in range(len(data)):
            p.ele(f"#name{i + 1}").input(data[i]["name"])
            p.ele(f"#surname{i + 1}").input(data[i]["surname"])
            p.ele(f"#birthday{i + 1}").select(data[i]["birthday"])
            p.ele(f"#birthmonth{i + 1}").select(data[i]["birthmonth"])
            p.ele(f"#birthyear{i + 1}").select(data[i]["birthyear"])
            p.ele(f"#passport{i + 1}").input(data[i]["passport"])
            p.ele(f"#phone{i + 1}").input(data[i]["phone"])
            p.ele(f"#email{i + 1}").input(data[i]["email"])
    elif isinstance(data, dict):
        p.ele("#name1").input(data["name"])
        p.ele("#surname1").input(data["surname"])
        p.ele("#birthday1").select(data["birthday"])
        p.ele("#birthmonth1").select(data["birthmonth"])
        p.ele("#birthyear1").select(data["birthyear"])
        p.ele("#passport1").input(data["passport"])
        p.ele("#phone1").input(data["phone"])
        p.ele("#email1").input(data["email"])
    else:
        print("Data değeri ne liste ne de sözlük.")

    p.ele("#btnAppPersonalNext").click()
    time.sleep(1)
    p.ele("#btnAppPreviewNext").click()
    time.sleep(1)
