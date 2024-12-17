import json
import re

def read_jsonl(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        return [json.loads(line)for line in f]

def clean_data(data):
    cleaned_data=[]
    seen_dialogues=set()
    for item in data:
        dialogue=item.get("dialogue","").strip()
        print(f"原始对话：{dialogue}")

        if not dialogue:
            print("跳过空对白")
            continue
        if  dialogue  in seen_dialogues:
            print(f"跳过重复对白：{dialogue}")
            continue

        if not re.search(r'曹操|操', dialogue):
            continue

        dialogue=re.sub(r'\s+','',dialogue)
        dialogue=re.sub(r'[^\w\s\,。!?]','',dialogue)

        cleaned_data.append({"dialogue":dialogue})
        seen_dialogues.add(dialogue)

    return cleaned_data

def save_to_jsonl(data,output_file):
    with open(output_file,'w',encoding='utf_8') as f:
        for item in data:
            json.dump(item,f,ensure_ascii=False)
            f.write('\n')

def main():
    input_file='C:/Users/15270/PycharmProjects/纯正古人/cao_cao_dialoues.jsonl'
    output_file='cao_cao_cleaned.jsonl'

    data=read_jsonl(input_file)
    cleaned_data=clean_data(data)

    save_to_jsonl(cleaned_data,output_file)
    print(f"数据清洗完成，已保存到{output_file}")

if __name__ == "__main__":
    main()