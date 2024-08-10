#!/usr/bin/env bash
python _pool.py &
python _process.py --bid AAAA &
python _process.py --bid BBBB &
wait