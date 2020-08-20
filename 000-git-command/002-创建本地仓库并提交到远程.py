# 创建本地仓库并提交到远程服务器

# git init
# git add .
# git commit -m "描述"
# git remote add origin 远程仓库地址
# git push -u origin master

# 解释
# git init  
# 初始化本地仓库 创建.git子目录 包含初始化git仓库所有必须文件 此时项目文件未被跟踪
# git add . 
# 跟踪所有文件(夹)  项目文件添加到暂存区
# git add 具体文件名称  
# 添加具体文件
# git commit -m "描述"
# 提交
# git remote add origin 远程仓库地址
# 本地仓库与远程仓库建立连接
# git push -u origin master
# 推送到远程仓库

# 拉取远程分支代码
# git pull origin master

# 问题:
# 拉取代码报错: fatal: refusing to merge unrelated histories
# 解决:
# git pull origin master --allow-unrelated-histories