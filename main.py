import statistics # Standard library for mean, min, max, sum

# --- Constants for better readability and maintainability ---
# Using constants avoids 'magic numbers' and makes values easy to update.
MIN_NUMBERS_REQUIRED = 1
DEFAULT_THRESHOLD = 50
ERROR_INVALID_INPUT = "Hata: Geçersiz giriş. Lütfen sadece sayı girin."
ERROR_NOT_ENOUGH_NUMBERS = f"Hata: En az {MIN_NUMBERS_REQUIRED} sayı girmelisiniz."

def get_user_numbers() -> list[float]:
    """
    Kullanıcıdan sayıları alır ve geçerli sayı listesi döndürür.
    Geçersiz girişleri filtreler ve kullanıcıya bilgi verir.
    """
    print("Lütfen sayıları virgülle ayırarak girin (örn: 10, 20.5, 30).")
    print("İşlemi bitirmek için boş bırakıp Enter'a basın.")

    numbers: list[float] = []
    while True:
        user_input = input("> ").strip()
        if not user_input:
            break

        try:
            # --- Input validation for robustness ---
            # Ensures the program handles unexpected input gracefully.
            current_numbers = [float(s.strip()) for s in user_input.split(',') if s.strip()]
            if not current_numbers:
                print(ERROR_INVALID_INPUT)
                continue
            numbers.extend(current_numbers)
        except ValueError:
            print(ERROR_INVALID_INPUT)
            continue

    # --- Early exit for invalid state ---
    # Improves readability by handling edge cases at the beginning.
    if len(numbers) < MIN_NUMBERS_REQUIRED:
        print(ERROR_NOT_ENOUGH_NUMBERS)
        return []
    
    return numbers

def calculate_statistics(data: list[float]) -> dict[str, float]:
    """
    Verilen sayı listesi için temel istatistikleri hesaplar.
    
    Args:
        data: Sayıların listesi.
        
    Returns:
        Toplam, ortalama, minimum ve maksimum değerleri içeren bir sözlük.
    """
    if not data:
        return {"sum": 0.0, "average": 0.0, "min": 0.0, "max": 0.0}
    
    # --- Using built-in functions for clarity and efficiency ---
    # Avoids re-implementing standard algorithms.
    total = sum(data)
    avg = statistics.mean(data)
    minimum = min(data)
    maximum = max(data)
    
    return {
        "sum": total,
        "average": avg,
        "min": minimum,
        "max": maximum
    }

def filter_numbers_above_threshold(data: list[float], threshold: float) -> list[float]:
    """
    Verilen sayı listesinden belirli bir eşik değerinin üzerindeki sayıları filtreler.
    
    Args:
        data: Sayıların listesi.
        threshold: Filtreleme için kullanılacak eşik değeri.
        
    Returns:
        Eşik değerinin üzerindeki sayıların listesi.
    """
    # --- List comprehensions for concise and readable filtering ---
    # A common Pythonic way to create new lists based on existing ones.
    return [num for num in data if num > threshold]

def display_results(original_numbers: list[float], stats: dict[str, float], filtered_numbers: list[float], threshold: float) -> None:
    """
    Hesaplanan istatistikleri ve filtrelenmiş sayıları kullanıcıya gösterir.
    
    Args:
        original_numbers: Orijinal sayı listesi.
        stats: Hesaplanan istatistikleri içeren sözlük.
        filtered_numbers: Eşik değerinin üzerindeki filtrelenmiş sayı listesi.
        threshold: Filtreleme için kullanılan eşik değeri.
    """
    print("\n--- Sonuçlar ---")
    if not original_numbers:
        print("İşlenecek sayı bulunamadı.")
        return

    print(f"Girilen Sayılar: {original_numbers}")
    print(f"Toplam: {stats['sum']:.2f}")
    print(f"Ortalama: {stats['average']:.2f}")
    print(f"Minimum: {stats['min']:.2f}")
    print(f"Maksimum: {stats['max']:.2f}")
    
    if filtered_numbers:
        print(f"Eşik Değeri ({threshold}) Üzerindeki Sayılar: {filtered_numbers}")
    else:
        print(f"Eşik Değeri ({threshold}) Üzerinde sayı bulunamadı.")

def main() -> None:
    """
    Ana program akışını yönetir.
    Kullanıcıdan sayıları alır, istatistikleri hesaplar ve sonuçları gösterir.
    """
    print("Python Betiği Temizliği ve Teslim Edilebilirliği Örneği")
    print("------------------------------------------------------")

    numbers = get_user_numbers()
    if not numbers:
        return # Exit if no valid numbers were entered

    stats = calculate_statistics(numbers)
    
    # --- Using constants for configurable values ---
    # Makes the code easier to modify and understand.
    filtered = filter_numbers_above_threshold(numbers, DEFAULT_THRESHOLD)
    
    display_results(numbers, stats, filtered, DEFAULT_THRESHOLD)

# --- Main execution guard for script reusability ---
# Ensures 'main()' is called only when the script is executed directly.
if __name__ == "__main__":
    main()
