hide-symlinks
=============

A simple FUSE filesystem that makes symlinks look like actual files.

You can run it by calling the package (the directory with __main__.py at the root) like so: `python hide-symlinks/ <root> <mount-point>`, where <root> is the directory to be mirrored or looped, and <mount-point> is the (empty) directory to mount the new fuse filesystem.

You can make the package executabe by running make, the output is titled 'hide-symlinks', and is based on [this blog post](http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html "Bundling Python Files").

It is based on [fusepy](https://github.com/terencehonles/fusepy), and uses the included Loopback example as a base. It simply changes the getattr operation to use the os.stat call instead of the os.lstat call, effectively hiding symlinks. I also removed the symlink operation (which seems to have issues, though it does work). Otherwise, all operations work as normal for a loopback filesystem (e.g. writes and reads defers to the <root> directory).
