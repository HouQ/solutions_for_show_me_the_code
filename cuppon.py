# -*- coding: utf-8 -*-
import random
import MySQLdb
import redis


def generate_cup(num):
    cups = []
    for i in xrange(num + 1):
        cup = ''
        for j in xrange(16):
            c = chr(random.randint(65, 90))
            cup += c
        cups.append(cup)
    return cups


def insert_to_mysql(cups):
    db = MySQLdb.connect(host="localhost", port=3306, user="username",
                         passwd="password", db="test")
    cursor = db.cursor()
    try:
        for cup in cups:
            sql = "INSERT INTO test.cuppons (cuppon) VALUES ('"+cup+"');"
            cursor.execute(sql)
            db.commit()
    except:
        db.rollback()
    db.close()


def insert_to_redis(cups):
    # 加上decode_responses=True，写入的键值对中的value为str类型，不加这个参数写入的则为字节类型。
    r = redis.Redis(host='localhost', port=6379, decode_responses=True)
    for i, cup in enumerate(cups):
        r.set(i, cup)


if __name__ == "__main__":
    cups = generate_cup(200)
    print cups
    insert_to_mysql(cups)
    insert_to_redis(cups)
