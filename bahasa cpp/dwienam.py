def konversi_suhu():
    print("Selamat datang di Konverter Suhu!")
    print("Pilih jenis konversi:")
    print("1. Celcius ke Fahrenheit")
    print("2. Fahrenheit ke Celcius")

    pilihan = input("Masukkan pilihan Anda (1/2): ")

    if pilihan == '1':
        suhu_celcius = float(input("Masukkan suhu dalam Celcius: "))
        suhu_fahrenheit = (suhu_celcius * 9/5) + 32
        print(f"{suhu_celcius}°C sama dengan {suhu_fahrenheit}°F")
    elif pilihan == '2':
        suhu_fahrenheit = float(input("Masukkan suhu dalam Fahrenheit: "))
        suhu_celcius = (suhu_fahrenheit - 32) * 5/9
        print(f"{suhu_fahrenheit}°F sama dengan {suhu_celcius}°C")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi untuk memulai konversi suhu
konversi_suhu()
