import os

commit = "99de31e8-dan"
release = "4.2.6-dan"
json = "4.0.1"
text = "4.0.1"
version = os.environ.get('EXABGP_VERSION',release)

# Do not change the first line as it is parsed by scripts

if __name__ == '__main__':
	import sys
	sys.stdout.write(version)
