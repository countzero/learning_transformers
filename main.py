import torch
import transformers

model_directory = ".\\models\\falcon-7b-instruct"

tokenizer = transformers.AutoTokenizer.from_pretrained(model_directory)

pipeline = transformers.pipeline(
    "text-generation",
    model=model_directory,
    tokenizer=tokenizer,
    torch_dtype=torch.bfloat16,
    trust_remote_code=True,
    device_map="auto",
)

prompt = """Write a response that appropriately completes the following request.

Request: Tell me everything you know about falcons.

Response:"""

sequences = pipeline(
    prompt,
    max_length=200,
    do_sample=True,
    top_k=10,
    num_return_sequences=1,
    eos_token_id=tokenizer.eos_token_id,
)

for sequence in sequences:
    print(f"{sequence['generated_text']}")
