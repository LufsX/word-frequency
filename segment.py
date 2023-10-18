import concurrent.futures
import datetime
import jieba
import os
import re
import sys

character_pattern = re.compile(r"^[\u4e00-\u9fa5]+$")


def segment_lines(lines):
    seg_list = []
    for line in lines:
        words = jieba.cut(line)
        line = ""
        for word in words:
            if character_pattern.match(word):
                line = line + word + " "
        seg_list.append(line)
    return seg_list


def process_segment_large_file(
    input_file_path,
    output_file_path,
    lines_per_process=2000,
    num_processes=max(1, os.cpu_count() - 1),
):
    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 使用 {num_processes} 线程开始处理 {input_file_path}"
    )

    with open(input_file_path, "r", encoding="utf-8") as i:
        lines = i.readlines()

    chunks = [
        lines[i : i + lines_per_process]
        for i in range(0, len(lines), lines_per_process)
    ]

    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        results = list(executor.map(segment_lines, chunks))

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 处理 {input_file_path} 完成")

    with open(output_file_path, "w", encoding="utf-8") as o:
        for result in results:
            for line in result:
                o.write(line + "\n")

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 保存到 {output_file_path}")


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python3 {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_segment_large_file(input_file, output_file)