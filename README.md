# word-frequency

词频统计小工具(?)

写的烂，没啥用（

# 使用

## 安装依赖

```bash
pip install -r requirements.txt
```

## 运行

```bash
python build.py
```

# 工具拆分

## 下载 Wiki 数据

```bash
python download.py
```

## 转换为纯文本

```bash
python wiki2txt.py path/to/wiki_articles_data path/to/output_file
```

## 转换简体/剔除非中文字符

```bash
python preprocessing.py path/to/input_file path/to/output_file
```

## 统计

```bash
python count.py path/to/input_file path/to/output_file
```

## 注音

```bash
python pinyin.py path/to/input_file path/to/output_file
```
