from huggingface_hub import hf_hub_download

hf_hub_download(repo_id='Jenthe/ECAPA2', filename='ecapa2.pt', cache_dir=None)
hf_hub_download(repo_id="subatomicseer/wavlm-large-sv-ckpts", filename="wavlm_large.pt", cache_dir=None)
hf_hub_download(repo_id="subatomicseer/wavlm-large-sv-ckpts", filename="wavlm_large_finetune.pth", cache_dir=None)