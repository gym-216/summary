# 合并分支

# git merge

# 场景：
# 		1、在develop分支开发完之后, 合并到master分支
# 				git checkout develop 		--先切换到develop分支
# 				git pull origin develop 	--拉取develop分支最新代码
# 				git checkout master 		--切换到master分支
# 				git pull origin master 		--拉取master分支最新代码
# 				git merge develop			--在master分支 merge develop分支 ***
# 				git push -u origin master 	--将从develop分支merge到的代码 提交到master分支

# 		   在bug分支开发完之后,合并到develop分支
# 				git checkout bug 			--切换到bug分支
# 				git pull origin bug 		--拉取bug分支最新代码
# 				git checkout develop 		--切换到develop分支
# 				git pull origin develop 	--拉取develop分支最新代码
# 				git merge bug
# 				git push -u origin develop

#		2、master分支代码改动,更新到develop开发分支
# 				git checkout master 		--切换到master分支
# 				git pull origin master 		--拉取master分支最新代码
# 				git chekcout develop 		--切换到develop分支
# 				git pull origin develop 	--拉取develop分支最新代码
# 				git merge master 			--merge master分支最新代码
# 				git push -u origin develop 	--将merge到的master分支代码提交到develop分支

# 			develop分支有改动,更新到bug分支
# 				git checkout develop 		--切换到develop分支
# 				git pull origin develop 	--拉取develop分支最新代码
# 				git checkout bug 			--切换到bug分支
# 				git pull origin bug	 		--拉取bug分支最新代码
# 				git merge develop 			--merge develop分支最新代码
# 				git push -u origin bug		