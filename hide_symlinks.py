"""Simple FUSE filesystem that mirrors a dir but hides symlinks."""
import os
import os.path

from loopback import Loopback


class HideSymlinks(Loopback):
    """A loopback filesystem that overrides geattr to hide symlinks."""

    symlink = None

    def getattr(self, path, fh=None):
        stat = os.stat(path)
        keys = ('st_atime', 'st_ctime', 'st_gid', 'st_mode',
                'st_mtime', 'st_nlink', 'st_size', 'st_uid')
        return dict((key, getattr(stat, key)) for key in keys)
