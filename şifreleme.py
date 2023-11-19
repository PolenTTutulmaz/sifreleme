BelirlenmişKullanıcıAdı = "kullanıcı"
BelirlenmişŞifre = "şifre"

while True:
    kullanıcıAdı = input("Kullanıcı adınızı giriniz : ")
    şifre = input("Şifrenizi giriniz : ")
    if BelirlenmişKullanıcıAdı != kullanıcıAdı:
        print("Kullanıcı adınız hatalı!")
    else:

        while True:

            if BelirlenmişŞifre != şifre:
                print("Şifreniz hatalı")
                şifre = input("Şifrenizi giriniz : ")
            else:
                print("Giriş yapıldı. Sayın", kullanıcıAdı)
                break
        break  # döngüyü sonlandırır
