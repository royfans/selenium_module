# -*- coding: utf-8 -*-

# import configparser
import configparser

#写入配置文件
def write_config():

    config = configparser.ConfigParser()
    config.read("../../config/data/login.ini")

    try:
        config.add_section("School")
        config.set("School","IP","10.15.40.123")
        config.set("School","Mask","255.255.255.0")
        config.set("School","Gateway","10.15.40.1")
        config.set("School","DNS","211.82.96.1")
    except configparser.DuplicateSectionError:
        print("Section 'School' already exists")
    config.write(open("../../config/data/login.ini", "w"))
"""
def read_config():
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read("../../config/data/login.ini")
    ip=config.get("School","IP")
    mask=config.get("School","mask")
    gateway=config.get("School","Gateway")
    dns=config.get("School","DNS")

    print (ip,mask+ "\n" +gateway,dns)
    print (type(ip))
"""
def read_config(path):
    # 读取配置文件
    config = configparser.ConfigParser()
    config.read(path, encoding="utf-8")

    return config



if __name__ == "__main__":
    # write_config()
    config = read_config("../../config/data/login.ini")
    user = config.get("User","username1")
    err = config.get("ErrorMsg","msg")
    print(user,err)
    