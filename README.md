- 连接MySQL并运行以下命令以及在新建数据库中运行以下命令（数据库名可以自由取舍）
```sql
CREATE DATABASE test;
```

- 编辑lib.conf.py文件与自己的主机环境相匹配
- 命令行中cd到当前项目主程序main.py所在的目录
- 以下命令为使用方法示例
```sh
python main.py -type help		# 输出帮助（本内容）
python main.py -type select		# 输出数据库中现有的全部url-name的键值对
python main.py -type download	# 将数据库中现有的全部键值对能下载的全部下载
python main.py -type insert		# 如果后边不加其他参数的话，目前功能尚未开发完善，此部分目的是将网站全部参数导入MySQL
python main.py -type insert --biantai 0 --value "![](xx/autsKBEUobaujwT.png)" 	# biantai参数的值为0的时候value的传参应当是markdown文档的格式（相信大部分人使用图床的目的也应该是使用markdown吧）
python main.py -type insert --biantai 1 --value xx/autsKBEUobaujwT.png 			#biantai参数的值为非0的时候value的传参应当是url的完整格式（如果直接获取url的话就应该是这样）
```
