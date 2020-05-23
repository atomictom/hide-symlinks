all:
	zip -r hide-symlinks.zip *
	echo '#!/usr/bin/env python3' | cat - hide-symlinks.zip > hide-symlinks
	chmod u+x hide-symlinks

clean:
	rm -f hide-symlinks.zip
	rm -f hide-symlinks
