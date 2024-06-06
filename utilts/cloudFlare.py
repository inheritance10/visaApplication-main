import time


def cloudflare(p):
    try:
        # Cloudflare iframe'ini kontrol et
        i = p.get_frame('@src^https://challenges.cloudflare.com/cdn-cgi')

        # Eğer iframe bulunduysa, içindeki 'mark' elemanına tıkla
        i('.mark').click()
        time.sleep(3)
    except Exception as e:
        print("Cloudflare geçişi gerekli değil veya iframe bulunamadı:", e)

