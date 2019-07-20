'''
 # @ Author: chenbo
 # @ Create Time: 2019-07-18 12:25:53
 # @ Modified by: chenbo
 # @ Modified time: 2019-07-19 11:48:39
 # @ Description:This will batch rename a group of files in a given directory,
once you pass the current and new extensions
 '''
import os
import argparse


def rename(dirc, oldext, newext):
    """
    This will batch rename a group of files in a given directory,
    once you pass the current and new extensions
    """
    for file in os.listdir(dirc):
        split_file = os.path.splitext(file)
        if not newext[0] == '.':
            newext = '.' + newext
        if not oldext[0] == '.':
            oldext = '.' + oldext
        file_ext = split_file[1]
        if file_ext == oldext:
            newfile = split_file[0] + newext
            os.rename(os.path.join(dirc, file), os.path.join(dirc, newfile))


def get_parser():
    '''
    def argument
    '''
    parser = argparse.ArgumentParser(
        description='change extension of files in a working directory')
    parser.add_argument('work_dir',
                        metavar='WORK_DIR',
                        type=str,
                        nargs=1,
                        help='the directory where to change extension')
    parser.add_argument('old_ext',
                        metavar='OLD_EXT',
                        type=str,
                        nargs=1,
                        help='old extension')
    parser.add_argument('new_ext',
                        metavar='NEW_EXT',
                        type=str,
                        nargs=1,
                        help='new extension')
    return parser

def main():
    """
    This will be called if the script is directly invoked.
    """
    parser = get_parser()
    args = vars(parser.parse_args())
    work_dir = args['work_dir'][0]
    old_ext = args['old_ext'][0]
    new_ext = args['new_ext'][0]
    rename(work_dir, old_ext, new_ext)

if __name__ == '__main__':
    main()
    