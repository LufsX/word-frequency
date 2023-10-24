import pypinyin
import datetime
import sys


def add_pinyin(input_file, output_file, filter=0):
    start_time = datetime.datetime.now()
    with open(input_file, "r", encoding="utf-8") as i:
        lines = i.readlines()

    with open(output_file, "w", encoding="utf-8") as o:
        wait_to_write = []
        n = 0

        for line in lines:
            n += 1
            zi, num = line.split("\t")
            zi_pinyin = " ".join(
                [p[0] for p in pypinyin.pinyin(zi, style=pypinyin.Style.NORMAL)]
            )
            if int(num) < filter:
                wait_to_write.clear()
                break
            wait_to_write.append(f"{zi}\t{zi_pinyin}\t{num}")
            if n % 100000 == 0:
                o.writelines(wait_to_write)
                wait_to_write.clear()
        if wait_to_write:
            o.writelines(wait_to_write)
            wait_to_write.clear()

    end_time = datetime.datetime.now()
    print(f"添加完毕，总共耗时 {end_time - start_time}")


if __name__ == "__main__":
    if len(sys.argv) <= 2:
        print(f"Usage: python {sys.argv[0]} path/to/input_file path/to/output_file")
        exit()

    input_file = sys.argv[1]
    output_file = sys.argv[2]

    add_pinyin(input_file, output_file, filter=10)
