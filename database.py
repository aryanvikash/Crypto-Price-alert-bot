import motor.motor_asyncio

import config


class Database:
    def __init__(self,db="bot",col="alerts"):
        self._client = motor.motor_asyncio.AsyncIOMotorClient(config.MONGODBURL)
        self._db = self._client[db]
        self._collection = self._db[col]

    async def insert(self, document: dict):
        return await self._collection.insert_one(document)

    async def find_one(self, search_data):
        return await self._collection.find_one(search_data)

    async def find(self, search_data: dict = {}):
        cursor = self._collection.find(search_data)
        return await cursor.to_list(length=100)

    async def update(self, old_data: dict, new_data: dict):
        return await self._collection.update_one(old_data, {'$set': new_data})

    async def delete_many(self, many_delete_data):
        return await self._collection.delete_many(many_delete_data)

    async def delete_one(self, id):
        return await self._collection.delete_one({"_id": id})


    async def count(self):
        return await self._collection.count_documents({})


if __name__ == "__main__":
    db = Database()
    import asyncio
    async def main():
        print(await db.find({}))
    asyncio.get_event_loop().run_until_complete(main())