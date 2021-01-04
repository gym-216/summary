# 删除远程分支

# 场景:
# 		git已经删除远程分支,本地仍然能看到

#		查看本地分支
#		git branch

#		查看远程分支
#		git branch -r

#		查看所有分支(本地+远程)
#		git branch -a
#		发现在远程已经删除的分支 本地仍可以看到

#		查看remote地址,远程分支与本地分支对应关系  **
#		git remote show origin
#		发现远程仓库不存在的分支

#		删除本地存在 远程不存在的分支 **
#		git remote prune origin

#		删除本地分支
#		git branch -d 分支名
#		git branch -D 分支名  (强制删除)

#		删除远程分支
#		git push origin --delete 分支名
