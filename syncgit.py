import os
os.system("git fetch upstream")
os.system("git checkout master")
os.system("git merge upstream/master")
os.system("git push origin master")
os.system("git checkout hotfixes")
os.system("git merge upstream/hotfixes")
os.system("git push origin hotfixes")
os.system("git checkout develop")
os.system("git merge upstream/develop")
os.system("git push origin develop")
