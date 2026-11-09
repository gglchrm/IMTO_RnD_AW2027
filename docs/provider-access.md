# Доступ к провайдерам LLM

## MWS GPT

- **Владелец квоты**: Наталья Барабанова
- **Endpoint**: https://gpt.mwsapis.ru/projects/itmo-research/openai/v1
- **Формат API**: OpenAI-compatible
- **Доступные модели** (выбраны самые популярные согласно официальному отчёту компании https://mws.ru/news/potreblenie-kitajskih-llm-v-rossii-vyroslo-bolee-chem-v-11-raz/):     
                            - glm-5.3       
                            - kimi-k2.6 
                            - qwen3.6-35b-a3b
                            - gpt-oss-120b
                            - gemma-4-31b-it
- **Ограничения контекста**: все 256000 токенов
- **Скорость / rate limit**: в среднем 3 сек на запрос 
- **Квота**: -- Максимальное количество деплойментов в проекте 3 / 20 шт.
        -- Количество запросов в минуту
            - glm-5.3g10 шт.
            - kimi-k2.6q 50 шт.
            - qwen3.6-35b-a3b 10 шт.
- **Статус проверки**: 05.10.2026

## Yandex Cloud

- **Владелец квоты**: Наталья Барабанова
- **Endpoint**: https://ai.api.cloud.yandex.net/v1
- **Формат API**: OpenAI-compatible
- **Доступные модели**:     - yandexgpt-4-lite
                            - yandexgpt-5-lite
                            - yandexgpt-5-pro
                            - yandexgpt-5.1
                            - Alince AI LLM
                            - Alice AI LLM Flash
                            - DeepSeek4 Flash
                            - GPT OSS 120B
                            - GPT OSS 20B
                            - Qwen 3.6-35B
- **Ограничения контекста**: <если известны>
- **Скорость / rate limit**: <наблюдения из короткого теста>
- **Квота**: - С 11.09.2026 по 10.11.2026, грант 4000 рублей
             -  Количество запросов на векторизацию текста, в секунду	10
             -  Количество одновременных выделенных инстансов	1
             -  Количество одновременных генераций в синхронном режиме	10
             -  Количество запросов в секунду, асинхронный режим (запрос)	10
             -  Количество запросов в секунду, асинхронный режим (получение ответа)	50
             -  Количество запросов в час, асинхронный режим (запрос)	5 000
             -  Количество запросов в секунду на токенизацию	50
- **Статус проверки**: 06.10.2026 (09.10.2026 отдаёт 500)

## GigaChat

- **Владелец квоты:** Наталья Барабанова
- **Endpoint:** `https://api.giga.chat/v1/chat/completions`
- **Формат API:** OpenAI-compatible
- **Доступные модели:** 
  - GigaChat-2
  - GigaChat-2-Pro
  - GigaChat-2-Max
  - GigaChat-3-Ultra *(только физические лица в рамках freemium-режима)*  
- **Ограничения контекста:**  
  - GigaChat-2: 4096 токенов  
  - GigaChat-2-Pro: 128 000 токенов  
  - GigaChat-2-Max: 128 000 токенов  
  - GigaChat-3-Ultra: 128 000 токенов  
 *(подробнее см.: [Документация моделей GigaChat](https://developers.sber.ru/docs/ru/gigachat/models/main))*  
- **Скорость / rate limit:**  
  - ~1 секунда на запрос для всех моделей, кроме GigaChat-3-Ultra  
  - Для GigaChat-3-Ultra ≈ 3 секунды на запрос  
- **Квота:**   
  - Бесплатные токены до 23 июля 2027 г.  
  - Текущие остатки по моделям:  
    - GigaChat Ultra: 42 246 925 токенов  
    - GigaChat Max: 19 853 356 токенов  
    - GigaChat Pro: 34 585 679 токенов  
    - GigaChat Lite: 245 362 920 токенов  
- **Статус проверки:** 29.09.2026


## ITMO LAB (judjge) 

- **Владелец квоты**: Indistrial AI lab ITMO
- **Endpoint**: https://admin.duckduck.cloud/
- **Формат API**: OpenAI-compatible
- **Доступные модели**: 
                        - gpt-oss-120b
                        - qwen2.5-72b
                        - qwen2.5-vl-7b
                        - qwen3-3b
                        - qwen3-3b-reasoning-cache
- **Ограничения контекста**: ?
- **Скорость / rate limit**: около 4х секунд на запрос
- **Квота**:
            - TPM: Unlimited
            - RPM: Unlimited
            - TPD (batch): Unlimited
            - Max Parallel Requests: Unlimited
            - Model TPM Limits: Unlimited
            - Model RPM Limits: Unlimited
            - Tag RPM Limits: Unlimited
            - Estimated Output Tokens: Default
            - Estimated Output Tokens Per Model: Default
- **Статус проверки**: 29.09.2026

## Блокеры
 
- ответ 500 от яндекса