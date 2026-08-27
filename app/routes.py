from app.service import greet


def handle(name: str) -> str:
    return greet(name)
