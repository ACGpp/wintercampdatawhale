import re

def read_txt_file(file_path):
     with open(file_path,'r',encoding='utf-8')as f:
         return f.readlines()

def clean_sentences(sentences):
    cleaned_sentences=[]
    for sentence in sentences:
       sentence=sentence.strip()
       sentence = re.sub(r'[^\w\s,。!?]','',sentence)

       if len(sentence)>3:
           cleaned_sentences.append(sentence)

    return  cleaned_sentences

def split_dataset(sentences,max_length=2000):
    dataset1=sentences[:max_length]
    dataset2=sentences[max_length:]
    return dataset1,dataset2

def save_to_txt(sentences,output_file):
    with open(output_file,'w',encoding='utf-8')as f:
        for sentence in sentences:
            f.write(sentence+'\n')

def main():
    input_file='C:/Users/15270/PycharmProjects/纯正古人/cao_cao_sentences.txt'
    cleaned_file1='cleaned_cao_cao_sentences_1.txt'
    cleaned_file2 = 'cleaned_cao_cao_sentences_2.txt'

    sentences=read_txt_file(input_file)

    cleaned_sentences=clean_sentences(sentences)
    print(f"清洗后的句子数量{len(cleaned_sentences)}")

    dataset1,dataset2=split_dataset(cleaned_sentences)

    save_to_txt(dataset1,cleaned_file1)
    save_to_txt(dataset2,cleaned_file2)

    print(f"两个数据集已保存：{cleaned_file1}和{cleaned_file2}")

if __name__=="__main__":
    main()

