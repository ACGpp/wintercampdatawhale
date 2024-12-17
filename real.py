from transformers import LlamaForCausalLM,LlamaTokenizer

model_name="Llama-2-7b-hf"
tokenizer=LlamaTokenizer.from_pretrained(model_name)
model=LlamaForCausalLM.from_pretrained(model_name)

model.eval()

def generate_response(prompt,model,tokenizer):
    inputs=tokenizer.encode(prompt,return_tensors="pt")

    outputs=model.generate(inputs,max_length=150,num_return_sequences=1,no_repeat_ngram_size=2)

    response=tokenizer.decode(outputs[0],skip_special_tokens=True)
    return response.strip()
def chat_with_histtoric_person(model,tokenizer,person_name=)