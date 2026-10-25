
import csv
import os
import time

NAMA_FILE = "google_books_dataset (1).csv"


def baca_data():
    if not os.path.exists(NAMA_FILE):
        print(f"File {NAMA_FILE} tidak ditemukan.")
        return []

    with open(NAMA_FILE, "r", encoding="utf-8-sig", newline="") as file:
        pembaca = csv.DictReader(file)
        data = list(pembaca)

    print("Dataset berhasil dibaca.")
    print("Jumlah data buku:", len(data))
    print("Kolom dataset:", list(data[0].keys()) if data else [])

    return data


def linear_search(data, kata_kunci):
    hasil = []
    jumlah_perbandingan = 0
    kata_kunci = kata_kunci.strip().lower()

    for buku in data:
        jumlah_perbandingan += 1
        judul = buku["title"].strip().lower()

        if judul == kata_kunci:
            hasil.append(buku)

    return hasil, jumlah_perbandingan


def binary_search(data, kata_kunci):
    hasil = []
    jumlah_perbandingan = 0
    kiri = 0
    kanan = len(data) - 1
    kata_kunci = kata_kunci.strip().lower()

    while kiri <= kanan:
        tengah = (kiri + kanan) // 2
        jumlah_perbandingan += 1
        judul = data[tengah]["title"].strip().lower()

        if judul == kata_kunci:
            hasil.append(data[tengah])

            i = tengah - 1
            while i >= 0 and data[i]["title"].strip().lower() == kata_kunci:
                hasil.append(data[i])
                jumlah_perbandingan += 1
                i -= 1

            i = tengah + 1
            while i < len(data) and data[i]["title"].strip().lower() == kata_kunci:
                hasil.append(data[i])
                jumlah_perbandingan += 1
                i += 1

            return hasil, jumlah_perbandingan

        elif judul < kata_kunci:
            kiri = tengah + 1
        else:
            kanan = tengah - 1

    return hasil, jumlah_perbandingan


if __name__ == "__main__":
    data_buku = baca_data()

    if data_buku:
        data_urut = sorted(
            data_buku,
            key=lambda buku: buku["title"].strip().lower()
        )

        kata_kunci = input(
            "\nMasukkan judul buku yang ingin dicari: "
        ).strip()

        mulai = time.perf_counter()
        hasil_linear, perbandingan_linear = linear_search(
            data_buku, kata_kunci
        )
        waktu_linear = time.perf_counter() - mulai

        mulai = time.perf_counter()
        hasil_binary, perbandingan_binary = binary_search(
            data_urut, kata_kunci
        )
        waktu_binary = time.perf_counter() - mulai

        print("\n=== HASIL LINEAR SEARCH ===")
        print("Jumlah buku ditemukan:", len(hasil_linear))
        print("Jumlah perbandingan:", perbandingan_linear)
        print(f"Waktu eksekusi: {waktu_linear:.8f} detik")

        print("\n=== HASIL BINARY SEARCH ===")
        print("Jumlah buku ditemukan:", len(hasil_binary))
        print("Jumlah perbandingan:", perbandingan_binary)
        print(f"Waktu eksekusi: {waktu_binary:.8f} detik")

        if hasil_linear:
            print("\nJudul buku yang ditemukan:")
            print(hasil_linear[0]["title"])
        else:
            print("\nBuku tidak ditemukan.")

        print("\n=== KESIMPULAN PERBANDINGAN ===")

        if waktu_linear < waktu_binary:
            print("Linear Search lebih cepat pada percobaan ini.")
        elif waktu_binary < waktu_linear:
            print("Binary Search lebih cepat pada percobaan ini.")
        else:
            print("Kedua algoritma memiliki waktu yang sama.")

        print("Total data buku:", len(data_buku))
        print("Linear Search:", perbandingan_linear, "perbandingan")
        print("Binary Search:", perbandingan_binary, "perbandingan")
