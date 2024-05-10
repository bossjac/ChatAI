from safetensors import safe_open

tensors = {}
with safe_open("/home/omx/Downloads/model-00002-of-00004.safetensors", framework="pt", device="cpu") as f:
    for key in f.keys():
        tensors[key] = f.get_tensor(key)

# Now you can inspect the tensors loaded from the file
print(tensors)

