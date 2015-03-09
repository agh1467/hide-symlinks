import os
import os.path
import sys
from loopback import Loopback

class HideSymlinks(Loopback):

    # This will superscede the readdir from loopback
    def readdir(self, path, fh):
        # Add current, and parent directoires to the list
        directory_list = ['.', '..']
        for entry in os.listdir(path):
            # Check to see if the current entry in the list is a link
            if not os.path.islink(os.path.join(path,entry)):
                # Add it to the directory list if it is
                directory_list += [entry]
        return directory_list
