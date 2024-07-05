
import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
from os import putenv
putenv("HSA_OVERRIDE_GFX_VERSION", "10.3.0")
putenv("PYTORCH_ROCM_ARCH", "gfx1031")
# pip install accelerate

tokenizer = AutoTokenizer.from_pretrained("google/gemma-2-9b")
model = AutoModelForCausalLM.from_pretrained(
    "google/gemma-2-9b",
    device_map="auto",
    torch_dtype=torch.bfloat16
)

input_text = "Write me a poem about Machine Learning."
input_ids = tokenizer(input_text, return_tensors="pt").to("cuda")

outputs = model.generate(**input_ids)
print(tokenizer.decode(outputs[0]))
