#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Init"""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = \
                {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """Fetch a page of data considering index gaps due to deletion."""
        assert index >= 0 and index < len(self.__indexed_dataset), \
            "Index out of valid range"
        dataset = self.__indexed_dataset
        items = list(dataset.items())
        start_index = index
        end_index = start_index + page_size
        result_data = []

        current_index = start_index
        while current_index < end_index and current_index < len(items):
            if items[current_index][0] >= start_index:
                result_data.append(items[current_index][1])
            current_index += 1

        next_index = current_index if current_index < len(items) else None

        return {
            "index": start_index,
            "next_index": next_index,
            "page_size": len(result_data),
            "data": result_data
        }
