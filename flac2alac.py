import os
import sys

input_dir_name = ''
input_dir = None
output_dir_name = ''
output_dir = None

def gen_dirs(args):
    global input_dir_name
    global input_dir
    global output_dir_name
    global output_dir

    if len(args) == 2:
        if os.path.isdir(args[1]):
            input_dir_name = args[1]
            input_dir = os.fsencode(input_dir_name)
            output_dir_name = input_dir_name
            output_dir = input_dir
        else:
            print('Given path is not a dir')
    elif len(args) == 3:
        if os.path.isdir(args[1]):
            input_dir_name = args[1]
            input_dir = os.fsencode(input_dir_name)
            output_dir_name = args[2]
            output_dir = os.fsencode(output_dir_name)

            try:
                os.mkdir(args[2])
            except FileExistsError:
                pass
            except PermissionError:
                print(f"Permission denied: Unable to create '{args[2]}'!")
            except Exception as error:
                print(f"An error occurred: {error}")
        else:
            print('Given path is not a dir!')
    else:
        if len(args) < 2:
            print('Not enough arguments!')
        else:
            print('Too many arguments!')
        exit()


def convert():
    global input_dir_name
    global input_dir
    global output_dir_name
    global output_dirs

    input_file_name = ''
    base_file_name = ''
    alac_ext = '.m4a'

    flacs_found = False

    for file in os.listdir(input_dir):
        input_file_name = os.fsdecode(file)
        if os.path.splitext(input_file_name)[1] == '.flac':
            flacs_found = True
            base_file_name = input_file_name[:-5]
            os.system(f'ffmpeg -i "{input_dir_name}/{input_file_name}" -c:a alac -c:v copy "{output_dir_name}/{base_file_name}{alac_ext}"')

    if not flacs_found:
        print('No flacs found!')


gen_dirs(sys.argv)
convert()
