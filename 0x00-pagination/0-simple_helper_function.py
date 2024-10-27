#!/usr/bin/env python3
"""Simple helper function"""

from typing import List


def index_range(page: int, page_size: int) -> List[int]:
    """index range function"""
    return ((page - 1) * page_size, (page - 1) * page_size + page_size)
