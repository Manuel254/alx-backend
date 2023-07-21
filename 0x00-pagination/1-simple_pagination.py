#!/usr/bin/env python3
import csv
import math
from typing import List
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Returns a tuple containing the start index and end index
    corresponding to the range of indexes to return in a list
    for those particular pagination parameters"""
    start = 0
    stop = 0

    for i in range(1, page + 1):
        if i == page:
            start = page_size * (i - 1)
            stop = start + page_size
    return (start, stop)


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
        """Gets the items in a page of the dataset"""
        data = self.dataset()
        num_of_pages = len(data)
        p = index_range(page, page_size)[0]
        size = index_range(page, page_size)[1]

        print(p)
        print(size)

        if type(page) and type(page_size) == int:
            assert page > 0 and page_size > 0
        else:
            assert type(page) and type(page_size) == int

        if p > num_of_pages or size > num_of_pages:
            return []
        else:
            return [record for index, record in enumerate(data)
                    if index >= p and index < size]
