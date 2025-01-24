def miwiti_permainan():
    print("Sugeng rawuh ing Petualangan Alas Ajaib!")
    print("Sampeyan minangka sawijining penjelajah sing wani, lan sampeyan anyar wae mlebu alas sing kebak misteri.")
    print("Apa sing pengin sampeyan lakoni?")

    pilihan_awal = input("Pilih: (1) Njelajah luwih jero utawa  (2) Bali menyang desa: ")

    if pilihan_awal == '1':
        print("\nSampeyan mutusake kanggo njelajah luwih jero menyang alas.")
        print("Ing ngarep, sampeyan ndeleng guwa sing peteng lan dalan setapak sing menuju kali.")
        pilihan_guwa = input("Pilih: (1) Mlebu guwa utawa (2) Ngelakoni dalan setapak: ")

        if pilihan_guwa == '1':
            print("\nSampeyan mlebu guwa lan nemokake harta karun sing didhelikake!")
            print("Selamet, sampeyan wis nemokake harta karun lan ngrampungake petualangan!")
        elif pilihan_guwa == '2':
            print("\nSampeyan ngikuti dalan setapak lan tekan kali sing ayu.")
            print("Sampeyan mutusake kanggo istirahat lan nikmati pemandangan.")
            print("Petualangan sampeyan pungkasan kanthi tentrem.")
        else:
            print("\nPilihan ora valid. Permainan rampung.")
    elif pilihan_awal == '2':
        print("\nSampeyan mutusake kanggo bali menyang desa.")
        print("Mungkin liyane sampeyan bakal luwih wani kanggo njelajah alas.")
    else:
        print("\nPilihan ora valid. Permainan rampung.")

# Ngluncurake fungsi kanggo miwiti permainan
miwiti_permainan()
