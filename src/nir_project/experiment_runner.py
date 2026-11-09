# src/nir_project/experiment_runner.py
from typing import Any

import mlflow

from nir_project import gigachat_client, mws_client, yandex_client
from nir_project.base import LLMClient, LLMResponse

CLIENTS: dict[str, LLMClient] = {
    "gigachat": gigachat_client,
    "yandex": yandex_client,
    "mws": mws_client,
}


def run_one(
    provider: str,
    prompt: str,
    model: str,
    **kwargs: Any,
) -> LLMResponse:
    if provider not in CLIENTS:
        raise ValueError(f"Unknown provider: {provider}. Known: {list(CLIENTS)}")

    client = CLIENTS[provider]
    resp = client.call_model(prompt, model, **kwargs)

    mlflow.log_metrics(
        {
            "latency_ms": resp.latency_ms or 0.0,
            "input_tokens": resp.input_tokens or 0,
            "output_tokens": resp.output_tokens or 0,
        }
    )
    mlflow.log_param("status", resp.status)
    if resp.error:
        mlflow.set_tag("error", resp.error[:250])

    return resp
