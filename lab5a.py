#!/usr/bin/env python3
# Author: Ajay Saini
# Student ID: asaini85 (152730222)

def read_file_string(file_name):
    """Reads entire file content as a string."""
    with open(file_name, 'r') as f:
        return f.read()

def read_file_list(file_name):
    """Reads file content as a list of lines, stripping new-line characters."""
    with open(file_name, 'r') as f:
        return [line.strip() for line in f.readlines()]

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))
