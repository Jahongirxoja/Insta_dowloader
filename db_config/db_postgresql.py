from typing import Union

import asyncpg
from asyncpg import Connection
from asyncpg.pool import Pool
from data.config import *


class DataBase:
    def __init__(self):
        self.pool = Union[Pool, None]

    async def conf(self):
        self.pool = await asyncpg.create_pool(
            user=DB_USER,
            password=DB_PASS,
            host=DB_HOST,
            database=DB_NAME
        )

    async def execute(self, sql, *args,
                      fetch: bool = False,
                      fetchval: bool = False,
                      fetchrow: bool = False,
                      execute: bool = False):

        async with self.pool.acquire() as connection:
            connection: Connection
            async with connection.transaction():
                if fetch:
                    result = await connection.fetch(sql, *args)
                elif fetchval:
                    result = await connection.fetchval(sql, *args)
                elif fetchrow:
                    result = await connection.fetchrow(sql, *args)
                elif execute:
                    result = await connection.execute(sql, *args)
            return result

    async def create_table_users(self):
        sql = """
                CREATE TABLE IF NOT EXISTS Users(
                    id BIGINT NOT NULL UNIQUE,
                    full_name VARCHAR(130),
                    phone_number BIGINT
                )
"""
        await self.execute(sql, execute=True)

    async def create_user(self, chat_id, full_name):
        sql = """
                INSERT INTO Users (id, full_name)
                VALUES ($1,$2)
                ON CONFLICT (id) DO NOTHING;
"""
        await self.execute(sql, chat_id, full_name, execute=True)
