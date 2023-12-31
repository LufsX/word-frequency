import datetime
import multiprocessing
import opencc
import sys


def process_file(input_file_path, output_file_path):
    converter = opencc.OpenCC("t2s")

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 开始处理 {input_file_path}")

    with open(input_file_path, "r", encoding="utf-8") as i:
        content = i.read()

    converted_content = converter.convert(content)

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 处理 {input_file_path} 完成")

    with open(output_file_path, "w", encoding="utf-8") as o:
        o.write(converted_content)

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 保存到 {output_file_path}")


def convert_lines(lines):
    converter = opencc.OpenCC("t2s")
    content = "".join(lines)
    return converter.convert(content)


def process_large_file(
    input_file_path,
    output_file_path,
    lines_per_process=2000,
    num_processes=max(1, multiprocessing.cpu_count() - 1),
):
    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 使用 {num_processes} 线程开始对 {input_file_path} 进行预处理"
    )

    with open(input_file_path, "r", encoding="utf-8") as i:
        lines = i.readlines()

    chunks = [
        lines[i : i + lines_per_process]
        for i in range(0, len(lines), lines_per_process)
    ]

    with multiprocessing.Pool(num_processes) as pool:
        results = pool.map(convert_lines, chunks)

    print(f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 处理 {input_file_path} 完成")

    with open(output_file_path, "w", encoding="utf-8") as o:
        for result in results:
            o.write(result)

    print(
        f"{datetime.datetime.now().strftime('%H:%M:%S.%f')} 已将预处理过的文件保存至 {output_file_path}"
    )


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_large_file(input_file, output_file)
