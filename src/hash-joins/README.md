## Understanding Hash Joins in MySQL

[Original article](https://www.percona.com/blog/2019/10/30/understanding-hash-joins-in-mysql-8/)

Docs
- https://dev.mysql.com/worklog/task/?id=2241
- https://dev.mysql.com/doc/refman/8.0/en/nested-loop-joins.html#block-nested-loop-join-algorithm

## Running

- Run everything from `./init.sql` inside mysql container
- Generate random data, run following from root folder

```bash
    make shell
    python ./src/hash-joins/insert_random_data.py
```
