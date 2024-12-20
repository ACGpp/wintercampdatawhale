import re


# 读取《三国演义》文本文件
def read_text_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


# 提取包含"曹操"或"操"的句子
def extract_sentences(text):
    # 正则表达式匹配包含“曹操”或“操”的句子
    pattern = r"([^.。]*曹操[^.。]*。|[^.。]*操[^.。]*。)"
    sentences = re.findall(pattern, text)
    return sentences


# 将提取的句子保存到txt文件中
def save_to_txt(sentences, output_file):
    with open(output_file, 'w', encoding='utf-8') as f:
        for sentence in sentences:
            f.write(sentence + '\n')


# 主函数
def main():
    input_file = 'C:/Users/15270/PycharmProjects/纯正古人/《三国演义》【爱上阅读_www.isyd.net】.txt'  # 《三国演义》的文本文件路径
    output_file = 'cao_cao_sentences.txt'  # 输出的txt文件路径

    # 读取文本
    text = read_text_file(input_file)

    # 提取相关句子
    sentences = extract_sentences(text)

    # 将句子保存到txt文件
    save_to_txt(sentences, output_file)
    print(f"提取的句子已保存到 {output_file}")


if __name__ == "__main__":
    main()
