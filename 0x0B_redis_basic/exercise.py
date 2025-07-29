#!/usr/bin/env python3
"""Redis basic exercise: Cache class."""

import uuid
import redis
from functools import wraps
from typing import Callable, Optional, Union, TypeVar, overload
from redis import Redis

Data = Union[str, bytes, int, float]
T = TypeVar("T")


def count_calls(method: Callable) -> Callable:
    """Décorateur qui compte le nombre d'appels d'une méthode.

    Clé utilisée : `method.__qualname__`.
    """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwds):
        self._redis.incr(key)
        return method(self, *args, **kwds)

    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Décorateur qui enregistre l'historique des entrées/sorties d'une méthode.

    Listes dans Redis :
      - <qualname>:inputs
      - <qualname>:outputs
    """
    base = method.__qualname__
    inputs_key = f"{base}:inputs"
    outputs_key = f"{base}:outputs"

    @wraps(method)
    def wrapper(self, *args):
        self._redis.rpush(inputs_key, str(args))
        result = method(self, *args)
        self._redis.rpush(outputs_key, str(result))
        return result

    return wrapper


def replay(method: Callable) -> None:
    """Affiche l'historique des appels d'une méthode décorée."""
    base = method.__qualname__
    r: Redis = method.__self__._redis

    raw_count = r.get(base)
    count = int(raw_count) if raw_count is not None else 0
    print(f"{base} was called {count} times:")

    inputs = r.lrange(f"{base}:inputs", 0, -1)
    outputs = r.lrange(f"{base}:outputs", 0, -1)

    for inp, out in zip(inputs, outputs):
        in_str = inp.decode("utf-8")
        out_str = out.decode("utf-8")
        print(f"{base}(*{in_str}) -> {out_str}")


class Cache:
    """Petit wrapper de cache autour de redis-py."""

    def __init__(self) -> None:
        """Instancie le client Redis et vide la base."""
        self._redis: Redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stocke `data` sous une clé aléatoire et retourne la clé."""
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    # Overloads pour une meilleure précision de type
    @overload
    def get(self, key: str) -> Optional[bytes]: ...
    @overload
    def get(self, key: str, fn: Callable[[bytes], T]) -> Optional[T]: ...

    def get(self, key: str, fn: Optional[Callable[[bytes], T]] = None):
        """Récupère la valeur associée à `key` (None si absent)."""
        data = self._redis.get(key)
        if data is None:
            return None
        return fn(data) if fn else data

    def get_str(self, key: str) -> Optional[str]:
        """Récupère la valeur et la convertit en str (UTF‑8)."""
        return self.get(key, fn=lambda d: d.decode("utf-8"))

    def get_int(self, key: str) -> Optional[int]:
        """Récupère la valeur et la convertit en int."""
        return self.get(key, fn=int)
