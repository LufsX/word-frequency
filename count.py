from collections import Counter
import datetime
import multiprocessing
import sys


def count_words_in_chunk(chunk):
    return Counter(chunk.split())


def count_large_file_chunk(chunk):
    return sum(map(count_words_in_chunk, chunk), Counter())


def count_large_file(
    input_file_path,
    output_file_path,
    lines_per_process=1000,
    num_processes=max(1, multiprocessing.cpu_count() - 1),
):
    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 使用 {num_processes} 线程开始对 {input_file_path} 词频统计"
    )

    with open(input_file_path, "r", encoding="utf-8") as i:
        lines = i.readlines()

    chunks = [
        lines[i : i + lines_per_process]
        for i in range(0, len(lines), lines_per_process)
    ]

    with multiprocessing.Pool(processes=num_processes) as pool:
        word_lists = pool.map(count_large_file_chunk, chunks)

    counter = sum(word_lists, Counter())

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 统计 {input_file_path} 完成")

    with open(output_file_path, "w", encoding="utf-8") as file:
        sorted_data = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        for word, count in sorted_data:
            file.write(f"{word}\t{count}\n")

    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 已将统计结果保存至 {output_file_path}"
    )


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    count_large_file(input_file, output_file)
