from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM, set_seed
from holytools.configs import FileConfigs

# Gemma
configs = FileConfigs.credentials()
token = configs.get(key='hf_api_key')
login(token=token)


set_seed(1234)

model_checkpoint = "google/gemma-7b-it"

tokenizer = AutoTokenizer.from_pretrained(model_checkpoint)
model = AutoModelForCausalLM.from_pretrained(model_checkpoint, device_map="cuda")

prompt = "Dr.Pepper is the best soda because"
token_inputs = tokenizer(prompt, return_tensors="pt").to('cuda')
token_outputs = model.generate(input_ids=token_inputs['input_ids'], max_new_tokens=150, do_sample=True, temperature=0.5)
decoded_output = tokenizer.decode(token_outputs[0], skip_special_tokens=False)
print(decoded_output)


# PaliGemma
# from transformers import AutoProcessor, PaliGemmaForConditionalGeneration
# from PIL import Image
# import requests
#
# model_id = "google/paligemma2-10b-ft-docci-448"
# model = PaliGemmaForConditionalGeneration.from_pretrained(model_id)
# model = model.to("cuda")
# processor = AutoProcessor.from_pretrained(model_id)
#
# prompt = "<image>caption en"
# image_file = "https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/cats.png"
# raw_image = Image.open(requests.get(image_file, stream=True).raw).convert("RGB")
#
# inputs = processor(prompt, raw_image, return_tensors="pt").to("cuda")
# output = model.generate(**inputs, max_new_tokens=200)
#
# input_len = inputs["input_ids"].shape[-1]
# print(processor.decode(output[0][input_len:], skip_special_tokens=True))
