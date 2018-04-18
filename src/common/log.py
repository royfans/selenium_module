# coding=utf-8
import logging.config
import os
# Program:
#   print log

# 日志级别等级CRITICAL > ERROR > WARNING > INFO > DEBUG > NOTSET）
curr_path = os.path.dirname(os.path.abspath(__file__))

def logger():
    # 第一步，创建一个logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)  # Log等级总开关

    # 第二步，创建一个handler，用于写入日志文件
    logfile = os.path.join(curr_path,"..\..\logs\\test.log")
    print(logfile)
    fh = logging.FileHandler(logfile, mode='a')
    fh.setLevel(logging.WARNING)  # 输出到file的log等级的开关

    # 第三步，再创建一个handler，用于输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(logging.WARNING)  # 输出到console的log等级的开关

    # 第四步，定义handler的输出格式
    formatter = logging.Formatter("%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s")
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # 第五步，将logger添加到handler里面
    logger.addHandler(fh)
    logger.addHandler(ch)

    return logger


def login():
    while True:
        try:
            name = input("input user name:")
            password = int(input("Input your password:"))
            if name == "any" and password == "pwd":
                print ("login success")

        except ValueError as e:
            # logger().debug(e)
            # logger().info(e)
            logger().warning(e)
            # logger().error(e)
            # logger().critical(e)
            break

if __name__ == '__main__':
    login()