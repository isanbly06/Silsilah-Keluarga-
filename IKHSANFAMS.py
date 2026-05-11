class Orang:

    def __init__(self, nama, jenis_kelamin):

        self.nama = nama
        self.jenis_kelamin = jenis_kelamin  # L / P

        self.ayah = None
        self.ibu = None
        self.pasangan = None

        self.anak = []

    # -----------------------------------------------------

    def tambah_anak(self, anak):

        if anak not in self.anak:
            self.anak.append(anak)

# CLASS SILSILAH KELUARGA

class SilsilahKeluarga:

    def __init__(self):

        # Dictionary penyimpanan data orang
        self.data_orang = {}

    # MENAMBAHKAN ORANG
    def tambah_orang(self, nama, jenis_kelamin):

        if nama not in self.data_orang:

            self.data_orang[nama] = Orang(
                nama,
                jenis_kelamin
            )

    # MENGATUR ORANG TUA
    def atur_orang_tua(
        self,
        nama_anak,
        nama_ayah=None,
        nama_ibu=None
    ):

        anak = self.data_orang.get(nama_anak)

        if not anak:
            return

        # AYAH
        if nama_ayah and nama_ayah != "-":

            ayah = self.data_orang.get(nama_ayah)

            if ayah:

                anak.ayah = ayah
                ayah.tambah_anak(anak)

        # ---------------------------------------------
        # IBU
        # ---------------------------------------------

        if nama_ibu and nama_ibu != "-":

            ibu = self.data_orang.get(nama_ibu)

            if ibu:

                anak.ibu = ibu
                ibu.tambah_anak(anak)

    # MENGATUR PASANGAN
    def atur_pasangan(self, nama1, nama2):

        if nama1 == "-" or nama2 == "-":
            return

        orang1 = self.data_orang.get(nama1)
        orang2 = self.data_orang.get(nama2)

        if orang1 and orang2:

            orang1.pasangan = orang2
            orang2.pasangan = orang1

    # MENAMPILKAN SELURUH DATA
    def tampilkan_semua_data(self):

        print("\n===== DATA SELURUH KELUARGA =====")

        for orang in self.data_orang.values():

            ayah = orang.ayah.nama if orang.ayah else "-"
            ibu = orang.ibu.nama if orang.ibu else "-"
            pasangan = orang.pasangan.nama if orang.pasangan else "-"

            print(f"""
Nama            : {orang.nama}
Jenis Kelamin   : {orang.jenis_kelamin}
Ayah            : {ayah}
Ibu             : {ibu}
Pasangan        : {pasangan}
""")

    # MENAMPILKAN SILSILAH
    def tampilkan_silsilah(self, nama, level=0):

        orang = self.data_orang.get(nama)

        if not orang:
            return

        print("   " * level + f"├── {orang.nama}")

        for anak in orang.anak:
            self.tampilkan_silsilah(anak.nama, level + 1)

    # MENCARI AYAH

    def cari_ayah(self, nama):

        orang = self.data_orang.get(nama)

        if orang and orang.ayah:
            return orang.ayah.nama

        return "Tidak ditemukan"

    # MENCARI IBU
    def cari_ibu(self, nama):

        orang = self.data_orang.get(nama)

        if orang and orang.ibu:
            return orang.ibu.nama

        return "Tidak ditemukan"

    # MENCARI KAKEK

    def cari_kakek(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return "Tidak ditemukan"

        # PIHAK AYAH
        if pihak == "ayah":

            if orang.ayah and orang.ayah.ayah:
                return orang.ayah.ayah.nama

        # PIHAK IBU
        elif pihak == "ibu":

            if orang.ibu and orang.ibu.ayah:
                return orang.ibu.ayah.nama

        else:

            if orang.ayah and orang.ayah.ayah:
                return orang.ayah.ayah.nama

        return "Tidak ditemukan"

    # MENCARI NENEK
    def cari_nenek(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return "Tidak ditemukan"

        # PIHAK AYAH

        if pihak == "ayah":

            if orang.ayah and orang.ayah.ibu:
                return orang.ayah.ibu.nama

        # PIHAK IBU
        elif pihak == "ibu":

            if orang.ibu and orang.ibu.ibu:
                return orang.ibu.ibu.nama

        else:

            if orang.ayah and orang.ayah.ibu:
                return orang.ayah.ibu.nama

        return "Tidak ditemukan"

    # MENCARI KAKEK BUYUT

    def cari_kakek_buyut(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return "Tidak ditemukan"

        # PIHAK AYAH
        # ayah -> ayah -> ayah
        if pihak == "ayah":

            if (
                orang.ayah and
                orang.ayah.ayah and
                orang.ayah.ayah.ayah
            ):

                return orang.ayah.ayah.ayah.nama
            
        # PIHAK IBU
        # ibu -> ibu -> ayah
        elif pihak == "ibu":

            if (
                orang.ibu and
                orang.ibu.ibu and
                orang.ibu.ibu.ayah
            ):

                return orang.ibu.ibu.ayah.nama

        return "Tidak ditemukan"

    # MENCARI NENEK BUYUT
    def cari_nenek_buyut(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return "Tidak ditemukan"

        # PIHAK AYAH
        # ayah -> ayah -> ibu
        if pihak == "ayah":

            if (
                orang.ayah and
                orang.ayah.ayah and
                orang.ayah.ayah.ibu
            ):

                return orang.ayah.ayah.ibu.nama

        # PIHAK IBU
        # ibu -> ibu -> ibu
        elif pihak == "ibu":

            if (
                orang.ibu and
                orang.ibu.ibu and
                orang.ibu.ibu.ibu
            ):

                return orang.ibu.ibu.ibu.nama

        return "Tidak ditemukan"

    # MENCARI SAUDARA KANDUNG
    def cari_saudara_kandung(self, nama):

        orang = self.data_orang.get(nama)

        if not orang:
            return []

        hasil = []

        for data in self.data_orang.values():

            if data.nama == orang.nama:
                continue

            if (
                data.ayah == orang.ayah and
                data.ibu == orang.ibu
            ):

                hasil.append(data)

        return hasil

    # MENCARI PAMAN
    def cari_paman(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return []

        target_orang_tua = None

        # PIHAK AYAH
        if pihak == "ayah":
            target_orang_tua = orang.ayah

        # PIHAK IBU
        elif pihak == "ibu":
            target_orang_tua = orang.ibu

        else:
            target_orang_tua = orang.ayah

        if not target_orang_tua:
            return []

        hasil = []

        saudara = self.cari_saudara_kandung(
            target_orang_tua.nama
        )

        for s in saudara:

            if s.jenis_kelamin == "L":
                hasil.append(s.nama)

        return hasil

    # MENCARI BIBI
    def cari_bibi(self, nama, pihak=None):

        orang = self.data_orang.get(nama)

        if not orang:
            return []

        target_orang_tua = None

        # PIHAK AYAH
        if pihak == "ayah":
            target_orang_tua = orang.ayah

        # PIHAK IBU
        elif pihak == "ibu":
            target_orang_tua = orang.ibu

        else:
            target_orang_tua = orang.ayah

        if not target_orang_tua:
            return []

        hasil = []

        saudara = self.cari_saudara_kandung(
            target_orang_tua.nama
        )

        for s in saudara:

            if s.jenis_kelamin == "P":
                hasil.append(s.nama)

        return hasil

    # MENCARI SEPUPU
    def cari_sepupu(self, nama, pihak=None):

        hasil_sepupu = []

        daftar_paman = self.cari_paman(nama, pihak)
        daftar_bibi = self.cari_bibi(nama, pihak)

        keluarga = daftar_paman + daftar_bibi

        for nama_keluarga in keluarga:

            orang = self.data_orang.get(nama_keluarga)

            if orang:

                for anak in orang.anak:
                    hasil_sepupu.append(anak.nama)

        return hasil_sepupu

    # MENAMBAHKAN ANGGOTA BARU
    def tambah_anggota_baru(self):

        print("\n===== TAMBAH ANGGOTA BARU =====")

        nama = input("Nama: ")
        jenis_kelamin = input("Jenis Kelamin (L/P): ")

        ayah = input("Nama Ayah (- jika tidak ada): ")
        ibu = input("Nama Ibu (- jika tidak ada): ")

        pasangan = input("Nama Pasangan (- jika tidak ada): ")

        # TAMBAH ORANG
        self.tambah_orang(nama, jenis_kelamin)

        # ATUR ORANG TUA
        self.atur_orang_tua(
            nama,
            ayah,
            ibu
        )

        # ATUR PASANGAN
        if pasangan != "-":

            if pasangan not in self.data_orang:

                print(
                    "Pasangan belum ada di data."
                )

            else:

                self.atur_pasangan(
                    nama,
                    pasangan
                )

        print("Data berhasil ditambahkan.")

    # MEMPROSES INPUT NATURAL
    def proses_perintah(self, teks):

        teks = teks.lower()

        # Kakek
        if "kakek" in teks:

            nama = input("Masukkan nama: ")

            pihak = None

            if "ayah" in teks:
                pihak = "ayah"

            elif "ibu" in teks:
                pihak = "ibu"

            hasil = self.cari_kakek(
                nama,
                pihak
            )

            print("Kakek:", hasil)

        # Nenek
        elif "nenek" in teks:

            nama = input("Masukkan nama: ")

            pihak = None

            if "ayah" in teks:
                pihak = "ayah"

            elif "ibu" in teks:
                pihak = "ibu"

            hasil = self.cari_nenek(
                nama,
                pihak
            )

            print("Nenek:", hasil)

        # Paman
        elif "paman" in teks:

            nama = input("Masukkan nama: ")

            pihak = None

            if "ayah" in teks:
                pihak = "ayah"

            elif "ibu" in teks:
                pihak = "ibu"

            hasil = self.cari_paman(
                nama,
                pihak
            )

            print("Paman:", hasil)

        # Bibi
        elif "bibi" in teks:

            nama = input("Masukkan nama: ")

            pihak = None

            if "ayah" in teks:
                pihak = "ayah"

            elif "ibu" in teks:
                pihak = "ibu"

            hasil = self.cari_bibi(
                nama,
                pihak
            )

            print("Bibi:", hasil)

        # Sepupu
        elif "sepupu" in teks:

            nama = input("Masukkan nama: ")

            pihak = None

            if "ayah" in teks:
                pihak = "ayah"

            elif "ibu" in teks:
                pihak = "ibu"

            hasil = self.cari_sepupu(
                nama,
                pihak
            )

            print("Sepupu:", hasil)

        else:

            print("Perintah tidak dikenali.")

# MEMBUAT OBJECT PROGRAM
keluarga = SilsilahKeluarga()

data_keluarga = [
# Pihak Ayah
# Kakek dan Nenek buyut dari dari Kakek
    ("Tgk. Husein", "L", "-", "-", "Fatimah"),
    ("Fatimah", "P", "-", "-", "Tgk Husein"),
    
# Kakek dan Nenek buyut dari dari nenek
    ("sayed Mahmud", "L", "-", "-", "Hawa"),
    ("Hawa", "P", "-", "-", "Sayed Mahmud"),

# Kakek dan Nenek 
    ("Abdul Hamid", "L", "Tgk. Husein", "Fatimah", "Aminah"),
    ("Aminah", "P", "Sayed Mahmud", "Hawa", "Abdul Hamid"),

# Paman dan Bibi
    ("Ridwan", "L", "-", "-", "Fauziah"),
    ("Fauziah", "P", "Abdul Hamid", "Aminah", "Ridwan"),

    ("Darmiah", "P", "Abdul Hamid", "Aminah", "-"),

    ("Saifullah", "L", "-", "-", "Syamsiah"),
    ("Syamsiah", "P", "Abdul Hamid", "Aminah", "Saifullah"),

    ("Safruddin", "L", "Abdul Hamid", "Aminah", "Wak Wi"),
    ("Wak Wi", "P", "-", "-", "Safruddin"),

    ("Salahuddin", "L", "Abdul Hamid", "Aminah", "Wak Laili"),
    ("Wak Laili", "P", "-", "-", "Salahuddin"),

    ("Zulfadli", "L", "Abdul Hamid", "Aminah", "Badriah Kamaruddin"),
    ("Badriah Kamaruddin", "P", "Teuku Kamaruddin", "Fatimah Syam", "Zulfadli"),

    ("Afifuddin", "L", "Abdul Hamid", "Aminah", "Eva Yanti"),
    ("Eva Yanti", "P", "-", "-", "Afifuddin"),

    ("Om Aris", "L", "-", "-", "Azimah"),
    ("Azimah", "P", "Abdul Hamid", "Aminah", "Om Aris"),

    ("Amiruddin", "L", "Abdul Hamid", "Aminah", "Cek Niar"),
    ("Cek Niar", "P", "-", "-", "Amiruddin"),

    # Pihak Ibu
# Kakek dan Nenek buyut dari kakek
    ("Teuku Ahmad", "L", "-", "-", "Cut Aminah"),
    ("Cut Aminah", "P", "-", "-", "Teuku Ahmad"),
    
# Kakek dan Nenek buyut dari nenek
    ("Tgk. Sarong", "L", "-", "-", "Cut Syahkubandi"),
    ("Cut Syahkubandi", "P", "-", "-", "Tgk. Sarong"),

# Kakek dan Nenek 
    ("Teuku Kamaruddin", "L", "Teuku Ahmad", "Cut Aminah", "Fatimah Syam"),
    ("Fatimah Syam", "P", "Tgk. Sarong", "Cut Syahkubandi", "Teuku Kamaruddin"),

    # Paman dan Bibi
    ("Sudarso", "L", "-", "-", "Safrana"),
    ("Safrana", "P", "Teuku Kamaruddin", "Fatimah Syam", "Sudarso"),

    ("Zulfadli", "L", "Abdul Hamid", "Aminah", "Badriah Kamaruddin"),
    ("Badriah Kamaruddin", "P", "Teuku Kamaruddin", "Fatimah Syam", "Zulfadli"),

    ("Hasanul Basri", "L", "-", "-", "Safrinda"),
    ("Safrinda", "P", "Teuku Kamaruddin", "Fatimah Syam", "Hasanul Basri"),

    ("Salamuddin", "L", "-", "-", "Karimah"),
    ("Karimah", "P", "Teuku Kamaruddin", "Fatimah Syam", "Salamuddin"),

    ("Teuku Kamaruzzaman", "L", "Teuku Kamaruddin", "Fatimah Syam", "Lili Yanti"),
    ("Lili Yanti", "P", "-", "-", "Teuku Kamaruzzaman"),

    ("Armiadi", "L", "-", "-", "Cut Intan Fitriani"),
    ("Cut Intan Fitriani", "P", "Teuku Kamaruddin", "Fatimah Syam", "Armiadi")

    # Sepupu dari ayah

    # Sepupu dari ibu

]

# MEMASUKKAN DATA KE PROGRAM
# Tambahkan semua orang
for data in data_keluarga:

    nama, jk, ayah, ibu, pasangan = data

    keluarga.tambah_orang(
        nama,
        jk
    )

# Hubungkan relasi
for data in data_keluarga:

    nama, jk, ayah, ibu, pasangan = data

    keluarga.atur_orang_tua(
        nama,
        ayah,
        ibu
    )

    keluarga.atur_pasangan(
        nama,
        pasangan
    )

# MENU UTAMA
while True:

    print("""
=================================================
        PROGRAM SILSILAH KELUARGA
=================================================

1. Tampilkan seluruh data keluarga
2. Tampilkan silsilah keluarga
3. Cari ayah
4. Cari ibu
5. Cari kakek
6. Cari nenek
7. Cari kakek buyut
8. Cari nenek buyut
9. Cari paman
10. Cari bibi
11. Cari sepupu
12. Tambah anggota keluarga
13. Input perintah natural
14. Keluar

=================================================
""")

    pilihan = input("Pilih menu: ")

    # MENU 1
    if pilihan == "1":

        keluarga.tampilkan_semua_data()

    # MENU 2
    elif pilihan == "2":

        nama = input("Masukkan nama root keluarga: ")

        keluarga.tampilkan_silsilah(nama)

    # MENU 3
    elif pilihan == "3":

        nama = input("Masukkan nama: ")

        hasil = keluarga.cari_ayah(nama)

        print("Ayah:", hasil)

    # MENU 4
    elif pilihan == "4":

        nama = input("Masukkan nama: ")

        hasil = keluarga.cari_ibu(nama)

        print("Ibu:", hasil)

    # MENU 5
    elif pilihan == "5":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_kakek(
            nama,
            pihak
        )

        print("Kakek:", hasil)

    # MENU 6
    elif pilihan == "6":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_nenek(
            nama,
            pihak
        )

        print("Nenek:", hasil)

    # MENU 7
    elif pilihan == "7":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_kakek_buyut(
            nama,
            pihak
        )

        print("Kakek Buyut:", hasil)

    # MENU 8
    elif pilihan == "8":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_nenek_buyut(
            nama,
            pihak
        )

        print("Nenek Buyut:", hasil)

    # MENU 9
    elif pilihan == "9":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_paman(
            nama,
            pihak
        )

        print("Paman:", hasil)

    # MENU 10
    elif pilihan == "10":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_bibi(
            nama,
            pihak
        )

        print("Bibi:", hasil)

    # MENU 11
    elif pilihan == "11":

        nama = input("Masukkan nama: ")

        pihak = input("Pihak (ayah/ibu): ")

        hasil = keluarga.cari_sepupu(
            nama,
            pihak
        )

        print("Sepupu:", hasil)

    # MENU 12
    elif pilihan == "12":

        keluarga.tambah_anggota_baru()

    # MENU 13
    elif pilihan == "13":

        teks = input("Masukkan perintah: ")

        keluarga.proses_perintah(teks)

    # MENU Exit
    elif pilihan == "14":

        print("Program selesai.")
        break

    # PILIHAN TIDAK VALID
    else:

        print("Pilihan tidak valid.")