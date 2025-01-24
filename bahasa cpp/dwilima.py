def konversi_mata_uang(jumlah, kurs):
    return jumlah * kurs

def main():
    # Nilai tukar statis (contoh)
    nilai_tukar = {
        'Dolar_Rupiah': 15000,  # 1 Dolar ke Rupiah
        'Euro_Rupiah': 16000,   # 1 Euro ke Rupiah
        'Rupiah_Dolar': 0.000067,  # 1 Rupiah ke Dolar
        'Rupiah_Euro': 0.0000625,  # 1 Rupiah ke Euro
    }

    print("Selamat datang di Konverter Mata Uang Sederhana!")
    print("Pilih konversi:")
    print("1. Dolar ke Rupiah")
    print("2. Euro ke Rupiah")
    print("3. Rupiah ke Dolar")
    print("4. Rupiah ke Euro")

    pilihan = input("Masukkan pilihan Anda (1/2/3/4): ")

    if pilihan in ['1', '2', '3', '4']:
        jumlah = float(input("Masukkan jumlah uang yang ingin dikonversi: "))

        if pilihan == '1':
            hasil = konversi_mata_uang(jumlah, nilai_tukar['Dolar_Rupiah'])
            print(f"{jumlah} Dolar sama dengan {hasil} Rupiah")
        elif pilihan == '2':
            hasil = konversi_mata_uang(jumlah, nilai_tukar['Euro_Rupiah'])
            print(f"{jumlah} Euro sama dengan {hasil} Rupiah")
        elif pilihan == '3':
            hasil = konversi_mata_uang(jumlah, nilai_tukar['Rupiah_Dolar'])
            print(f"{jumlah} Rupiah sama dengan {hasil} Dolar")
        elif pilihan == '4':
            hasil = konversi_mata_uang(jumlah, nilai_tukar['Rupiah_Euro'])
            print(f"{jumlah} Rupiah sama dengan {hasil} Euro")
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi utama untuk memulai aplikasi
main()
