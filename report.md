# Algorithm Analysis Project

## Quick Sort and Heap Sort

This report explains the implementation, theoretical complexity, correctness testing, and limitations of **Quick Sort** and **Heap Sort**. English and Turkish explanations are provided together for easy comparison.

---

## Contents

- [1. Objective / Amaç](#1-objective--amaç)
- [2. Quick Sort / Hızlı Sıralama](#2-quick-sort--hızlı-sıralama)
- [3. Heap Sort / Yığın Sıralaması](#3-heap-sort--yığın-sıralaması)
- [4. Complexity Analysis / Karmaşıklık Analizi](#4-complexity-analysis--karmaşıklık-analizi)
- [5. Comparison and Use Cases / Karşılaştırma ve Kullanım Alanları](#5-comparison-and-use-cases--karşılaştırma-ve-kullanım-alanları)
- [6. Testing / Testler](#6-testing--testler)
- [7. Limitations / Sınırlılıklar](#7-limitations--sınırlılıklar)
- [8. AI Usage Statement / Yapay Zekâ Kullanım Beyanı](#8-ai-usage-statement--yapay-zekâ-kullanım-beyanı)
- [Appendix A: Source Code / Ek A: Kaynak Kod](#appendix-a-source-code--ek-a-kaynak-kod)

---

## 1. Objective / Amaç

**English**

This project implements and analyzes Quick Sort and Heap Sort in Python. It explains how the algorithms work, their theoretical time and auxiliary-space complexity, and the situations in which each algorithm may be suitable.

**Türkçe**

Bu proje, Quick Sort ve Heap Sort algoritmalarını Python ile uygular ve analiz eder. Algoritmaların çalışma mantığını, teorik zaman ve ek bellek karmaşıklıklarını ve hangi durumlarda uygun olabileceklerini açıklar.

## 2. Quick Sort / Hızlı Sıralama

**English**

Quick Sort is a divide-and-conquer algorithm. This implementation chooses the last element as the pivot. The partition procedure places values less than or equal to the pivot on its left and larger values on its right. The algorithm then recursively sorts both partitions.

Pivot selection is important. If the partitions are consistently unbalanced—as can happen with already sorted or reverse-sorted data when the last element is always selected—the running time can reach `O(n²)`. The best- and average-case time complexity is `O(n log n)`.

**Türkçe**

Quick Sort, böl ve yönet yaklaşımını kullanan bir algoritmadır. Bu uygulamada pivot olarak son eleman seçilir. Partition işlemi, pivot değerinden küçük veya eşit elemanları sola, büyük değerleri sağa yerleştirir. Ardından iki bölüm özyinelemeli olarak sıralanır.

Pivot seçimi önemlidir. Bölümler sürekli dengesiz oluşursa — son elemanın pivot seçildiği bu uygulamada sıralı veya ters sıralı girdilerde görülebileceği gibi — çalışma süresi `O(n²)` olabilir. En iyi ve ortalama durum zaman karmaşıklığı `O(n log n)`'dir.

## 3. Heap Sort / Yığın Sıralaması

**English**

Heap Sort first builds a max heap, where each parent is greater than or equal to its children. The largest value is at the root. The algorithm swaps the root with the last value in the heap, reduces the heap size, and restores the max-heap property. Repeating this process produces ascending order.

Building the heap takes `O(n)` time, while repeatedly extracting the maximum takes `O(n log n)`. The overall best-, average-, and worst-case time complexity is `O(n log n)`.

**Türkçe**

Heap Sort önce her ebeveynin çocuklarından büyük veya eşit olduğu bir max-heap oluşturur. En büyük değer kökte bulunur. Algoritma kökü yığının son elemanıyla değiştirir, yığın boyutunu küçültür ve max-heap özelliğini yeniden kurar. Bu işlem tekrarlandığında artan sıralama elde edilir.

Yığının oluşturulması `O(n)` zaman alır; en büyük elemanın tekrar tekrar çıkarılması ise `O(n log n)` sürer. En iyi, ortalama ve en kötü durum zaman karmaşıklığı `O(n log n)`'dir.

## 4. Complexity Analysis / Karmaşıklık Analizi

| Property / Özellik | Quick Sort | Heap Sort |
|---|---:|---:|
| Best-case time / En iyi durum | `O(n log n)` | `O(n log n)` |
| Average-case time / Ortalama durum | `O(n log n)` | `O(n log n)` |
| Worst-case time / En kötü durum | `O(n²)` | `O(n log n)` |
| Auxiliary call-stack space / Ek çağrı yığını belleği | Average: `O(log n)`; worst: `O(n)` | Recursive `heapify`: `O(log n)` |
| Stable sorting / Kararlı sıralama | No / Hayır | No / Hayır |

> **Space note / Bellek notu**
>
> **English:** Both functions copy the input list, so this Python interface requires `O(n)` additional storage for that copy. The table describes the algorithmic workspace and call stack separately from the input copy. Quick Sort uses `O(log n)` stack space on average and `O(n)` in the worst case. Heap Sort operates on the copied list, and its recursive `heapify` function can use `O(log n)` call-stack space.
>
> **Türkçe:** Her iki fonksiyon da girdi listesinin kopyasını oluşturduğu için bu Python arayüzü kopya nedeniyle `O(n)` ek bellek kullanır. Tabloda, girdi kopyasından ayrı olarak algoritmanın çalışma alanı ve çağrı yığını gösterilmiştir. Quick Sort ortalama `O(log n)`, en kötü durumda `O(n)` çağrı yığını kullanır. Heap Sort kopyalanan liste üzerinde çalışır; özyinelemeli `heapify` fonksiyonu ise `O(log n)` çağrı yığını kullanabilir.

## 5. Comparison and Use Cases / Karşılaştırma ve Kullanım Alanları

### Quick Sort

- **English:** Quick Sort is often fast in practice because of good memory-access locality and low constant overhead. However, its performance depends on pivot selection and can degrade to `O(n²)`.
- **Türkçe:** Quick Sort, bellek erişim yerelliği ve düşük sabit maliyetleri nedeniyle pratikte çoğu zaman hızlıdır. Ancak performansı pivot seçimine bağlıdır ve `O(n²)`'ye düşebilir.

### Heap Sort

- **English:** Heap Sort guarantees `O(n log n)` worst-case time and does not need a separate array for the heap itself. Its access pattern may, however, be less cache-friendly.
- **Türkçe:** Heap Sort, en kötü durumda `O(n log n)` zaman garantisi sunar ve yığının kendisi için ayrı bir dizi gerektirmez. Buna karşılık bellek erişim düzeni önbellek açısından daha az verimli olabilir.

**English:** Neither implementation is stable. Quick Sort may be suitable when practical average speed is important and pivot selection is handled carefully. Heap Sort is useful when a predictable worst-case running time matters. Actual performance should be measured on representative data rather than assumed.

**Türkçe:** Bu iki uygulama da kararlı sıralama yapmaz. Ortalama pratik hız önemliyse ve pivot seçimi dikkatle ele alınıyorsa Quick Sort uygun olabilir. En kötü durum için öngörülebilir çalışma süresi önemliyse Heap Sort yararlıdır. Gerçek performans varsayılmamalı, temsili veriler üzerinde ölçülmelidir.

## 6. Testing / Testler

**English**

The Python file runs eight correctness test cases. They cover empty and single-element lists, mixed values, duplicates, ascending and descending inputs, and negative numbers. Each algorithm's output is compared with Python's built-in `sorted()` function. Both sorting functions return a sorted copy and leave the original input list unchanged.

**Türkçe**

Python dosyası sekiz doğruluk testi çalıştırır. Testler boş ve tek elemanlı listeleri, karışık değerleri, tekrar eden değerleri, artan ve azalan sıralı girdileri ve negatif sayıları kapsar. Her algoritmanın çıktısı Python'ın yerleşik `sorted()` fonksiyonuyla karşılaştırılır. Her iki sıralama fonksiyonu da sıralanmış bir kopya döndürür ve orijinal girdi listesini değiştirmez.

### Run correctness tests / Doğruluk testlerini çalıştırma

```bash
python quick_sort_heap_sort.py
```

Expected output / Beklenen çıktı:

```text
All 8 test cases passed for both algorithms.
```

### Run the benchmark / Performans ölçümünü çalıştırma

The Python file also includes an optional benchmark mode. It compares median execution times over seven trials for random, ascending, and descending inputs at several input sizes.

Python dosyasında isteğe bağlı bir performans ölçüm modu da bulunur. Farklı girdi boyutlarında rastgele, artan ve azalan listeler için yedi denemenin medyan çalışma sürelerini karşılaştırır.

```bash
python quick_sort_heap_sort.py --benchmark
```

Benchmark timings depend on the Python version and the computer used. / Performans ölçüm sonuçları Python sürümüne ve kullanılan bilgisayara göre değişebilir.

## 7. Limitations / Sınırlılıklar

**English**

This educational Quick Sort implementation always chooses the last element as the pivot. On sufficiently large, already sorted or reverse-sorted inputs, it may create highly unbalanced partitions and reach Python's recursion limit. Randomized or median-based pivot selection can reduce this risk, but it does not remove the theoretical `O(n²)` worst case.

For fair timing experiments, use repeated trials and several input patterns, and report the Python version and machine used.

**Türkçe**

Eğitim amaçlı bu Quick Sort uygulaması her zaman son elemanı pivot seçer. Yeterince büyük, sıralı veya ters sıralı girdilerde çok dengesiz bölümler oluşturabilir ve Python'ın özyineleme sınırına ulaşabilir. Rastgele veya medyan tabanlı pivot seçimi bu riski azaltabilir; ancak teorik `O(n²)` en kötü durumunu ortadan kaldırmaz.

Adil süre ölçümleri için birden fazla deneme ve farklı girdi türleri kullanılmalı; Python sürümü ve test yapılan bilgisayar belirtilmelidir.

## 8. AI Usage Statement / Yapay Zekâ Kullanım Beyanı

**English**

ChatGPT (GPT-6) was used in the code, explanation, and analysis sections of this project. It was used through prompts requesting clarification and editing of code comments, assistance with code errors, and translation. The output has been reviewed and verified by me for technical accuracy, safety, and originality. I bear full responsibility for the work.

**Türkçe**

Bu projede ChatGPT (GPT-6), kod açıklamalarını düzenlemek, kodlardaki hataları gidermeye yardımcı olmak ve bazı açıklamaları çevirmek amacıyla kullanılmıştır. Üretilen çıktılar teknik doğruluk, güvenlik ve özgünlük açısından tarafımdan incelenip doğrulanmıştır. Çalışmanın tüm sorumluluğu bana aittir.

---

## Appendix A: Source Code / Ek A: Kaynak Kod

The complete source code is available in [`quick_sort_heap_sort.py`](./quick_sort_heap_sort.py). For readability, it is not repeated inline here.

Kaynak kodun tamamı [`quick_sort_heap_sort.py`](./quick_sort_heap_sort.py) dosyasında bulunmaktadır. Okunabilirliği korumak için kod burada tekrar edilmemiştir.
