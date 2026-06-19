# Speaker Similarity App

## Prerequisites
- Python 3.12.4

## Start the app
```bash
streamlit run app.py
```

## Acknowledgements
This repository is based on the [tts-asr-eval-suite](https://github.com/naba89/tts-asr-eval-suite/tree/main) repository.

## Update Notes June 2026

- Updated `requirements.txt` for strict version control of two modules

- If system `ffmpeg` is not of version `>=4.4, <7`, use `conda install -c conda-forge 'ffmpeg<7'`, or when creating a new environment `conda create -n <env_name> -c conda-forge ffmpeg==6.1.2 python==3.12.4`. 

  For details see [torchaudio installation](https://docs.pytorch.org/audio/main/installation.html#optional-dependencies).
