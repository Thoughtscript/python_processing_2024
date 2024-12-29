# python_processing_2024

[![](https://img.shields.io/badge/Python-3.12.3-yellow.svg)](https://www.python.org/downloads/) [![](https://img.shields.io/badge/Docker-blue.svg)](https://www.docker.com/) 

Quick and brief review of some important Python Concurrency, Fork, and Threading concepts.

## Use

```bash
docker-compose up

# If using Docker Compose Engine V2:
docker compose up
```

> The container will exit after it's done running.

```bash
python-1  | I'm in BASH fork: BBBB
python-1  | BBBB.p_one.t_one thread local data: -783
python-1  | ================= BEGIN bashfork: BBBB pid: p_one tid: t_one example() =================
python-1  | 0 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 1 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 2 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 3 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 4 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 5 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 6 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 7 in bashfork: BBBB pid: p_one tid: t_one
python-1  | 8 in bashfork: BBBB pid: p_one tid: t_one
python-1  | ================= END bashfork: BBBB pid: p_one tid: t_one example() =================
python-1  | BBBB.p_one.t_two thread local data: -730
python-1  | ================= BEGIN bashfork: BBBB pid: p_one tid: t_two example() =================
python-1  | 0 in bashfork: BBBB pid: p_one tid: t_two
python-1  | 1 in bashfork: BBBB pid: p_one tid: t_two
python-1  | ================= END bashfork: BBBB pid: p_one tid: t_two example() =================
python-1  | I'm in BASH fork: AAAA
python-1  | BBBB.p_two.t_one thread local data: -127
python-1  | ================= BEGIN bashfork: BBBB pid: p_two tid: t_one example() =================
python-1  | 0 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 1 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 2 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 3 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 4 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 5 in bashfork: BBBB pid: p_two tid: t_one
python-1  | 6 in bashfork: BBBB pid: p_two tid: t_one
python-1  | ================= END bashfork: BBBB pid: p_two tid: t_one example() =================
python-1  | BBBB.p_two.t_two thread local data: -250
python-1  | ================= BEGIN bashfork: BBBB pid: p_two tid: t_two example() =================
python-1  | 0 in bashfork: BBBB pid: p_two tid: t_two
python-1  | 1 in bashfork: BBBB pid: p_two tid: t_two
python-1  | 2 in bashfork: BBBB pid: p_two tid: t_two
python-1  | 3 in bashfork: BBBB pid: p_two tid: t_two
python-1  | ================= END bashfork: BBBB pid: p_two tid: t_two example() =================
python-1  | AAAA.p_one.t_one thread local data: -102
python-1  | ================= BEGIN bashfork: AAAA pid: p_one tid: t_one example() =================
python-1  | 0 in bashfork: AAAA pid: p_one tid: t_one
python-1  | 1 in bashfork: AAAA pid: p_one tid: t_one
python-1  | 2 in bashfork: AAAA pid: p_one tid: t_one
python-1  | 3 in bashfork: AAAA pid: p_one tid: t_one
python-1  | 4 in bashfork: AAAA pid: p_one tid: t_one
python-1  | 5 in bashfork: AAAA pid: p_one tid: t_one
python-1  | ================= END bashfork: AAAA pid: p_one tid: t_one example() =================
python-1  | AAAA.p_one.t_two thread local data: -954
python-1  | ================= BEGIN bashfork: AAAA pid: p_one tid: t_two example() =================
python-1  | 0 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 1 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 2 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 3 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 4 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 5 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 6 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 7 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 8 in bashfork: AAAA pid: p_one tid: t_two
python-1  | 9 in bashfork: AAAA pid: p_one tid: t_two
python-1  | ================= END bashfork: AAAA pid: p_one tid: t_two example() =================
python-1  | AAAA.p_two.t_one thread local data: -539
python-1  | ================= BEGIN bashfork: AAAA pid: p_two tid: t_one example() =================
python-1  | 0 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 1 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 2 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 3 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 4 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 5 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 6 in bashfork: AAAA pid: p_two tid: t_one
python-1  | 7 in bashfork: AAAA pid: p_two tid: t_one
python-1  | ================= END bashfork: AAAA pid: p_two tid: t_one example() =================
python-1  | AAAA.p_two.t_two thread local data: -164
python-1  | ================= BEGIN bashfork: AAAA pid: p_two tid: t_two example() =================
python-1  | 0 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 1 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 2 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 3 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 4 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 5 in bashfork: AAAA pid: p_two tid: t_two
python-1  | 6 in bashfork: AAAA pid: p_two tid: t_two
python-1  | ================= END bashfork: AAAA pid: p_two tid: t_two example() =================
python-1  | ================= BEGIN multiprocessing.Pool example() =================
python-1  | 0
python-1  | 1
python-1  | 2
python-1  | 3
python-1  | 4
python-1  | 5
python-1  | 6
python-1  | 7
python-1  | 8
python-1  | 9
python-1  | ================= END multiprocessing.Pool example() =================
python-1  | ================= BEGIN multiprocessing.Pool example() =================
python-1  | 0
python-1  | 1
python-1  | 2
python-1  | 3
python-1  | 4
python-1  | 5
python-1  | 6
python-1  | 7
python-1  | 8
python-1  | 9
python-1  | 10
python-1  | 11
python-1  | 12
python-1  | 13
python-1  | 14
python-1  | 15
python-1  | 16
python-1  | 17
python-1  | 18
python-1  | 19
python-1  | ================= END multiprocessing.Pool example() =================
python-1  | ================= BEGIN multiprocessing.Pool example() =================
python-1  | 0
python-1  | 1
python-1  | 2
python-1  | 3
python-1  | 4
python-1  | 5
python-1  | 6
python-1  | 7
python-1  | 8
python-1  | 9
python-1  | 10
python-1  | 11
python-1  | 12
python-1  | 13
python-1  | 14
python-1  | 15
python-1  | 16
python-1  | 17
python-1  | 18
python-1  | 19
python-1  | 20
python-1  | 21
python-1  | 22
python-1  | 23
python-1  | 24
python-1  | 25
python-1  | 26
python-1  | 27
python-1  | 28
python-1  | 29
python-1  | ================= END multiprocessing.Pool example() =================
python-1  | ================= BEGIN multiprocessing.Pool example() =================
python-1  | 0
python-1  | 1
python-1  | 2
python-1  | 3
python-1  | 4
python-1  | 5
python-1  | 6
python-1  | 7
python-1  | 8
python-1  | 9
python-1  | ================= END multiprocessing.Pool example() =================
python-1  | ================= BEGIN multiprocessing.Pool example() =================
python-1  | 0
python-1  | 1
python-1  | 2
python-1  | 3
python-1  | 4
python-1  | 5
python-1  | 6
python-1  | 7
python-1  | 8
python-1  | 9
python-1  | 10
python-1  | 11
python-1  | 12
python-1  | 13
python-1  | 14
python-1  | 15
python-1  | 16
python-1  | 17
python-1  | 18
python-1  | 19
python-1  | 20
python-1  | 21
python-1  | 22
python-1  | 23
python-1  | 24
python-1  | ================= END multiprocessing.Pool example() =================
python-1  | async_call_back!
python-1  | async_call_back!
python-1 exited with code 0
```

## Resources and Links

1. https://docs.python.org/3/library/multiprocessing.html
2. https://docs.python.org/3/library/threading.html
3. https://docs.python.org/3/library/argparse.html
4. https://www.geeksforgeeks.org/with-statement-in-python/
