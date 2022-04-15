#   赵阳，2021年6月份写
#   给单个设备建表，并写入0，1随机数
#  ===========================副文件==============================
from random import random
import xlrd,random,time,datetime
# from xlrd import sheet


# *********标点符号问题，引号用 `， 不要用’或者'********

Rfile = '中创熔铸小数据库901.xls'
Wfile = '设备表908含01.sql'
R1 = xlrd.open_workbook(filename=Rfile)  # 打开文件
W1 = open(Wfile, 'w', encoding="utf8")

def data_deal(sheet_name, SQL_table_name):
        Sheet1 = R1.sheet_by_name(sheet_name)  # 通过名字检索
        nrows = Sheet1.nrows  # 获得表格行数
        # 数据类型字典
        DataStyle = {
            'float': 'float(10,1)', 'FLOAT ': 'float(10,1)',
            'bool': 'tinyint(1)', 'Bool': 'tinyint(1)', 'BOOL': 'tinyint(1)',
            'int': 'int', 'Int': 'int', 'INT': 'int',
            'Uint': 'bigint', 'UInt': 'bigint',
            'Real': 'double', 'REAL': 'double',
            'Byte': 'bigint',
            'DIN': 'double', 'DINT': 'bigint', 'DInt': 'bigint',
            'USInt': 'bigint',
            'SInt': 'bigint',
            'UDInt': 'bigint',
            'datatime': 'timestamp(6)', 'Time': 'timestamp(6)', 'DataTime': 'timestamp(6)', 'DateTime': 'timestamp(6)',
            'DTL' : 'timestamp(6)',
            'Timer': 'timestamp(6)',
            'STRING': 'varchar(100)', 'String': 'varchar(100)',
            'varchar': 'varchar(100)',
            'Word': 'varchar(200)',
            # 均热炉特殊
            'AValve V 0.0.6': 'double',
            'Adjust V 0.0.4': 'float(10,1)',
            'Adjust V 0.0.5': 'float(10,1)',
            'BurnerStatus V 0.0.4': 'double',
            'Cylinder V 0.0.5': 'double',
            'Cylinder V 0.0.4': 'double',
            'FreFan V 0.0.4': 'double',
            'FreFan V 0.0.5': 'double',
            'NormalFan V 0.0.4': 'float(10,1)',
            'NormalFan V 0.0.5': 'float(10,1)',
            'RecipType V 0.0.7': 'text',
            'RecipType V 0.0.6': 'text',
            'RecipEditType V 0.0.2': 'text',
            'Valve V 0.0.4': 'text',
            'LeakCheck V 0.0.6': 'text',
            'LeakCheck V 0.0.4': 'text',
            'WString': 'text',
            'HeaterType V 0.0.2': 'text',
            'HeaterType V 0.0.2': 'text',
            '水阀_1 V 0.0.2': 'text',
            'HeaterCommType V 0.0.1': 'text',
            'F6_ProcessStop_year': 'text',
            # 冷却炉
            'Array [0..59] of Word': 'text',
        }

        # 获得当前时间
        def now_time():
            now = int(round(time.time() * 1000))  # 读取当下时间
            timetamp = datetime.datetime.fromtimestamp(now / (1000))
            datetimeValue = timetamp.strftime("%Y-%m-%d %H:%M:%S.%f")  # 时间格式转换,精确到毫秒
            return datetimeValue  # 上传时间戳


        W1.write("DROP TABLE IF EXISTS `{}`;\n".format(SQL_table_name))
        W1.write("CREATE TABLE `{}` (\n".format(SQL_table_name))
        W1.write("  `Upload_timestamp` timestamp(6) NOT NULL COMMENT '上传时间戳',\n")
        W1.write("  `id` int DEFAULT NULL,\n")


        for i in range(nrows-1):
            i = i+1
            W1.write('  ')  # 函数内首行空格
            # 为了获得变量数据类型
            var = Sheet1.cell(i, 5).value
            varstyle = DataStyle.get(var)

            W1.write("`{}` {} DEFAULT NULL COMMENT '{}',".format(Sheet1.cell(i, 6).value, varstyle, Sheet1.cell(i, 7).value))
            W1.write('\n')  # 换行
        W1.write("  `Tasknum` varchar(150) NOT NULL COMMENT '任务号',\n")
        W1.write("  PRIMARY KEY (`Upload_timestamp`) USING BTREE\n")
        W1.write(") ENGINE=InnoDB DEFAULT CHARSET=utf8 ROW_FORMAT=DYNAMIC;\n\n")

        # ==============================写如0-1数据========================================
        # W1.write("INSERT INTO {} VALUES\n".format(SQL_table_name))
        # for x in range(39):
        #     Upload_timestamp = now_time()  # 上传时间戳
        #     W1.write("      ('{}', ".format(Upload_timestamp))
        # # 输入id
        #     W1.write("{}, ".format(x))
        #     for i in range(nrows-1):  
        #         num = int(random.choice([0,1]))
        #         W1.write("{}, ".format(num))
        #     W1.write("'aaa'),\n")
        #     time.sleep(0.01)

        # 单独写一行
        # Upload_timestamp = now_time()  # 上传时间戳
        # W1.write("      ('{}', ".format(Upload_timestamp))
        # # 输入id
        # W1.write("{}, ".format(x+1))
        # for i in range(nrows-1):  
        #     num = int(random.choice([0,1]))
        #     W1.write("{}, ".format(num))
        # W1.write("'aaa');\n\n")

        print("     {}行，实际{}个变量".format(nrows, nrows-1))
        print("     {}数据处理完毕".format(sheet_name))
        
        W1.close
