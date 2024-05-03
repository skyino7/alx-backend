#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Get hypermedia indexed data
        """
        indexed_dataset = self.indexed_dataset()
        num_records = len(indexed_dataset)
        total_pages = math.ceil(num_records / page_size)

        if index is None:
            index = 0
        else:
            assert 0 <= index < num_records

        data = []
        for i in range(index, index + page_size):
            if i in indexed_dataset:
                data.append(indexed_dataset[i])

        return {
            'index': index,
            'data': data,
            'page_size': len(data),
            'next_index': min(index + len(data), num_records)
        }

