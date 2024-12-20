import json

# 预设的系统提示
system_prompt = "你是三国时期的曹操，现为一位具有军事战略智慧和深厚历史背景的历史人物。你不知晓现代科技、科学原理或任何超出三国时期的事物。例如，你从未听说过飞机、瑞士卷或现代的计算机技术等任何现代发明。你所拥有的知识局限于三国时代的历史事件、人物、军事战略等内容。请在与我对话时仅使用三国时期的信息进行回答。"


# 读取已有的jsonl文件
def read_jsonl(file_path):
    data = []
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line))
    return data


# 修改数据并转化为Alpaca格式
def convert_to_alpaca_format(data):
    alpaca_data = []
    for entry in data:
        # 构建 Alpaca 格式的数据
        alpaca_entry = {
            "instruction": system_prompt,
            "input": entry["input"],  # 使用原数据中的问题
            "output": entry["target"]  # 使用原数据中的答案
        }
        alpaca_data.append(alpaca_entry)
    return alpaca_data


# 保存修改后的数据为新的alpaca格式的jsonl文件
def save_to_alpaca_jsonl(data, file_name="alpaca_data.jsonl"):
    with open(file_name, 'w', encoding='utf-8') as f:
        for item in data:
            json.dump(item, f, ensure_ascii=False)
            f.write('\n')


# 主程序
def process_jsonl(file_path, output_file="alpaca_data.jsonl"):
    # 1. 读取原始数据
    data = read_jsonl(file_path)

    # 2. 转化为Alpaca格式
    alpaca_data = convert_to_alpaca_format(data)

    # 3. 保存转化后的数据
    save_to_alpaca_jsonl(alpaca_data, output_file)
    print(f"转换后的数据已保存到：{output_file}")


# 调用处理函数
input_file = 'C:/Users/15270/Downloads/三国演义.jsonl'  # 替换为你自己的文件路径
process_jsonl(input_file)
