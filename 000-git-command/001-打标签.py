# 发布版本 打标签

# 查看本地所有tag
# git tag
# git tag -l '模式匹配'
# git tag --list

# 查看指定tag版本信息
# git show v1.0

# 创建tag  -打标签
# git tag -a v1.0 -m "tag描述"
# -a 增加add
# -m 描述

# 提交tag
# git push origin --tags  将本地所有tag一次性提交到git服务器
# git push origin v1.0    将指定某版本号tag提交到git服务器

# 删除tag
# 删除本地tag：git tag -d v1.0
# 删除远程tag：git push origin --delete tag v1.0
