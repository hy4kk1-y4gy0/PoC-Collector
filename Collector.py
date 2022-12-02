import os
from optparse import OptionParser

def init():
	os.system("mkdir /opt/exploitDB")
	os.system("mkdir repo_urls")

def update():
	os.system("rm sources/nomi-sec.md")
	os.system("wget https://raw.githubusercontent.com/nomi-sec/PoC-in-GitHub/master/README.md -O sources/nomi-sec.md")
	os.system("rm -rf repo_urls/*")
	filename = "sources/nomi-sec.md"

	with open(filename) as f:
		lines = f.readlines()

		CVE = ""
		CVE_repo = []
		
		print("[+] Generating CVE PoC Repository List...")
		for line in lines:
			data = line.split(" ")

			if data[0] == "###":
				CVE = data[1].split("\n")[0]
			elif data[0] == "-":
				CVE_repo.append(data[1])
			elif data[0] == "\n" and not CVE == "" and not CVE_repo == []:
				os.system("touch repo_urls/" + CVE)
				with open("repo_urls/" + CVE, "w") as repo:
					repo.writelines(CVE_repo)
				CVE = ""
				CVE_repo = []
		print("[!] Generation Complete")

def clone_all(CVE):
	filename = "repo_urls/" + CVE
	basedir = "/opt/exploitDB/"     # Repository Location

	try:
		with open(filename) as f:
			lines = f.readlines()

			for line in lines:
				md = line.split("](")
				dirname = basedir + CVE + "/" + md[0].split("[")[1].replace("/", "_")
				repo = md[1][:-2]
				os.system("git clone " + repo + " " + dirname)
				print()
	except:
		print("[!] No Related PoC on Github TAT")


def clone_repo(CVE, repo):
	basedir = "/opt/exploitDB/"     # Repository Location
	repo_url = "https://github.com/" + repo
	dirname = basedir + CVE + "/" + repo.replace("/", "_")

	try:
		print()
		os.system("git clone " + repo_url + " " + dirname)
	except:
		print("[!] No Related PoC on Github TAT")

def search(CVE):
	filename = "repo_urls/" + CVE
	repo = []

	try:
		with open(filename) as f:
			lines = f.readlines()
			repo_amount = 0

			for line in lines:
				repo_amount += 1
				md = line.split("](")
				repo_name = md[0][1:]
				repo.append(repo_name)
				print(("[%3d] " % repo_amount) + repo_name)
		choice = int(input("Which repository do you want to clone? "))
		clone_repo(CVE, repo[choice - 1])
	except:
		print("[!] No Related PoC on Github TAT")
	


def main():
	usage = "Usage: Collector.py [options] [arg1]"
	parser = OptionParser(usage = usage)

	parser.add_option("-i", "--init",
						action = "store_true", default = False,
						dest = "init",
						help = "Create related directory and file")
	parser.add_option("-u", "--update",
						action = "store_true", default = False,
						dest = "update",
						help = "Update the PoC Collection")
	parser.add_option("-c", "--clone",
						dest = "cve",
						help = "Clone all PoC of the specified CVE")
	parser.add_option("-s", "--search",
						dest = "vuln", 
						help = "Find if there are PoC of CVE")

	(options, args) = parser.parse_args()

	if options.init:
		init()
	elif options.update:
		update()
	elif options.cve != None:
		clone(options.cve)
	elif options.vuln != None:
		search(options.vuln)
	else:
		print("Usage: " + parser.usage)
		exit()

if __name__ == "__main__":
    main()
