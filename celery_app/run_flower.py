import subprocess

cmd = [
    'flower',
    '--broker=redis://127.0.0.1:6379/0',  # 监控的broker的地址
    # '--basic_auth=root:123456',  # 登录flower需要的用户名和密码
    '--port=5555',  # flower需要的端口号
    '--url_prefix=flower'  # 主页的路径前缀 比如:https://west.com/flower/
]
if __name__ == '__main__':
    subprocess.run(cmd)