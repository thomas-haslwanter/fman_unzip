from fman import DirectoryPaneCommand, show_alert
import os
import zipfile
from fman.url import as_human_readable
from fman.url import as_url


class UnZipSelected(DirectoryPaneCommand):
    def __call__(self):
        selected_files = self.pane.get_selected_files()
        output = ""
        if len(selected_files) >= 1 or (len(selected_files) == 0 and self.get_chosen_files()):
            if len(selected_files) == 0 and self.get_chosen_files():
                selected_files.append(self.get_chosen_files()[0])
            dirPath = os.path.dirname(as_human_readable(selected_files[0]))
            unZipName = os.path.basename(as_human_readable(selected_files[0]))
            inFile = os.path.join(dirPath, unZipName)
            unZipDir = unZipName[:-4]
            unZipPath = os.path.join(dirPath, unZipDir)
            zipfile.ZipFile(inFile).extractall(path=unZipPath)
            output += "Files were unzipped to directory {0}".format(unZipDir)
        else:
            output += "No files or directories selected"

        show_alert(output)
