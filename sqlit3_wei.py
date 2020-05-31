import sqlite3


class weiSqlite3:
    def __init__(self,path):
        """sqlite3增删改查"""
        self.conn = sqlite3.connect(path) #连接数据库，不存在则创建
        self.cursor = self.conn.cursor() #创建游标

    def s_add_del_dpd(self,*sql):
        """创建表、添加数据、删除、修改"""
        self.cursor.execute(*sql)
        self.conn.commit() #保存操作

    def s_sel(self,*sql):
        """查询数据"""
        return self.cursor.execute(*sql).fetchall()




class weiSqlite3_dxm(weiSqlite3):
    def __init__(self,path):
        super().__init__(path=path)

    def add_table1(self,user_name):
        self.paiming = user_name.split(':')[0]+'_排名'
        #table_name = '自然之名旗舰店_排名'
        self.zhuanhua = user_name.split(':')[0] + '_转化'
        #table_name1 = '自然之名旗舰店_转化'
        fields_1 = '''日期 integer primary key autoincrement,
            转人工率 real,转人工率top real,
            卡片点击率 real,卡片点击率top real,
            接待占比 real,接待占比top real,
            小蜜参与询单转化率 real,小蜜参与询单转化率top real,
            人工询单转化率 real,行业排名 integer'''
        # 转人工率|转人工率top
        # 首问语uv点击率|首问语uv点击率top
        # 智能服务占比|智能服务占比top
        # 店小蜜询单转化|店小蜜询单转化top
        # 人工参与询单转化率

        fields_2  = '''日期 integer primary key autoincrement,
            纯店小蜜询单转化率 real,接待人数 integer,
            小蜜参与询单人数 integer,人工衔接后下单率 real'''
        # 全自动纯店小蜜询单转化率|全自动接待UV
        # 全自动参与询单UV|工衔接后下单率=店小蜜接待后转工下单UVnew/店小蜜接待后转人工询单UVnew

        sql = f'create table if not exists {self.paiming} ({fields_1})'
        sql1 = f'create table if not exists {self.zhuanhua} ({fields_2})'

        self.s_add_del_dpd(sql)
        self.s_add_del_dpd(sql1)



sql = 'select pm.日期,转人工率,转人工率top,人工衔接后下单率,卡片点击率,卡片点击率top,纯店小蜜询单转化率,\
小蜜参与询单转化率,人工询单转化率,小蜜参与询单转化率top,接待占比,接待占比top,小蜜参与询单人数,\
接待人数 from 自然之名旗舰店_排名 pm,自然之名旗舰店_转化 zh where pm.日期 = zh.日期 and pm.日期>20200101'


sql1='''
select * 
from 自然之名旗舰店_排名 pm,自然之名旗舰店_转化 zh 
where pm.日期=zh.日期 and (pm.日期 between 20200100 and 20200132)
'''

sq=weiSqlite3('data.db')
c1=sq.s_sel('select name from sqlite_master where type = "table" order by name')
tb={i[0]:sq.s_sel(f'pragma table_info({i[0]})') for i in c1}


print(6666)

