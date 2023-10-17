import datetime
import opencc
import sys


def process_file(input_file_path, output_file_path):
    converter = opencc.OpenCC("t2s.json")

    print(f"{datetime.datetime.now().strftime("%H:%M:%S.%f")} 开始处理 {input_file_path}")

    with open(input_file_path, "r", encoding="utf-8") as i:
        content = i.read()

    converted_content = converter.convert(content)

    print(f"{datetime.datetime.now().strftime("%H:%M:%S.%f")} 处理 {input_file_path} 完成")

    with open(output_file_path, "w", encoding="utf-8") as o:
        o.write(converted_content)

    print(f"{datetime.datetime.now().strftime("%H:%M:%S.%f")} 保存到 {output_file_path}")

if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python3 {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    process_file(input_file, output_file)
