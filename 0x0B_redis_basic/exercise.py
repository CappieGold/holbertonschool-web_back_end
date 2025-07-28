#!/usr/bin/env python3
"""Redis basic exercise: Cache class."""

from typing import Union, Optional, Callable, TypeVar, overload, Any
from functools import wraps
import uuid
import redis
from redis import Redis

Data = Union[str, bytes, int, float]
T = TypeVar("T")


def count_calls(method: Callable[..., Any]) -> Callable[..., Any]:
    """Décorateur qui compte combien de fois `method` est appelée.

    La clé utilisée dans Redis est le `__qualname__` de la méthode.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable[..., Any]) -> Callable[..., Any]:
    """Décorateur qui enregistre l'historique des entrées/sorties.

    - Stocke les arguments passés dans la liste `<qualname>:inputs`
    - Stocke la valeur de retour dans la liste `<qualname>:outputs`
    """
    inputs_key = f"{method.__qualname__}:inputs"
    outputs_key = f"{method.__qualname__}:outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


class Cache:
    """Petit wrapper de cache autour de redis-py."""

    def __init__(self) -> None:
        """Instancie le client Redis et vide la base."""
        self._redis: Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Data) -> str:
        """Stocke `data` sous une clé aléatoire et retourne la clé.

        Args:
            data: valeur à stocker (str, bytes, int ou float).

        Returns:
            str: la clé générée.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    @overload
    def get(self, key: str) -> Optional[bytes]: ...
    @overload
    def get(self, key: str, fn: Callable[[bytes], T]) -> Optional[T]: ...

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None):
        """Récupère la valeur associée à `key`.

        - Comportement de `Redis.get`: `None` si la clé n'existe pas,
          sinon `bytes`.
        - Si `fn` est fourni, applique la fonction de conversion sur les bytes.
        """
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Récupère la valeur et la convertit en str (UTF-8)."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Récupère la valeur et la convertit en int."""
        return self.get(key, fn=int)
