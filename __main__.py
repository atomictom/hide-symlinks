import sys
import fuse
from hide_symlinks import HideSymlinks

def main():
	if len(sys.argv) != 3:
		print 'usage: {} <root> <mountpoint>'.format(sys.argv[0])
		exit(1)

	# Start the FUSE FS
	fuse.FUSE(HideSymlinks(sys.argv[1]), sys.argv[2], foreground=True)

if __name__ == '__main__':
	main()
