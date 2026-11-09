from os import getenv
from time import perf_counter, sleep
from typing import Any

from openai import OpenAI

from .base import LLMResponse

MWS_API_KEY = getenv("MWS_API_KEY")
BASE_URL = "https://gpt.mwsapis.ru/projects/itmo-research/openai/v1"

_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(
            api_key=MWS_API_KEY,
            base_url=BASE_URL,
            timeout=60.0,
            max_retries=0,  # ретраи делаем сами, чтобы логировать каждую попытку
        )
    return _client


def call_model(prompt: str, model: str, max_retries: int = 3, **kwargs: Any) -> LLMResponse:
    """MWS GPT: model — алиас из config.yaml (glm, kimi, qwen-mws)."""
    last_error = None

    for attempt in range(1, max_retries + 1):
        t0 = perf_counter()
        try:
            response = get_client().chat.completions.create(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                **kwargs,
            )
            latency_ms = (perf_counter() - t0) * 1000
            usage = response.usage
            return LLMResponse(
                content=response.choices[0].message.content or "",
                model_id=response.model or model,
                input_tokens=usage.prompt_tokens if usage else None,
                output_tokens=usage.completion_tokens if usage else None,
                latency_ms=latency_ms,
                status="ok",
                raw=response.model_dump(),
            )
        except Exception as e:
            last_error = f"{type(e).__name__}: {e}"
            if attempt < max_retries:
                sleep(2**attempt)  # 2, 4, 8 секунд

    return LLMResponse(
        content="",
        model_id=model,
        status="error",
        error=last_error,
    )


def generate(prompt: str, model: str) -> str:
    """Тонкая обёртка для ноутбуков — возвращает только текст."""
    return call_model(prompt, model).content
