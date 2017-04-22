import os
import os.path
import sys
from loopback import Loopback

class HideSymlinks(Loopback):

    symlink = None

    def getattr(self, path, fh=None):
        # This is the key line
        st = os.stat(path)
        keys = ('st_atime', 'st_ctime','st_gid', 'st_mode',
                'st_mtime', 'st_nlink', 'st_size', 'st_uid')
        return dict((key, getattr(st, key)) for key in keys)
