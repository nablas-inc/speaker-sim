import shutil
import tempfile
from pathlib import Path
from typing import Annotated, List

from fastapi import FastAPI, File, Form, HTTPException, UploadFile


app = FastAPI(title="Speaker Similarity API")


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/speaker/compare")
def compare_speakers(
    file1: Annotated[UploadFile, File(...)],
    file2: Annotated[UploadFile, File(...)],
    methods: Annotated[List[str] | None, Form()] = None,
) -> dict:
    try:
        suffix1 = Path(file1.filename or "").suffix
        suffix2 = Path(file2.filename or "").suffix

        with tempfile.NamedTemporaryFile(suffix=suffix1) as tmp1:
            with tempfile.NamedTemporaryFile(suffix=suffix2) as tmp2:
                shutil.copyfileobj(file1.file, tmp1)
                shutil.copyfileobj(file2.file, tmp2)
                tmp1.flush()
                tmp2.flush()

                from speaker_service import compare_audio_files

                scores = compare_audio_files(
                    tmp1.name,
                    tmp2.name,
                    methods=methods,
                    normalize=True,
                )

        return {
            "similarity_score": sum(scores.values()) / len(scores),
            "scores": scores,
            "range": {"min": 0.0, "max": 1.0},
        }
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail=f"Failed to compare speakers: {exc}") from exc
