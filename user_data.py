#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/8/19 22:19
# @Author  : Aries
# @Site    : 
# @File    : user_data.py
# @Software: PyCharm


import time
import mysqloper
def get_time_stamp():
    ct = time.time()
    local_time = time.localtime(ct)
    data_head = time.strftime("%H:%M:%S", local_time)
    data_secs = (ct - int(ct)) * 1000
    time_stamp = "%s.%03d" % (data_head, data_secs)
    return time_stamp

class user():
    def __init__(self):
        self._myconf = {
            'host': '127.0.0.1',
            'port': 3306,
            'user': 'root',
            'passwd': '123456'
        }
        pass
        self._myexec = mysqloper.MysqlExec(self._myconf)

    def getdept4A(self):
        if not self._myexec.sql_noresult("use pw_test"):
            return dict()
        values, fields=self._myexec.getTableValue('t_department4a')
        return values[0][1]
        # for value in values:

    def getUser4A(self):
        # print(get_time_stamp())

        if not self._myexec.sql_noresult("use pw_test"):
            return dict()
        values, fields=self._myexec.getTableValue('t_user4a')

        print(get_time_stamp())
        # user_data = list()
        user_data_d = dict()
        for value in values:

            user = dict()
            i = 0
            for field in fields:
                user[field[0]] = value[i]
                i += 1
            # _user = user
            if user_data_d.get(user['bizOrgId']):
                user_data_d[user['bizOrgId']].append(user)
            else:
                user_data_d[user['bizOrgId']] = [user]

        print(get_time_stamp())
        print("end")
        return user_data_d


if __name__ == '__main__':
    u = user()
    d = u.getdept4A()
    s = u'中国南方电网有限责任公司'
    print(d)

    # ddd = dict()
    # for i in range(5):
    #     if ddd.get('text'):
    #        ddd['text'].append(str(i))
    #     else:
    #         ddd['text'] = [str(i)]
    # print(ddd)