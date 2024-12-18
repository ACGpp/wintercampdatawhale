import json
import re

def read_jsonl(file_path):
    with open(file_path,'r',encoding='utf-8')as f:
        lines=f.readlines()
        return [json.loads(line)for line in lines]

def convert_to_alpaca_format(data):
    alpaca_data=[]

    for item in data:
        dialogue=item.get("dialogue","").strip()

        if not dialogue:
            continue

        if not re.search(r'曹操|操',dialogue):
            continue

        alpaca_item={
            "instruction":"请以曹操的风格回答以下问题，结合三国时期的背景和曹操的个性特点，注意，在对话中出现的一切不属于三国时期之前的事物曹操都不知道，需要对话者对你进行解释后你才能知道，并且以三国时期的知识对新事物进行理解消化",
            "input":dialogue,
            "output":f"这是曹操的回答:{dialogue}"
        }

        alpaca_data.append(alpaca_item)
    return alpaca_data

def save_to_jsonl(data,output_file):
    with open(output_file,'w',encoding='utf-8')as f:
        for item in data:
            json.dump(item,f,ensure_ascii=False)
            f.write('\n')

def main():
    input_file='C:/Users/15270/PycharmProjects/纯正古人/cao_cao_cleaned.jsonl'
    output_file="cao_cao_alpaca.jsonl"

    data=read_jsonl(input_file)
    print(f"读取到的原始数据条数:{len(data)}")

    alpaca_data=convert_to_alpaca_format(data)
    print(f"转换后的数据条数：{len(alpaca_data)}")

    save_to_jsonl(alpaca_data,output_file)
    print(f"已保存")

if __name__ == "__main__":
    main()
