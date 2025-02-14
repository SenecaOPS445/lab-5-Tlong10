#!/usr/bin/env python3
# Author ID: TLONG10

def read_file_string(file_name):
    # Takes file_name as string for a file name, returns its entire contents as a string
    file = open(file_name, 'r')
    read_data = file.read()
    file.close()
    return read_data

    
def read_file_list(file_name):
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters
    file = open(file_name, 'r')
    list = file.read().splitlines()
    return list

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))