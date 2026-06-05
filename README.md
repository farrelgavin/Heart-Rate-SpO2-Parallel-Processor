# Evaluasi 3 Kompar — Parallel Heart Rate & SpO2 Processor

> Proyek ini merupakan bagian dari **Evaluasi 3** mata kuliah **IFB 206 Komputasi Paralel**.  
> Fokus utama: implementasi **komputasi paralel** menggunakan `multiprocessing` Python untuk memproses data kesehatan (Heart Rate & SpO2) dari beberapa pasien secara bersamaan.

---

## 👤 Informasi Mahasiswa

| | |
|---|---|
| **Nama** | Farrel Gavin |
| **NRP** | 152024016 |
| **Mata Kuliah** | IFB 206 Komputasi Paralel |
| **Evaluasi** | Evaluasi 3 |
| **Institusi** | Institut Teknologi Nasional (ITENAS) Bandung |

---

## 📁 Struktur Proyek

```
Evaluasi 3 Kompar/
├── main.py          # Program utama komputasi paralel
├── index.html       # Antarmuka web dokumentasi
├── style.css        # Stylesheet antarmuka web
├── app.js           # Logika interaktif halaman web
└── README.md        # Dokumentasi proyek ini
```

---

## 🐍 `main.py` — Komputasi Paralel Pemrosesan Data Kesehatan

### Deskripsi

Program ini mensimulasikan **pemrosesan data Heart Rate (detak jantung) dan SpO2 (saturasi oksigen)** dari beberapa pasien secara paralel menggunakan modul `multiprocessing` Python.

Setiap pasien memiliki 500 titik data sensor. Dengan komputasi paralel, semua pasien diproses **secara bersamaan** di core CPU yang berbeda — jauh lebih cepat dibanding sekuensial.

### Library yang Digunakan

| Library | Kegunaan |
|---|---|
| `multiprocessing` | Membuat dan mengelola proses paralel menggunakan banyak core CPU |
| `time` | Mengukur waktu eksekusi program |
| `random` | Membangkitkan data sensor simulasi secara acak |

### Alur Kerja Program

```
Data 4 Pasien (masing-masing 500 titik HR + SpO2)
        │
        ▼
┌──────────────────────────────────────┐
│         multiprocessing.Pool(4)      │
│  ┌─────────┐  ┌─────────┐           │
│  │ Core 1  │  │ Core 2  │  ...dst   │  ← berjalan BERSAMAAN
│  │Pasien P1│  │Pasien P2│           │
│  └─────────┘  └─────────┘           │
└──────────────────────────────────────┘
        │
        ▼
  Hasil: avg HR, avg SpO2, status tiap pasien
```

### Penjelasan Kode

```python
import multiprocessing
import time
import random
```
> Tiga modul standar Python, tidak perlu instalasi tambahan.

---

```python
def process_patient_data(patient_info):
    patient_id, hr_data, spo2_data = patient_info
    time.sleep(1)  # Simulasi komputasi berat
    avg_hr   = sum(hr_data)   / len(hr_data)
    avg_spo2 = sum(spo2_data) / len(spo2_data)
    ...
    return { "patient_id": ..., "avg_hr": ..., "avg_spo2": ... }
```
> Fungsi yang dijalankan oleh setiap worker process. Menerima data satu pasien, menghitung rata-rata HR dan SpO2, serta menentukan status kesehatannya.

---

```python
with multiprocessing.Pool(processes=4) as pool:
    results = pool.map(process_patient_data, patients)
```
> **Inti komputasi paralel:** `Pool(4)` membuat 4 worker process, `pool.map` mendistribusikan setiap pasien ke core CPU berbeda secara **bersamaan**.

---

### Logika Status Kesehatan

| Parameter | Rentang | Status |
|---|---|---|
| Heart Rate | < 60 bpm | Bradikardia |
| Heart Rate | 60–100 bpm | Normal |
| Heart Rate | > 100 bpm | Takikardia |
| SpO2 | ≥ 95 % | Normal |
| SpO2 | < 95 % | Hipoksemia |

### Contoh Output

```
=======================================================
  Heart Rate & SpO2 Parallel Processor
  Farrel Gavin — 152024016
=======================================================

Memulai komputasi paralel untuk 4 pasien...

[SpawnPoolWorker-1] Memproses data Pasien P01 (500 sampel)...
[SpawnPoolWorker-2] Memproses data Pasien P02 (500 sampel)...
[SpawnPoolWorker-3] Memproses data Pasien P03 (500 sampel)...
[SpawnPoolWorker-4] Memproses data Pasien P04 (500 sampel)...

=======================================================
  HASIL PEMROSESAN
=======================================================

Pasien P01:
  Heart Rate : 82.47 bpm  → Normal
  SpO2       : 96.31 %    → Normal

Pasien P02:
  Heart Rate : 97.15 bpm  → Normal
  SpO2       : 93.82 %    → Hipoksemia (rendah)

Pasien P03:
  Heart Rate : 58.90 bpm  → Bradikardia (terlalu lambat)
  SpO2       : 97.44 %    → Normal

Pasien P04:
  Heart Rate : 103.21 bpm → Takikardia (terlalu cepat)
  SpO2       : 95.10 %    → Normal

Waktu eksekusi (Paralel) : 1.0312 detik
Estimasi sekuensial      : ~4 detik
Speedup                  : ~3.9x lebih cepat
=======================================================
```

> ⚡ Tanpa paralel → ~4 detik. Dengan paralel → ~1 detik. Speedup hampir **4x lipat**.

---

## 🔑 Konsep Kunci

### Mengapa `multiprocessing` bukan `threading`?

| | `threading` | `multiprocessing` |
|---|---|---|
| Cocok untuk | I/O-bound (file, network) | CPU-bound (komputasi berat) |
| GIL | Terkena — tidak benar-benar paralel | Bebas — tiap proses punya GIL sendiri |
| Memori | Shared (rawan race condition) | Terpisah per proses (aman) |
| Overhead | Rendah | Lebih tinggi (spawn process) |

> Pemrosesan data sensor adalah **CPU-bound**, sehingga `multiprocessing` adalah pilihan yang tepat.

---

## ▶️ Cara Menjalankan

**Prasyarat:** Python 3.x (semua modul sudah bawaan)

```bash
python main.py
```

> ⚠️ **Penting:** Pastikan selalu ada `if __name__ == "__main__":` saat menggunakan `multiprocessing` di Windows.

---

> 📌 *Dokumentasi resmi Evaluasi 3 Kompar — Farrel Gavin (152024016)*
