import os
import subprocess

def update_all():
	for _dir in os.listdir("."):
		if os.path.isdir(_dir):
			cmd = 'cd %s & git pull  -v --progress "origin"' % _dir
			print "cmd:", cmd
			os.system(cmd)

def list_all():
	gitlist = []
	for _dir in os.listdir("."):
		if os.path.isdir(_dir):
			cmd = 'cd %s & git remote get-url origin' % _dir
			out = subprocess.check_output(cmd, shell=True)
			gitlist.append(out)
	with open("./repolist.txt", "w") as f:
		f.write("".join(gitlist))

if __name__ == '__main__':
	update_all()
	list_all()