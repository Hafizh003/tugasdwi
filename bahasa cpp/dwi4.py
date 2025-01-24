import time

def setel_alarm():
    try:
        # Meminta pengguna untuk memasukkan waktu dalam detik
        detik = int(input("Masukkan jumlah detik hingga alarm berbunyi: "))
        
        print(f"Alarm disetel selama {detik} detik. Tunggu...")
        
        # Menunggu selama jumlah detik yang ditentukan
        time.sleep(detik)
        
        # Memberi tahu pengguna bahwa waktu telah habis
        print("Waktu habis! Alarm berbunyi!")
    except ValueError:
        print("Masukkan angka yang valid.")

# Memanggil fungsi untuk memulai alarm
setel_alarm()
