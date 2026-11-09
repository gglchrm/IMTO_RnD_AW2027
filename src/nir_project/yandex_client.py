from os import getenv
from time import perf_counter, sleep
from typing import Any

from openai import OpenAI

from .base import LLMResponse

YANDEX_API_KEY = getenv("YANDEX_API_KEY")
YANDEX_FOLDER_ID = getenv("YANDEX_FOLDER_ID")
BASE_URL = "https://ai.api.cloud.yandex.net/v1"

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(
            api_key=YANDEX_API_KEY,
            base_url=BASE_URL,
            project=YANDEX_FOLDER_ID,  # именно сюда идёт folder_id
            timeout=60.0,
            max_retries=0,
        )
    return _client


def _model_uri(model: str) -> str:
    """Yandex ожидает gpt://<folder_id>/<model>."""
    if model.startswith("gpt://"):
        return model
    return f"gpt://{YANDEX_FOLDER_ID}/{model}"


def call_model(prompt: str, model: str, max_retries: int = 3, **kwargs: Any) -> LLMResponse:
    last_error = None
    model_uri = _model_uri(model)

    for attempt in range(1, max_retries + 1):
        t0 = perf_counter()
        try:
            response = get_client().chat.completions.create(
                model=model_uri,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
            latency_ms = (perf_counter() - t0) * 1000
            usage = response.usage
            return LLMResponse(
                content=response.choices[0].message.content or "",
                model_id=model,
                input_tokens=usage.prompt_tokens if usage else None,
                output_tokens=usage.completion_tokens if usage else None,
                latency_ms=latency_ms,
                status="ok",
                raw=response.model_dump(),
            )
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"
            if attempt < max_retries:
                sleep(2**attempt)

    return LLMResponse(
        content="",
        model_id=model,
        status="error",
        error=last_error,
    )


def generate(prompt: str, model: str) -> str:
    return call_model(prompt, model).content
