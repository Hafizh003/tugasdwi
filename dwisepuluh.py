def tambah_kontak(kontak_dict):
    nama = input("Masukkan nama kontak: ")
    nomor = input("Masukkan nomor telepon: ")
    kontak_dict[nama] = nomor
    print(f"Kontak '{nama}' telah ditambahkan.")

def ambil_kontak(kontak_dict):
    nama = input("Masukkan nama kontak yang ingin diambil: ")
    if nama in kontak_dict:
        print(f"Nomor telepon {nama}: {kontak_dict[nama]}")
    else:
        print(f"Kontak '{nama}' tidak ditemukan.")

def tampilkan_kontak(kontak_dict):
    if not kontak_dict:
        print("Tidak ada kontak yang disimpan.")
    else:
        print("Daftar Kontak:")
        for nama, nomor in kontak_dict.items():
            print(f"{nama}: {nomor}")

def main():
    kontak_dict = {}  # Kamus untuk menyimpan kontak
    while True:
        print("\nMenu:")
        print("1. Tambah Kontak")
        print("2. Ambil Kontak")
        print("3. Tampilkan Semua Kontak")
        print("4. Keluar")

        pilihan = input("Pilih opsi (1/2/3/4): ")

        if pilihan == '1':
            tambah_kontak(kontak_dict)
        elif pilihan == '2':
            ambil_kontak(kontak_dict)
        elif pilihan == '3':
            tampilkan_kontak(kontak_dict)
        elif pilihan == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Memanggil fungsi utama untuk memulai aplikasi
main()
