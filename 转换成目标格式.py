import json
import re

def read_jsonl(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        lines=f.readlines()
        return [json.loads(line) for line in lines]

def clean_data(data):
    cleaned_data=[]
    seen_dialogues=set()

    for item in data:
        dialogue=item.get("dialogue","").strip()
        print(f"原始对话：{dialogue}")
        if not dialogue or dialogue in seen_dialogues:
            continue
        if not re.search(r'曹操|操',dialogue):
            continue

        dialogue = re.sub(r'\s+','',dialogue)
        dialogue=re.sub(r'[^\w\s、，。！？]','',dialogue)

        item_with_metadata={
        "dialogue":dialogue,
        "metadata":{
            "character":"曹操 ",
            "era":"三国时期",
            "knowledge_scope":"仅限三国时期的知识，军事战略，历史背景"
         }
        }
        cleaned_data.append(item_with_metadata)
        seen_dialogues.add(dialogue)
    return cleaned_data

def save_to_jsonl(data,output_file):
    with open(output_file,'w',encoding='utf-8')as f:
        for item in data:
            json.dump(item, f ,ensure_ascii=False)
            f.write('\n')

def main():
    file_path='C:/Users/15270/PycharmProjects/纯正古人/cao_cao_dialoues.jsonl'
    output_file='cleaned_cao_cao_dialoues2.jsonl'
    data=read_jsonl(file_path)
    print(f"读取到的原始数据条数: {len(data)}")
    cleaned_data=clean_data(data)
    print(f"清洗后的数据条数: {len(cleaned_data)}")

    save_to_jsonl(cleaned_data,output_file)

    print(f"cleaned")

if __name__=="__main__":
    main()