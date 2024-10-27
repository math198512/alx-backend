#!/usr/bin/env python3
"""Simple pagination"""

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> List[int]:
    """index range function"""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Simple pagination function"""
        assert type(page) == int
        assert type(page_size) == int
        assert page > 0
        assert page_size > 0
        start, end = index_range(page, page_size)
        csv_size = len(self.dataset())
        end = min(end, csv_size)
        if start >= csv_size:
            return []
        return self.dataset()[start:end]
