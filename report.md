ALGORITHM ANALYSIS PROJECT
QUICK SORT AND HEAP SORT
1. Objective / Amaç
EN: This project implements and analyzes Quick Sort and Heap Sort in Python. It explains their operation, theoretical time and auxiliary-space complexity, and the situations in which each algorithm may be suitable.

TR: Bu proje, Quick Sort ve Heap Sort algoritmalarını Python ile uygular ve analiz eder. Algoritmaların çalışma mantığını, teorik zaman ve ek bellek karmaşıklıklarını ve hangi durumlarda uygun olabileceklerini açıklar.
2. Quick Sort / Hızlı Sıralama
EN: Quick Sort is a divide-and-conquer algorithm. This implementation chooses the last element as the pivot. The partition procedure places values less than or equal to the pivot on its left and larger values on its right. The algorithm then recursively sorts both parts.

TR: Quick Sort, böl ve yönet yaklaşımını kullanan bir algoritmadır. Bu uygulamada pivot olarak son eleman seçilir. Partition işlemi, pivot değerinden küçük veya eşit elemanları sola, büyük değerleri sağa yerleştirir. Ardından iki bölüm özyinelemeli olarak sıralanır.

EN: The pivot choice matters. If partitions are consistently very unbalanced, such as with already sorted data when the last element is always chosen, the running time can reach O(n²). The average and best-case time complexity is O(n log n).

TR: Pivot seçimi önemlidir. Bölümler sürekli dengesiz oluşursa, örneğin son elemanın pivot seçildiği bu uygulamada girdi zaten sıralıysa, çalışma süresi O(n²) olabilir. Ortalama ve en iyi durum zaman karmaşıklığı O(n log n)'dir.
3. Heap Sort / Yığın Sıralaması
EN: Heap Sort first builds a max heap, where each parent is greater than or equal to its children. The largest value is at the root. The algorithm swaps the root with the last value in the heap, shrinks the heap, and restores the max-heap property. Repeating this process produces ascending order.

TR: Heap Sort önce her ebeveynin çocuklarından büyük veya eşit olduğu bir max-heap oluşturur. En büyük değer kökte bulunur. Algoritma kökü yığının son elemanıyla değiştirir, yığın boyutunu küçültür ve max-heap özelliğini yeniden kurar. Bu işlem tekrarlandığında artan sıralama elde edilir.

EN: Building the heap takes O(n) time, and the repeated extraction phase takes O(n log n). The overall best, average, and worst-case time complexity is O(n log n).

TR: Yığının oluşturulması O(n) zaman alır; en büyük elemanın tekrar tekrar çıkarılması ise O(n log n) sürer. Toplam en iyi, ortalama ve en kötü durum zaman karmaşıklığı O(n log n)'dir.
4. Complexity Analysis / Karmaşıklık Analizi
Algorithm / Algoritma	Best / En iyi	Average / Ortalama	Worst / En kötü	Auxiliary space / Ek bellek
Quick Sort	O(n log n)	O(n log n)	O(n²)	Average O(log n), worst O(n) call stack
Heap Sort	O(n log n)	O(n log n)	O(n log n)	O(1) auxiliary space for this iterative outer algorithm; recursive heapify uses O(log n) stack in this implementation


EN: Space note: both functions copy the input list, so total extra storage in this particular Python interface includes O(n) for that copy. The table's auxiliary-space column describes the algorithmic workspace apart from the returned/input copy. Quick Sort's recursion stack is O(log n) on average and O(n) in the worst case. Heap Sort's heap storage is in-place, but this recursive heapify implementation can use O(log n) call-stack space.

TR: Bellek notu: Her iki fonksiyon da girdinin kopyasını oluşturur; bu nedenle bu Python arayüzünde toplam ek alan, kopya nedeniyle O(n) içerir. Tablodaki ek bellek sütunu, döndürülen/girdi kopyası dışındaki algoritmik çalışma alanını açıklar. Quick Sort çağrı yığını ortalama O(log n), en kötü durumda O(n)'dir. Heap Sort yığın yapısını yerinde kullanır; ancak bu uygulamadaki özyinelemeli heapify işlemi O(log n) çağrı yığını kullanabilir.
5. Comparison and Use Cases / Karşılaştırma ve Kullanım Alanları
EN: Quick Sort is often fast in practice because its operations have good locality and low constant overhead, but performance depends on pivot selection and can degrade to O(n²). Heap Sort provides an O(n log n) worst-case time guarantee and does not require a separate array for the heap itself, although its access pattern can be less cache-friendly. Neither implementation is stable.

TR: Quick Sort, bellek erişim yerelliği ve düşük sabit maliyetleri nedeniyle pratikte çoğu zaman hızlıdır; ancak performansı pivot seçimine bağlıdır ve O(n²)'ye düşebilir. Heap Sort, O(n log n) en kötü durum garantisi sunar ve yığının kendisi için ayrı bir dizi gerektirmez; buna karşılık bellek erişimleri önbellek açısından daha az verimli olabilir. Bu iki uygulama da kararlı değildir.

EN: Quick Sort is a reasonable choice when average practical speed is important and pivot selection is handled carefully. Heap Sort is useful when a predictable worst-case time bound is important. Actual performance should be measured on representative data rather than assumed.

