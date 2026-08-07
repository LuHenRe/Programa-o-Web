from fastapi import FastAPI

def create_app() -> FastAPI:
    aplicattion = FastAPI(
        title="Aula ackend",
        description="FastApi",
        version="0.0.1"
    )
    @aplicattion.get("/")
    async def get():
        return {"olá": "ok"}

    return aplicattion

app = create_app()
