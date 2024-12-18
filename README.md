 # 纯正古人-曹操！创造历程！  
## 数据集构建  
   对收集的三国演义进行抽取对话，实则是将有关曹操或操的句子提取出来，在抽取对话.py文件中
## 数据集清洗
   对构建后的数据集进行清洗（清洗数据.py）
   1. 去除重复项：如果你的数据中存在重复的对话，可以去重，确保每个对话都是唯一的。

   2. 去除无关内容：你可能需要过滤掉一些无关的对话片段或包含特殊字符的内容。例如，剔除掉空字符串、无意义的短语或者乱码。

   3. 文本标准化：统一文本格式，如去除多余的空格、标点符号标准化等。

   4. 检查与“曹操”无关的对话：在提取过程中，可能会包含一些无关的对话。可以通过特定的过滤规则去除这些内容。
   
   5. 处理格式问题：确保 jsonl 文件的每一行格式正确，确保解析时没有错误。
## 数据集格式转换
    我的格式（转换成目标格式.py)样例
  {  
  "dialogue": "曹操道：“宁教我负天下人，休叫天下人负我。”",  
  "metadata": {  
    "character": "曹操",  
    "era": "三国时期",  
    "knowledge_scope": "仅限三国时期的军事战略与历史背景"  
            }  
    }  
   alpaca格式使用转换成alpaca形式.py
## 模型构建
   我使用的是internlm2.5_7b_chat模型，因为它可以进行全量精调，参数随便调了几下，因为没有做的那么细致的原因，所以我干脆让模型过拟合以实现贴合曹操人设 
