from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware


def add_cors_configuration(app: FastAPI) -> None:
    """
    Adiciona um schema de configurações personalizadas para o OpenAPI

    Args:
        app: instancia do FastAPI

    Returns:
        None: Não retorna nada

    Examples:
        >>> add_cors_configuration(FastAPI())
    """
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"], 
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )