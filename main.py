from datetime import datetime, timezone

from fastapi import FastAPI

app = FastAPI(title="Server Time API", version="1.0.0")


@app.get("/")
def root() -> dict[str, str]:
    return {"status": "ok", "docs": "/docs", "time": "/time"}


@app.get("/time")
def get_server_time() -> dict[str, str | float]:
    now_utc = datetime.now(timezone.utc)
    now_local = datetime.now().astimezone()
    return {
        "utc": now_utc.isoformat(),
        "local": now_local.isoformat(),
        "timezone": str(now_local.tzinfo),
        "unix_timestamp": now_utc.timestamp(),
    }


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "healthy"}
