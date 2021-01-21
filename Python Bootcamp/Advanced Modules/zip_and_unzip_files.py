# assuming 2 files existing on current directory: fileOne.txt, fileTwo.txt
import zipfile
comp_file = zipfile.ZipFile('comp_file.zip', 'w')   # create a comp_file.zip in write mode
comp_file.write('fileOne.txt', compress_type=zipfile.ZIP_DEFLATED)  # write fileOne to zip file
comp_file.write('fileTwo.txt', compress_type=zipfile.ZIP_DEFLATED)  # write fileTwo to zip file
comp_file.close()   # close the zip file

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')  # read the zip file
zip_obj.extractall('extracted_content')     # extract the content of the zip_object into extracted_cnotent dir
