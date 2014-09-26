hide-symlinks
=============

A simple FUSE filesystem that makes symlinks look like actual files.

It works by calling the package like so: `python hide-symlinks <root> <mount-point>`, where <root> is the directory to be mirrored or looped, and <mount-point> is the (empty) directory to mount the new fuse filesystem.

You can make the package executabe by running make, the output is titled 'hide-symlinks', and is based on [this blog post](http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html).

It is based on [fusepy](https://github.com/terencehonles/fusepy), and uses the included Loopback example as a base. It then removes the symlink operation (which seems to throw errors about not working, though it does appear work, so I just removed it), and changes the getattr operation to use the os.stat call instead of the os.lstat call, effectively hiding symlinks. Otherwise, all operations work as normal for a loopback (everything defers to the <root> directory).
