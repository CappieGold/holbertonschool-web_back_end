#!/usr/bin/env python3
"""Redis basic exercise: Cache class."""

from typing import Union
import uuid
import redis
from redis import Redis

# Type accepté pour data
Data = Union[str, bytes, int, float]


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
