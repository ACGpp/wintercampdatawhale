from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "Llama-2-7b-hf"
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)

model.eval()


def generate_response(prompt, model, tokenizer):
    # Encode the input prompt
    inputs = tokenizer.encode(prompt, return_tensors="pt")

    # Generate the output from the model
    outputs = model.generate(
        inputs,
        max_length=150,
        num_return_sequences=1,
        no_repeat_ngram_size=2,
        temperature=0.7,
        top_p=0.95,
        top_k=50
    )

    # Decode the output and return the response
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.strip()


def chat_with_historic_person(model, tokenizer, person_name="曹操"):
    print(f"吾乃{person_name}！")  # Print the character introduction
    while True:
        user_input = input(f"{person_name}: ")  # Get input from the user

        # Exit condition
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print(f"{person_name}: 手机没电了，下播下播！")
            break

        # Generate the prompt for the model
        prompt = f"请用{person_name}的风格回答以下问题：{user_input}"

        # Generate a response using the model
        response = generate_response(prompt, model, tokenizer)

        # Print the model's response
        print(f"{person_name}: {response}")


# Run the chat function with the model and tokenizer
chat_with_historic_person(model, tokenizer, person_name="曹操")