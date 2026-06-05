import multiprocessing
import time
import random

# ============================================================
# Evaluasi 3 - Komputasi Paralel
# Mata Kuliah : IFB 206 Komputasi Paralel
# Nama        : Farrel Gavin
# NRP         : 152024016
# Deskripsi   : Simulasi pemrosesan data Heart Rate & SpO2
#               dari beberapa pasien secara paralel
#               menggunakan multiprocessing Python.
# ============================================================

def process_patient_data(patient_info):
    """
    Fungsi yang dijalankan oleh setiap worker process secara paralel.
    Menerima data satu pasien dan menghitung:
      - Rata-rata Heart Rate
      - Rata-rata SpO2
      - Status kesehatan pasien
    """
    patient_id, hr_data, spo2_data = patient_info
    process_name = multiprocessing.current_process().name

    print(f"[{process_name}] Memproses data Pasien {patient_id} ({len(hr_data)} sampel)...")

    # Simulasi komputasi berat (analisis sinyal, filtering, dll.)
    time.sleep(1)

    avg_hr   = sum(hr_data)   / len(hr_data)
    avg_spo2 = sum(spo2_data) / len(spo2_data)

    # Tentukan status berdasarkan nilai rata-rata
    if avg_hr < 60:
        hr_status = "Bradikardia (terlalu lambat)"
    elif avg_hr > 100:
        hr_status = "Takikardia (terlalu cepat)"
    else:
        hr_status = "Normal"

    if avg_spo2 < 95:
        spo2_status = "Hipoksemia (rendah)"
    else:
        spo2_status = "Normal"

    return {
        "patient_id" : patient_id,
        "avg_hr"     : round(avg_hr, 2),
        "hr_status"  : hr_status,
        "avg_spo2"   : round(avg_spo2, 2),
        "spo2_status": spo2_status,
    }


def generate_patient_data(patient_id):
    """Membangkitkan data sensor simulasi untuk satu pasien."""
    # Heart Rate: nilai normal 60-100 bpm, sesekali anomali
    hr_data   = [random.uniform(55.0, 110.0) for _ in range(500)]
    # SpO2: nilai normal 95-100 %, sesekali anomali
    spo2_data = [random.uniform(92.0, 100.0) for _ in range(500)]
    return (patient_id, hr_data, spo2_data)


if __name__ == "__main__":
    NUM_PATIENTS = 4   # Jumlah pasien yang diproses secara paralel

    print("=" * 55)
    print("  Heart Rate & SpO2 Parallel Processor")
    print("  Farrel Gavin — 152024016")
    print("=" * 55)

    # 1. Bangkitkan data untuk setiap pasien
    patients = [generate_patient_data(f"P{i+1:02d}") for i in range(NUM_PATIENTS)]

    print(f"\nMemulai komputasi paralel untuk {NUM_PATIENTS} pasien...\n")
    start_time = time.time()

    # 2. Proses semua pasien secara PARALEL dengan Pool
    with multiprocessing.Pool(processes=NUM_PATIENTS) as pool:
        results = pool.map(process_patient_data, patients)

    end_time = time.time()

    # 3. Tampilkan hasil
    print("\n" + "=" * 55)
    print("  HASIL PEMROSESAN")
    print("=" * 55)
    for r in results:
        print(f"\nPasien {r['patient_id']}:")
        print(f"  Heart Rate : {r['avg_hr']} bpm  → {r['hr_status']}")
        print(f"  SpO2       : {r['avg_spo2']} %    → {r['spo2_status']}")

    print(f"\nWaktu eksekusi (Paralel) : {end_time - start_time:.4f} detik")
    print(f"Estimasi sekuensial      : ~{NUM_PATIENTS:.0f} detik")
    print(f"Speedup                  : ~{NUM_PATIENTS / (end_time - start_time):.1f}x lebih cepat")
    print("=" * 55)
