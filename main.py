from model import switch_test, switch_num
import pandas as pd
import time as tm

test_names_list = ["Тест Ферма", "Тест Лемана", "Тест Соловея — Штрассена", "Тест Миллера — Рабина"]
num_ranges_list = ["0 - 2^7", "2^7 - 2^12", "2^12 - 2^17", "2^17 - 2^20", "2^20 - 2^22", "2^22 - 2^24",
                   "2^24 - 2^26"]
num_ranges = []
test_names = []
counts = []
times = []

for name_iter in range(len(test_names_list)):
    print("Текущий тест - ", test_names_list[name_iter])
    for num_range in range(len(num_ranges_list)):
        count = 0
        print("Текущий диапазон - ", num_ranges_list[num_range])
        start = tm.time()
        prev_mid_time = start
        for i in switch_num(num_range):
            if (i - 1) % 10000 == 0:
                mid_time = tm.time()
                #print("Текущая луковица - {}; сколько времени со старта диапазона - {}; а вот сколько времени от предыдущих {} - {}; кол-во вер. простых чисел - {}".format(i, round(mid_time - start, 2), 10000, round(mid_time - prev_mid_time, 2), count))
                prev_mid_time = mid_time
            if switch_test(name_iter, i):
                count += 1
        end = tm.time()
        time = end - start
        print("Законченный диапазон - ", num_ranges_list[num_range])
        num_ranges.append(num_ranges_list[num_range])
        test_names.append(test_names_list[name_iter])
        print("Кол-во вер. простых чисел - {}; затраченное время - {}".format(count, round(time, 4)))
        counts.append(count)
        times.append(round(time, 4))
    print("Законченный тест - ", test_names_list[name_iter])

results = {"Диапазоны чисел": num_ranges, "Тест": test_names, "Кол-во вер. простых": counts, "Время": times}
df = pd.DataFrame(results)
df.to_csv("tests-results.csv", index=False, encoding='utf-8')
