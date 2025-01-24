def mulai_kuis():
    # Daftar pertanyaan dan pilihan jawaban
    pertanyaan = [
        "Apa ibukota Indonesia?",
        "Siapa penemu lampu pijar?",
        "Apa nama planet terdekat dengan matahari?"
    ]

    pilihan_jawaban = [
        ["A. Jakarta", "B. Bandung", "C. Surabaya", "D. Medan"],
        ["A. Thomas Edison", "B. Alexander Graham Bell", "C. Nikola Tesla", "D. Albert Einstein"],
        ["A. Venus", "B. Mars", "C. Merkurius", "D. Jupiter"]
    ]

    jawaban_benar = ['A', 'A', 'C']  # Jawaban yang benar untuk setiap pertanyaan

    skor = 0  # Inisialisasi skor

    # Mengulangi setiap pertanyaan
    for i in range(len(pertanyaan)):
        print(f"\nPertanyaan {i + 1}: {pertanyaan[i]}")
        for pilihan in pilihan_jawaban[i]:
            print(pilihan)

        jawaban = input("Masukkan jawaban Anda (A/B/C/D): ").upper()

        # Memeriksa jawaban
        if jawaban == jawaban_benar[i]:
            print("Jawaban Anda benar!")
            skor += 1
        else:
            print(f"Jawaban Anda salah. Jawaban yang benar adalah {jawaban_benar[i]}.")

    # Menampilkan skor akhir
    print(f"\nKuis selesai! Skor Anda: {skor}/{len(pertanyaan)}")
    

# Memanggil fungsi untuk memulai kuis
mulai_kuis()
