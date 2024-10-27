#!/usr/bin/env python3

"""
Implement a method named get_page that
"""

import csv
import math
from typing import List
index_range = __import__('0-simple_helper_function').index_range


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a list of rows from the dataset
        for the given page and page size.
        :param page: The page number (1-indexed)
        :param page_size: The number of items per page
        :return: A list of rows from the dataset
        """
        assert isinstance(page, int) and page > 0, "page must"
        assert isinstance(page_size, int) and page_size > 0, "page must"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]
