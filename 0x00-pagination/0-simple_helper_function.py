#!/usr/bin/env python3
"""0-simple_helper_function.py"""


def index_range(page, page_size):
    """index_range function"""
    return ((page * page_size) - page_size, page * page_size)
