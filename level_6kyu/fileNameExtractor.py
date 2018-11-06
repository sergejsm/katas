import re

class FileNameExtractor:
    def extract_file_name(dirty_file_name):
        return re.search('(?<=_)[^.]+\w+\.+[^.]+\W+', dirty_file_name).group()[:-1]
        # return re.search('(?<=_)\w+\.\w+', dirty_file_name).group()


print(FileNameExtractor.extract_file_name("088172418_-_SVUgKegijbEj_QVphZX_dPNNuu_lD.3u-i.7556_Q395wXr6txT6419_vB17agO"))
print(FileNameExtractor.extract_file_name("1_FILE_NAME.EXTENSION.OTHEREXTENSIONadasdassdassds34"))
print(FileNameExtractor.extract_file_name("9666867390404776030571878661486_VgEc-naSfR.53-.9419L4u4p0DB6DO09H3"))



#Best Solutions:


class FileNameExtractor1:
    def extract_file_name(dirty_file_name):
        return re.match(r'\d+_(.+?\..+?)\.', dirty_file_name).group(1)


class FileNameExtractor2:
    def extract_file_name(dirty_file_name):
        matched = re.search(r'\d+_([^.]+\.[^.]+)', dirty_file_name)
        return matched.group(1)