# Speaker Similarity App

## Prerequisites
- Python 3.12.4

## Start the app
```bash
streamlit run app.py
```

## Start the API
```bash
uvicorn api:app --host 0.0.0.0 --port 8000
```

## Start the API with Docker Compose
```bash
APP_MODE=api docker compose up --build
```

## Compare speakers via API
```bash
curl -X POST http://localhost:8000/speaker/compare \
  -F "file1=@speaker_a.wav" \
  -F "file2=@speaker_b.wav" \
  -F "methods=ecapa2"
```

The API returns normalized similarity scores from `0.0` to `1.0`.

Example response:
```json
{
  "similarity_score": 0.873,
  "scores": {
    "SECS (ecapa2)": 0.873
  },
  "range": {
    "min": 0.0,
    "max": 1.0
  }
}
```

## Acknowledgements
This repository is based on the [tts-asr-eval-suite](https://github.com/naba89/tts-asr-eval-suite/tree/main) repository.

## Update Notes June 2026 2.0

- Added `Dockerfile` to build the app into a docker image.

  To build: `docker build -t ss-app .`

  To run: `docker run -d --name app_run --gpus all -p 8501:8501 ss-app:latest`

- Separated methods to load large models in `load_models.py` (~2 minutes before app is booted)

  Add `HF_TOKEN` environment variable for faster loading
