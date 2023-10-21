import datetime
import jieba
import multiprocessing
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


def process_segment_chunk(chunk):
    return segment_lines(chunk)


def process_segment_large_file(
    input_file_path,
    output_file_path,
    lines_per_process=2000,
    num_processes=max(1, multiprocessing.cpu_count() - 1),
):
    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 使用 {num_processes} 线程对 {input_file_path} 进行分词"
    )

    with open(input_file_path, "r", encoding="utf-8") as i:
        lines = i.readlines()

    chunks = [
        lines[i : i + lines_per_process]
        for i in range(0, len(lines), lines_per_process)
    ]

    with multiprocessing.Pool(processes=num_processes) as pool:
        results = list(pool.map(process_segment_chunk, chunks))

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 对 {input_file_path} 分词完成")

    with open(output_file_path, "w", encoding="utf-8") as o:
        for result in results:
            for line in result:
                o.write(line + "\n")

    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 已将分词后的文件保存至 {output_file_path}"
    )


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python3 {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_segment_large_file(input_file, output_file)
