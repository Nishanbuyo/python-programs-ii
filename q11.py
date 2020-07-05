def file_and_extension(filename):
    filenamee = filename[:-4]
    extension = filename[-3:]
    return filenamee, extension

filename,extension = file_and_extension('README.txt')
print("Filename: ", filename)
print("Extension: ", extension)