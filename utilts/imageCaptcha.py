from vision_service import detect_text_from_image
import base64
import os
import time

def solve_captcha_and_submit(p):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = './steam-kingdom-385919-d8d875f83e98.json'
    initial_url = p.url

    while True:
        # CAPTCHA görüntüsünü al
        data = p.ele(".imageCaptcha").src()
        image_content = base64.b64encode(data).decode('utf-8')
        detected_text = detect_text_from_image(image_content)
        p.ele("#mailConfirmCodeControl").input(detected_text)
        p.ele("#confirmationbtn").click()

        time.sleep(1)

        current_url = p.url

        if current_url != initial_url:
            break

        p.refresh()
        time.sleep(1)
