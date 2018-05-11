#!/usr/bin/env python
# coding=utf-8

import logging

def main():
    # logging.basicConfig(filename='myapp.log', level=logging.INFO)
    logging.basicConfig(level=logging.INFO)

    logging.info('Started')
    logging.info('Finished')

if __name__ == '__main__':
    main()