TR: Ortalama pratik hız önemliyse ve pivot seçimi dikkatle ele alınıyorsa Quick Sort uygun bir seçim olabilir. En kötü durum için öngörülebilir zaman sınırı önemliyse Heap Sort yararlıdır. Gerçek performans varsayılmamalı, temsili veriler üzerinde ölçülmelidir.
6. Testing / Testler
EN: The supplied Python file tests empty and single-element lists, mixed values, duplicate values, ascending and descending inputs, and negative numbers. Each result is compared with Python's built-in sorted() function. The tests also verify that both functions return the expected ascending order.

TR: Verilen Python dosyası boş ve tek elemanlı listeleri, karışık değerleri, tekrar eden değerleri, artan ve azalan sıralı girdileri ve negatif sayıları test eder. Her sonuç Python'ın yerleşik sorted() fonksiyonuyla karşılaştırılır. Testler iki fonksiyonun da doğru artan sıralamayı ürettiğini doğrular.

Expected command / Çalıştırma komutu:
python quick_sort_heap_sort.py
Expected output / Beklenen çıktı:
All 8 test cases passed for both algorithms.
7. Limitations / Sınırlılıklar
EN: This educational Quick Sort always chooses the last element as pivot and may hit Python's recursion limit on large, already sorted inputs. A randomized or median-based pivot strategy can reduce this risk. For a fair timing experiment, use repeated trials and several input patterns, and report the Python version and machine used.

TR: Eğitim amaçlı bu Quick Sort her zaman son elemanı pivot seçer ve büyük, zaten sıralı girdilerde Python'ın özyineleme sınırına ulaşabilir. Rastgele veya medyan tabanlı pivot seçimi bu riski azaltabilir. Adil süre ölçümü için birden fazla deneme ve farklı girdi türleri kullanılmalı; Python sürümü ve test yapılan bilgisayar raporlanmalıdır.
8. AI Usage Statement / Yapay Zekâ Kullanım Beyanı
[Model/Tool Name and Version]: ChatGPT (GPT-6) was used in the code, explanation, and analysis sections of this project. The tool was utilized via prompts requesting clarification and editing of code comments, correction of errors in the code, and translation. The output has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work.

Türkçe açıklama: Bu projede ChatGPT (GPT-6), kod açıklamalarını düzenlemek, kodlardaki hataları gidermeye yardımcı olmak ve bazı açıklamaların çevirisini yapmak amacıyla kullanılmıştır. Üretilen çıktılar teknik doğruluk, güvenlik ve özgünlük açısından tarafımdan incelenip doğrulanmıştır. Çalışmanın tüm sorumluluğu bana aittir.
Appendix A. Source Code / Ek A. Kaynak Kod
"""
Algorithm Analysis Project: Quick Sort and Heap Sort
Language: Python

Both functions return a sorted copy of the input list and leave the original
list unchanged. The implementation is intended for learning and analysis.
"""


def quick_sort(arr):
    """Return a sorted copy of arr using Quick Sort."""
    items = arr.copy()  # Copy input so the caller's list is not modified.

    def partition(low, high):
        pivot = items[high]  # Select the last element as the pivot.
        i = low - 1          # Last index of the region <= pivot.

        # Move each value <= pivot to the left side of the partition.
        for j in range(low, high):
            if items[j] <= pivot:
                i += 1
                items[i], items[j] = items[j], items[i]

        # Place the pivot between the two partition regions.
        items[i + 1], items[high] = items[high], items[i + 1]
        return i + 1

    def sort(low, high):
        # A segment with zero or one item is already sorted.
        if low < high:
            pivot_index = partition(low, high)
            sort(low, pivot_index - 1)  # Sort the left partition.
            sort(pivot_index + 1, high) # Sort the right partition.

    sort(0, len(items) - 1)
    return items


def heap_sort(arr):
    """Return a sorted copy of arr using Heap Sort."""
    items = arr.copy()  # Work on a copy to preserve the original list.
    n = len(items)

    def heapify(heap_size, root):
        """Restore the max-heap property in the subtree rooted at root."""
        largest = root
        left = 2 * root + 1
        right = 2 * root + 2

        # Check whether the left child is larger than the current largest.
        if left < heap_size and items[left] > items[largest]:
            largest = left

        # Check whether the right child is larger than the current largest.
        if right < heap_size and items[right] > items[largest]:
            largest = right

        # If a child is larger, swap and continue restoring the heap.
        if largest != root:
            items[root], items[largest] = items[largest], items[root]
            heapify(heap_size, largest)

    # Build a max heap from the unsorted list.
    for i in range(n // 2 - 1, -1, -1):
        heapify(n, i)

    # Move the maximum (root) to the end, then repair the reduced heap.
    for end in range(n - 1, 0, -1):
        items[0], items[end] = items[end], items[0]
        heapify(end, 0)

    return items


def run_tests():
    """Run representative correctness tests for both algorithms."""
    test_cases = [
        [],
        [1],
        [5, 2, 8, 1, 3],
        [4, 4, 4, 4],
        [9, 7, 5, 3, 1],
        [1, 2, 3, 4, 5],
        [-3, 0, 7, -1, 2],
        [3, -2, 3, 0, -2, 8, 1],
    ]

    for values in test_cases:
        expected = sorted(values)
        assert quick_sort(values) == expected
        assert heap_sort(values) == expected

    print(f"All {len(test_cases)} test cases passed for both algorithms.")


if __name__ == "__main__":
    run_tests()