# 根据tag创建分支

# 主分支master 有一个tag版本v0.2.4

# 获取master分支最新
# git pull origin master
# 根据tag创建feature分支
# git branch feature v0.2.4
# 切换到新创建分支
# git checkout feature
# 本地创建分支推送到远程
# git push origin feature

# 版本回退场景：
# 在feature分支拉取代码时，不小心拉取了master分支代码，在feature分支进行了无用提交
# 版本回退
# git reset --hard commit id 
# 例：
# git reset --hard 139dcfaa558e3276b30b6b2e5cbbb9c00bbdca96