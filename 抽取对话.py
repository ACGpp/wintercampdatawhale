import re
import json

file_path='C:/Users/15270/PycharmProjects/extract-dialogue/《三国演义》【爱上阅读_www.isyd.net】.txt'

def read_file(file_path):
    with open(file_path,'r',encoding='utf-8')as file:
        text =file.read()
    return text

def extract_cao_cao_dialogue(text):
    pattern=r"([^.。]*曹操[^.。]*。)|([^.。]*操[^.。]*。)"
    cao_cao_mentions=re.findall(pattern,text)

    return [match[0] or match[1] for match in cao_cao_mentions]

def save_to_jsonl(data,output_file):
    with open(output_file,'a',encoding='utf-8') as f:
        for item in data:
            json.dump({"dialogue":item},f,ensure_ascii=False)
            f.write('\n')

def main():
    text=read_file(file_path)
    cao_cao_dialogues=extract_cao_cao_dialogue(text)
    for dialogue in cao_cao_dialogues:
        print(dialogue)

    output_file='cao_cao_dialoues.jsonl'
    save_to_jsonl(cao_cao_dialogues,output_file)
    print(f"提取完成，已保存到{output_file}")

if __name__ == "__main__":
    main()