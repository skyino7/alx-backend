#!/usr/bin/env python3
"""
Implement a get_hyper method that takes the same
arguments (and defaults) as get_page and returns a
dictionary containing the following key-value pairs
"""
import csv
import math
from typing import List, Dict, Union


def index_range(page, page_size):
    """
    range of indexes to return in a list for
    those particular pagination parameters.
    """
    start = (page - 1) * page_size
    end = start + page_size
    return start, end


class Server:
    """
    Server class to paginate a database of
    popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Doc"""
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Get Page"""
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        num_records = len(dataset)
        total_pages = math.ceil(num_records / page_size)

        start, end = index_range(page, page_size)

        if page > total_pages:
            return []

        return dataset[start:min(end, num_records)]

    def get_hyper(self, page: int = 1, page_size: int = 10
                  ) -> Dict[str, Union[int, List[List], None]]:
        """
        returns a dictionary containing the following key-value pairs
        """
        page_data = self.get_page(page, page_size)
        num_records = len(self.__dataset)
        total_pages = math.ceil(num_records / page_size)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": len(page_data),
            "page": page,
            "data": page_data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
