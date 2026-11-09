# src/nir_project/base.py
from dataclasses import dataclass
from typing import Any, Protocol


@dataclass
class LLMResponse:
    content: str
    model_id: str
    input_tokens: int | None = None
    output_tokens: int | None = None
    latency_ms: float | None = None
    status: str = "ok"  # ok | error | empty | unavailable
    error: str | None = None
    raw: dict[str, Any] | None = None


class LLMClient(Protocol):
    """Контракт клиента LLM: любой модуль с такой функцией подходит."""

    def call_model(
        self,
        prompt: str,
        model: str,
        max_retries: int = ...,
        **kwargs: Any,
    ) -> LLMResponse: ...
