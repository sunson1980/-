'''
 # @ Author: chenbo
 # @ Create Time: 2019-07-20 12:11:30
 # @ Modified by: chenbo
 # @ Modified time: 2019-07-20 12:11:49
 # @ Description:creat new dir
 '''
import os
import argparse


def creat_dir(dirc, newdir):
    '''
    creat a directory if it is not exists
    @parameter dirc:where to creat a directory
    @parameter newdir:the new directory
    '''
    try:
        if os.path.isdir(dirc):
            if not os.path.exists(os.path.join(dirc, newdir)):
                os.makedirs(os.path.join(dirc, newdir))
            else:
                print("The directory already exists")
    except Exception as event:
        print(event)


def get_parser():
    """
    def arguments
    """
    parser = argparse.ArgumentParser(
        description='creat a new directory if it don`t exists')
    parser.add_argument('dirc', type=str, nargs=1, help='the path')
    parser.add_argument('newdir', type=str, nargs=1, help='new directory')
    return parser


def main():
    """
    This will be called if the script is directly invoked.
    """
    parser = get_parser()
    args = vars(parser.parse_args())
    dirc = args['dirc'][0]
    newdir = args['newdir'][0]
    creat_dir(dirc, newdir)


if __name__ == '__main__':
    # creat_dir(r'C:\Users\陈波\Downloads\pyttest', 'newdir')
    main()
