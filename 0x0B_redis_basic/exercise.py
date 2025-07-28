#!/usr/bin/env python3
"""Redis basic exercise: Cache class."""

from typing import Union, Optional, Callable, TypeVar, overload
import uuid
import redis
from redis import Redis

Data = Union[str, bytes, int, float]
T = TypeVar("T")


class Cache:
    """Petit wrapper de cache autour de redis-py."""

    def __init__(self) -> None:
        """Instancie le client Redis et vide la base."""
        self._redis: Redis = redis.Redis()
        self._redis.flushdb()

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

        - Conserve le comportement de `Redis.get`: retourne `None`
          si la clé n'existe pas, sinon retourne des `bytes`.
        - Si `fn` est fourni, applique cette fonction aux `bytes`
          et retourne le résultat.

        Args:
            key: clé Redis.
            fn: fonction de conversion à appliquer aux bytes.

        Returns:
            None si la clé n'existe pas,
            sinon `bytes` ou le type retourné par `fn`.
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
