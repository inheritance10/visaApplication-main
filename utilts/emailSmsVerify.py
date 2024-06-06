import imaplib
import email
from email.header import decode_header


def getCodefromMail():
    username = "erbaltadeveloper@gmail.com"
    password = "ejjf wlgd hryk xlyi"
    # IMAP sunucusuna bağlanma
    mail = imaplib.IMAP4_SSL("imap.gmail.com")
    mail.login(username, password)

    # Gelen kutusuna erişme
    mail.select("inbox")

    # Belirtilen adresten gelen e-postaları arama
    status, messages = mail.search(None, 'FROM "noreply@idata.com.tr"')
    mail_ids = messages[0].split()

    if mail_ids:
        # Son e-postayı alma
        latest_email_id = mail_ids[-1]
        status, msg_data = mail.fetch(latest_email_id, "(RFC822)")
        for response_part in msg_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1])

                # E-postanın içeriğini çekme
                if msg.is_multipart():
                    for part in msg.walk():
                        content_type = part.get_content_type()
                        if content_type.startswith("image/"):
                            filename = part.get_filename()
                            if not filename:
                                ext = content_type.split("/")[-1]
                                filename = f"image.{ext}"
                            else:
                                filename = filename.rstrip(".png")
                            mail.logout()
                            return filename
                else:
                    content_type = msg.get_content_type()
                    if content_type.startswith("image/"):
                        filename = msg.get_filename()
                        if not filename:
                            ext = content_type.split("/")[-1]
                            filename = f"image.{ext}"
                        else:
                            filename = filename.rstrip(".png")
                        mail.logout()
                        return filename
    else:
        print("noreply@idata.com.tr adresinden gelen e-posta bulunamadı.")

    # Bağlantıyı kapatma
    mail.logout()
    return None


def getCodefromSms(shared_variable):

    while True:
        if shared_variable.value != 0:
            return shared_variable

"""    while True:
        if shared_variable.value == 1:  # Örneğin, 1 değerini dinliyorsanız
            # Burada yapmak istediğiniz işlemleri gerçekleştirin
            print("Değişken 1 oldu, işlem yapılıyor")
            # Değişkeni sıfırlayabilirsiniz veya başka bir işlem yapabilirsiniz
            shared_variable.value = 0"""