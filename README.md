# Server Time API

Простой тестовый бэкенд на FastAPI. Возвращает текущие время и дату сервера.

## Требования

- Python 3.10+

## Установка

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

На Linux / macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Запуск

```powershell
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Сервер будет доступен по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Эндпоинты

| Метод | Путь | Описание |
| --- | --- | --- |
| `GET` | `/` | Статус сервиса и ссылки |
| `GET` | `/time` | Текущее время сервера |
| `GET` | `/date` | Текущая дата сервера |
| `GET` | `/health` | Проверка работоспособности |
| `GET` | `/docs` | Интерактивная документация Swagger |

### Пример ответа `/time`

```json
{
  "utc": "2026-08-26T21:37:57.564645+00:00",
  "local": "2026-08-27T00:37:57.564654+03:00",
  "timezone": "Turkey Standard Time",
  "unix_timestamp": 1787780277.564645
}
```

### Пример ответа `/date`

```json
{
  "utc": "2026-08-26",
  "local": "2026-08-27",
  "timezone": "Turkey Standard Time",
  "weekday": "Thursday"
}
```

## CI/CD (GitHub Actions)

При пуше в `main` workflow `.github/workflows/deploy.yml` делает две джобы:

1. Собирает Docker-образ и публикует его в GitHub Container Registry (`ghcr.io`).
2. По SSH заходит на сервер, скачивает образ из реестра и запускает контейнер.

### Секреты репозитория

Settings → Secrets and variables → Actions:

| Секрет | Назначение |
| --- | --- |
| `SSH_HOST` | IP или домен сервера |
| `SSH_USER` | Пользователь SSH |
| `SSH_PRIVATE_KEY` | Приватный ключ для входа |
| `SSH_PORT` | Порт SSH (обычно `22`) |
| `GHCR_TOKEN` | PAT с правом `read:packages` для `docker pull` на сервере |

На сервере должны быть установлены Docker. Образ публикуется как `ghcr.io/<owner>/<repo>:<sha>` и `:latest`, контейнер слушает порт `8000`.

