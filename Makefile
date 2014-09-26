all:
	zip -r hide-symlinks.zip *
	echo '#!/usr/bin/env python' | cat - hide-symlinks.zip > hide-symlinks
	chmod u+x hide-symlinks

clean:
	rm hide-symlinks.zip
	rm hide-symlinks
