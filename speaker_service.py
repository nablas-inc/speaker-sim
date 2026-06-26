from functools import lru_cache
from typing import Dict, Iterable, List, Tuple

import torch

from tts_asr_eval_suite.secs import SECS


AVAILABLE_METHODS = (
    "resemblyzer",
    "wavlm_large_sv",
    "wavlm_base_plus_sv",
    "ecapa2",
)

DEFAULT_METHODS = ("ecapa2",)


def get_device() -> str:
    """Get the appropriate device for model inference."""
    return "cuda" if torch.cuda.is_available() else "cpu"


def validate_methods(methods: Iterable[str] | None) -> List[str]:
    selected_methods = list(methods or DEFAULT_METHODS)

    if not selected_methods:
        selected_methods = list(DEFAULT_METHODS)

    invalid_methods = sorted(set(selected_methods) - set(AVAILABLE_METHODS))
    if invalid_methods:
        raise ValueError(f"Invalid methods: {', '.join(invalid_methods)}")

    return selected_methods


@lru_cache(maxsize=8)
def get_scorer(methods: Tuple[str, ...]) -> SECS:
    return SECS(device=get_device(), methods=list(methods))


def normalize_score(score: float) -> float:
    """Convert a cosine-like -1.0..1.0 score to a 0.0..1.0 API score."""
    return max(0.0, min(1.0, (score + 1.0) / 2.0))


def compare_audio_files(
    file1_path: str,
    file2_path: str,
    methods: Iterable[str] | None = None,
    normalize: bool = False,
) -> Dict[str, float]:
    selected_methods = validate_methods(methods)
    scorer = get_scorer(tuple(selected_methods))
    scores = scorer(file1_path, file2_path)

    if normalize:
        return {name: normalize_score(float(score)) for name, score in scores.items()}

    return {name: float(score) for name, score in scores.items()}
