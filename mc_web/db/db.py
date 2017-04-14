# -.- coding:utf-8 -.-
import logging

from config import *
from model.model_db import AccountModel
from pymongo import MongoClient


class DbMongo:
    def __init__(self):
        try:
            self.client = MongoClient(DB_IP["ip"], DB_IP["port"])
            self.db = self.client[DB_NAME]
        except Exception as e:
            logging.error("Fail to connect db" + str(e))

    def connect_db(self):
        # try:
        #     self.db.auth(DB_ACCOUNT["user"], DB_ACCOUNT["password"], mechanism='SCRAM-SHA-1')
        # except Exception as e:
        #     logging.error("auth db fail" + str(e))
        return

    def close_db(self):
        """
        Dong db moi khi su dung xong
        :return:
        """
        if self.client is not None:
            self.client.close()

    def init_db(self):
        """
        Đánh index cho collection
        :return:
        """
        self.connect_db()
        account = self.db[AccountModel.COLLECTION_NAME]
        account.create_index(AccountModel.PARENT + "." + AccountModel.EMAIL,
                             unique=True)
        self.close_db()


class Version:
    """
        VersionUtils của tất cả các bảng được lưu theo format
        version_code.version1.version2
        version_code không có ý nghĩa gì.
        <p>
        example:
        1.01.5.100
        <p>
        Nếu version2 > 65000 thì tăng version1 lên 1
        </p>
    """

    def __init__(self, version):
        version_array = version.split(".")
        self.version_code = version_array[0] + "." + version_array[1]
        self.version_one = version_array[2]
        self.version_two = version_array[3]
        pass

    def compare(self, b):
        """
        So sánh 2 version
        :param a:
        :param b:
        :return: int
        0 nếu bằng nhau
        1 nếu a > b
        -1 nếu a < b
        """
        if self.version_one < b.version_one:
            return -1
        elif self.version_one > b.version_one:
            return 1
        elif self.version_one == b.version_one:
            if self.version_two < b.version_two:
                return -1
            elif self.version_two > b.version_two:
                return 1
            elif self.version_two == b.version_two:
                return 0

    def increase(self):
        if self.version_two < 65000:
            self.version_two += 1
        else:
            self.version_one += 1
            self.version_two = 1

    def to_string(self):
        return self.version_code + "." + self.version_one + "." + self.version_two