import sys
import fuse
from hide_symlinks import HideSymlinks

def main():
	if len(sys.argv) < 3:
		print 'usage: {} <root> <mountpoint>'.format(sys.argv[0])
		exit(1)

        # Find the filesystem options (the things following "-o")
        options = ""
        for i in range(len(sys.argv)):
            if sys.argv[i] == "-o" and len(sys.argv) > i+1:
                options = sys.argv[i+1]

        # Turn them into a format fuse.FUSE can handle (kwargs)
        fuse_args = {}
        for option in options.split(","):
            option_parts = option.split("=")
            if len(option_parts) == 1:
                fuse_args[option_parts[0]] = True
            else:
                fuse_args[option_parts[0]] = option_parts[1]

	# Start the FUSE FS
        fuse.FUSE(HideSymlinks(sys.argv[1]), sys.argv[2], foreground=False, **fuse_args)

if __name__ == '__main__':
	main()
