# 创建本地分支推送到远程

# 查看本地分支
# git branch
# 查看远程分支
# git branch -r
# 查看所有分支(本地+远程)
# git branch -a

# 查看当前分支状态
# git status

# 创建本地分支
# git branch 新建分支名

# 切换分支
# git checkout 分支名 (如果当前分支有未提交,切换不了,需要强制切分支)

# 强制切分支
# git checkout -f 分支名

# 创建本地分支并切换 ***
# git checkout -b 新建分支名

# 推送本地分支到远程
# git push origin 新建远程分支名:本地新建分支名
# git push origin 新建远程分支名

# 删除本地分支
# git branch -d 分支名

# 删除远程分支
# git push origin --delete 分支名
# 或推送一个空的分支,删除远程分支
# git push origin :分支名

# 本地已经拉取主分支,要拉取远程某一分支代码到本地
# git checkout -b 本地新建分支名 origin/远程分支