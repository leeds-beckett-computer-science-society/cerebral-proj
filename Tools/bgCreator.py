import os


# script to get list of all files
# in dir tree for entered path
# copy and paste output into bg.txt file

def getListOfFiles(dirname):

    # create list of file and sub dirs
    filelist = os.listdir(dirname)
    allfiles = list()

    # iterate over entries
    for entry in filelist:
        fullpath = os.path.join(dirname, entry)

        # if entry is dir get list of file in dir
        if os.path.isdir(fullpath):
            allfiles = allfiles + getListOfFiles(fullpath)
        else:
            allfiles.append(fullpath)

    return allfiles


def main():
    # enter path
    dirname = '/home/slightowl/Desktop/opencv_workspace/KnivesImagesDatabase/neg';

    # get list of files in dir tree
    filelist = getListOfFiles(dirname)

    # print files
    for elem in filelist:
        print(elem)

    print("**********")

    # get list of files in dir tree
    filelist = list()
    for (dirpath, dirnames, filenames) in os.walk(dirname):
        filelist += [os.path.join(dirpath, file) for file in filenames]

    # print files
    for elem in filelist:
        # for pos images add ' 1 0 0 50 50'
        print("/home/slightowl/Desktop/opencv_workspace/KnivesImagesDatabase/neg" + os.path.basename(elem))


if __name__ == '__main__':
    main()
