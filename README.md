hide-symlinks
=============

A simple FUSE filesystem that makes symlinks look like actual files.

Compile
-------

You can compile the package into an executabe by running *make*. The output is titled 'hide-symlinks'. The idea is based on [this blog post](http://blog.ablepear.com/2012/10/bundling-python-files-into-stand-alone.html "Bundling Python Files").

Run
---

You can run it by calling the executable like so: `./hide-symlinks <root> <mount-point>`, where `<root>` is the directory to be mirrored or looped, and `<mount-point>` is the (empty) directory to mount the new fuse filesystem.

Mount
-----

You can mount it in /etc/fstab by adding a line like so:

    /path/to/hide-symlinks#/path/to/root /path/to/mount fuse user,allow_other,noexec 0 0

In this example, I use the 'user' option to allow any user to mount the filesystem and 'allow\_other' to allow any user to access the filesystem. These are not strictly necessary, but because /etc/fstab entries which are auto mounted are done so by root, only root can access the filesystem without 'allow\_other'. And, if it is not auto mounted, without the 'user' option only root can mount it. Also note that the hide-symlinks executable and root directory are separated by a "#".

How It Works
------------

The filesystem relies on [fusepy](https://github.com/terencehonles/fusepy), and uses the Loopback example included with fusepy as a base class. It simply changes the getattr operation to use the os.stat call instead of the os.lstat call, effectively hiding symlinks. I also removed the symlink operation (which seems to have issues, though it does work). Otherwise, all operations work as normal for a loopback filesystem (e.g. writes and reads defer to the `<root>` directory).
