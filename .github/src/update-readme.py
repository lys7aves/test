import os

os.('echo "File list" > files.txt')
os.('find . -type f -printf "- %p %TY-%Tm-%Td %TH:%TM\n" | sed \'s/\.\///\' >> files.txt')
os.('echo "::set-output name=filelist::$(cat files.txt)"')
