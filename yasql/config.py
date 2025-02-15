# -*- coding:utf-8 -*-
# edit by xff

import ldap
from django_auth_ldap.config import LDAPSearch

# 关闭debug，本地开发时打开
# 生产环境请务必改为：DEBUG_ENABLED = False
DEBUG_ENABLED = True

# 在生产环境中，请变更此KEY，自己随机生成一个即可
SECRET_KEY = 'm3cfrcrlbikc16h+u8c4!gru$h8@4k)@m^p4$f=bwqi1o$r_c^'

# 配置MySQL数据库，库必须先创建，且库的字符集必须为:utf8
# 存储django程序运行的系统库表等数据
# 权限：grant all on *.* to 'xxx'@'%' with grant options
# CREATE DATABASE `yasql` /*!40100 DEFAULT CHARACTER SET utf8 */ 要设置库的字符集为utf8
DB = {
    'database': 'yasql',
    'user': 'yasql_rw',
    'host': '127.0.0.1',
    'port': 3306,
    'password': '1234.com',
}

# 连接目标需要审计或执行工单的数据库的用户
# 每个连接的目标数据库都需要创建，用于语法、工单执行、备份、查询
# create user 'yasql_rw'@'%' identified by '1234.com'
# grant all on *.* to 'yasql_rw'@'%';
# 用户名和密码请进行自行修改，不要使用默认的
REOMOTE_USER = {
    'user': 'yasql_rw',
    'password': '1234.com'
}

# 作为开发查询数据库使用
# 该账户仅设置为只读即可
# create user 'yasql_ro'@'%' identified by '1234.com'
# grant select on *.* to 'yasql_ro'@'%';
# 用户名和密码请进行自行修改，不要使用默认的
QUERY_USER = {
    'user': 'yasql_ro',
    'password': ''
}

# 查询LIMIT限制
# 如果查询没有LIMIT子句，默认加上limit default_return_rows
# 如果查询LIMIT子句返回行数大于max_return_rows，则改写为：limit max_return_rows
QUERY_LIMIT = {
    'default_return_rows': 100,
    'max_return_rows': 2000
}

# REDIS配置
# 存储session、消息队列等
REDIS = {
    'host': '127.0.0.1',
    'port': 6379,
    'password': '1234.com'
}

# 启用LDAP
# LDAP配置如下，请按照自己公司的LDAP配置进行更正
LDAP_SUPPORT = {
    'enable': False,  # 为True启用LDAP，为False禁用LDAP
    'config': {
        'AUTH_LDAP_SERVER_URI': "ldap://192.168.3.221:389",
        'AUTH_LDAP_BIND_DN': "uid=lisi,ou=people,dc=fzf,dc=com",  # 用户，绝对路径
        'AUTH_LDAP_BIND_PASSWORD': '1234.com',  # 密码
        'AUTH_LDAP_USER_SEARCH': LDAPSearch(
            "ou=people,dc=fzf,dc=com", ldap.SCOPE_SUBTREE, "(uid=%(user)s)"
        ),
        # 用户属性映射(key:value) key为系统表字段，value为ldap字段(value部分对齐自己公司的ldap属性)
        'AUTH_LDAP_USER_ATTR_MAP': {
            'username': 'uid',
            'displayname': 'description',
            'email': 'email',
            'mobile': 'phone',
            'department': 'department'
        },
        'AUTH_LDAP_ALWAYS_UPDATE_USER': True,
        'AUTH_LDAP_START_TLS': False
    }
}

# gh-ost工具使用，新的参数自行添加即可
GH_OST_ARGS = ['--allow-on-master',
               '--assume-rbr',
               '--initially-drop-ghost-table',
               '--initially-drop-old-table',
               '-exact-rowcount',
               '--approve-renamed-columns',
               '--concurrent-rowcount=false',
               '--chunk-size=800',
               '--hooks-path=/data/www/yasql/yasql/hook/']

# gAudit
GAUDIT_API = "http://127.0.0.1:8082/api/v1/audit"

# 配置接收工单消息
# 通知消息里面的url地址
NOTICE_URL = 'http://localhost:8001'

# 配置支持的通道
NOTICE = {
    'DINGDING': {
        'enabled': False,  # 是否启用消息通知
        'webhook': 'https://oapi.dingtalk.com/robot/send?xxx',  # 更换为自己的webhook地址
        'key': 'DBNotice'  # Webhook安全设置的自定义的关键字
    },
    # 此处应该是您的企业邮箱配置
    'MAIL': {
        'enabled': True,  # 是否启用消息通知
        'email_host': 'smtp.163.com',
        'email_port': '465',
        'email_host_user': 'xxx@163.com',
        'email_host_password': 'xxx',
        'email_use_ssl': True,
    },
    'WEIXIN': {
        'enabled': True,  # 是否启用消息通知
        'webhook': 'https://qyapi.weixin.qq.com/cgi-bin/webhook/xxx'  # 更换为自己的webhook地址
    }
}
