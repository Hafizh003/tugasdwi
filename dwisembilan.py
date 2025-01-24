import random

def main():
    print("Selamat datang di permainan Batu, Kertas, Gunting!")
    pilihan = ["Batu", "Kertas", "Gunting"]

    while True:
        # Meminta input pengguna
        user_input = input("Masukkan pilihan Anda (Batu/Kertas/Gunting) atau 'keluar' untuk mengakhiri: ").capitalize()

        if user_input == 'Keluar':
            print("Terima kasih telah bermain!")
            break

        if user_input not in pilihan:
            print("Pilihan tidak valid. Silakan coba lagi.")
            continue

        # Komputer memilih secara acak
        komputer_input = random.choice(pilihan)
        print(f"Komputer memilih: {komputer_input}")

        # Menentukan pemenang
        if user_input == komputer_input:
            print("Hasil: Seri!")
        elif (user_input == "Batu" and komputer_input == "Gunting") or \
             (user_input == "Kertas" and komputer_input == "Batu") or \
             (user_input == "Gunting" and komputer_input == "Kertas"):
            print("Anda menang!")
        else:
            print("Komputer menang!")

# Memanggil fungsi utama untuk memulai permainan
main()
