from os import getenv
from time import perf_counter, sleep
from typing import Any

from gigachat import GigaChat
from gigachat.models import Chat, Messages, MessagesRole

from .base import LLMResponse

GIGACHAT_TOKEN = getenv("GIGACHAT_API_KEY")

_client: GigaChat | None = None


def get_client() -> GigaChat:
    global _client
    if _client is None:
        _client = GigaChat(
            base_url="https://api.giga.chat/v1",
            credentials=GIGACHAT_TOKEN,
            scope="GIGACHAT_API_PERS",
            verify_ssl_certs=False,
        )
    return _client


def call_model(prompt: str, model: str, max_retries: int = 3, **kwargs: Any) -> LLMResponse:
    last_error = None

    for attempt in range(1, max_retries + 1):
        t0 = perf_counter()
        try:
            chat = Chat(
                model=model,
                messages=[Messages(role=MessagesRole.USER, content=prompt)],
            )
            response = get_client().chat(chat)
            latency_ms = (perf_counter() - t0) * 1000

            # GigaChat SDK отдаёт usage отдельным объектом; имена полей
            # могут отличаться от OpenAI — берём через getattr, чтобы не падать.
            usage = getattr(response, "usage", None)
            return LLMResponse(
                content=response.choices[0].message.content or "",
                model_id=model,
                input_tokens=getattr(usage, "input_tokens", None) if usage else None,
                output_tokens=getattr(usage, "output_tokens", None) if usage else None,
                latency_ms=latency_ms,
                status="ok",
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
