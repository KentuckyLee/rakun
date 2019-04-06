from django.core.mail import send_mail


class Sys_Mails():
    from_email = 'recipient_list'

    def owner_first_record(self, mail, phone_number, password):
        try:
            print('...............system_mails/Sys_Mails/owner_first_record function called.')
            if mail or phone_number or password is not None:
                subject = 'Rakun Okul Yazılımları | Yeni şifreniz.'
                message = """Merhaba,
                
                Rakun ailesine hoşgeldiniz. Sistem giriş bilgileriniz aşağıdadır.
                Yukarıdaki bilgiler ile sisteme giriş yaptığınızda, şifre değiştirme alanına yönlendirileceksiniz. 
                Buradan yeni şifrenizi oluşturabilirsiniz.
    
    
                Hesap Bilgileri
                --------------------------------
                Kullanıcı adı: {}
                Giriş kodu: {}
                """.format(phone_number, password)
                mail = send_mail(
                    subject,
                    message,
                    from_email=self.from_email,
                    recipient_list=[mail],
                    fail_silently=False)
                if mail:
                    return True
                else:
                    return False
            else:
                raise Exception('function parameters empty')
        except Exception as e:
            print(e)

    def parent_first_record(self, mail, phone_number, password):
        try:
            print('...............system_mails/Sys_Mails/owner_first_record function called.')
            if mail or phone_number or password is not None:
                subject = 'Rakun Okul Yazılımları | Yeni şifreniz.'
                message = """Merhaba,

                Değerli velimiz Rakun ailesine hoşgeldiniz. Sistem giriş bilgileriniz aşağıdadır.
                Yukarıdaki bilgiler ile sisteme giriş yaptığınızda, şifre değiştirme alanına yönlendirileceksiniz. 
                Buradan yeni şifrenizi oluşturabilirsiniz.


                Hesap Bilgileri
                --------------------------------
                Kullanıcı adı: {}
                Giriş kodu: {}
                """.format(phone_number, password)
                mail = send_mail(
                    subject,
                    message,
                    from_email=self.from_email,
                    recipient_list=[mail],
                    fail_silently=False)
                if mail:
                    return True
                else:
                    return False
            else:
                raise Exception('function parameters empty')
        except Exception as e:
            print(e)

