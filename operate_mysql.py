#   赵阳，2021年6月15日写
#   将生成的Mysql文件导入到数据库
import pymysql

#  ===========================副文件==============================
# 写入到mysql数据库,sql_name:sql文件名； db_name:数据库名称
def write_to_mysql(sql_name, db_name):
    try:
        db = pymysql.connect(host="localhost", user='root', password='001131', db= db_name, port=3306)
        c = db.cursor()
        with open(sql_name,encoding='utf-8',mode='r') as f:
        # 读取整个sql文件，以分号切割。[:-1]删除最后一个元素，也就是空字符串
            sql_list = f.read().split(';')[:-1]
            num_n = 1
            for x in sql_list:
                # 判断包含空行的
                if '\n' in x:
                    # 替换空行为1个空格
                    x = x.replace('\n', ' ')

                # 判断多个空格时
                if '    ' in x:
                    # 替换为空
                    x = x.replace('    ', '')

                # sql语句添加分号结尾
                sql_item = x+';'
                # print(sql_item)
                c.execute(sql_item)

                # print("执行成功sql: %s"%sql_item)
                print("第{}部分执行成功".format(num_n))
                num_n=num_n+1

    except Exception as e:
        print(e)
        print("执行失败sql: %s")
    finally:
        # 关闭mysql连接
        c.close()
        db.commit()
        db.close()
