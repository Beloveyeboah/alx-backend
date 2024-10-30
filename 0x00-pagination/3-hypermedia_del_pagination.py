#!/usr/bin/env python3
"""Deletion-resilient hypermedia pagination"""

import csv
import math
from typing import List, Dict, Optional, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index and an end index
    corresponding to the range of indexes to return in a list for those
    particular pagination parameters.

    :param page: The page number (1-indexed)
    :param page_size: The number of items per page
    :return: A tuple (start index, end index)
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


class Server:
    """Server class to paginate a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0"""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Return a list of rows from the dataset for
        the given page and page size.

        :param page: The page number (1-indexed)
        :param page_size: The number of items per page
        :return: A list of rows from the dataset
        """
        assert isinstance(page, int) and page > 0, (
            "page must be an integer greater than 0"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be an integer greater than 0"
        )

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        if start_index >= len(dataset):
            return []

        return dataset[start_index:end_index]

    def get_hyper_index(self, index: Optional[int] = 0,
                        page_size: int = 10) -> Dict:

        """
        Return a dictionary containing pagination information.

        :param index: The starting index of the page
        :param page_size: The number of items per page
        :return: A dictionary containing pagination information
        """
        assert isinstance(index, int) and index >= 0, (
            "index must be a non-negative integer"
        )
        assert isinstance(page_size, int) and page_size > 0, (
            "page_size must be an integer greater than 0"
        )

        indexed_data = self.indexed_dataset()
        data = []

        next_index = index
        for _ in range(page_size):
            while (next_index not in indexed_data and
                    next_index < len(indexed_data)):
                next_index += 1

            if next_index >= len(indexed_data):
                break
            data.append(indexed_data[next_index])
            next_index += 1
        return {
                'index': index,
                'data': data,
                'page_size': page_size,
                'next_index': next_index if next_index < len(indexed_data)
                else None
                }

# Example usage


if __name__ == "__main__":
    server = Server()
    print(server.get_page(1, 10))
    print(server.get_hyper_index(1, 10))
