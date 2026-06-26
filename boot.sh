python load_models.py

if [ "${APP_MODE:-streamlit}" = "api" ]; then
    uvicorn api:app --host 0.0.0.0 --port "${PORT:-8000}"
else
    streamlit run app.py
fi
