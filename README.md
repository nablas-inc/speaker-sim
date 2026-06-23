# Speaker Similarity App

## Prerequisites
- Python 3.12.4

## Start the app
```bash
streamlit run app.py
```

## Acknowledgements
This repository is based on the [tts-asr-eval-suite](https://github.com/naba89/tts-asr-eval-suite/tree/main) repository.

## Update Notes June 2026 2.0

- Added `Dockerfile` to build the app into a docker image.

  To build: `docker build -t ss-app .`

  To run: `docker run -d --name app_run --gpus all -p 8501:8501 ss-app:latest`

- Separated methods to load large models in `load_models.py` (~2 minutes before app is booted)

  Add `HF_TOKEN` environment variable for faster loading
