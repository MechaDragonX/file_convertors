import os
import sys

# Name of input dir
input_dir_name = ''
# OS obj of input dir
input_dir = None
# Name of output dir
output_dir_name = ''
# OS obj of output dir
output_dir = None

# Generate input and output dir variables
def gen_dirs(args):
    # Use global vars
    global input_dir_name
    global input_dir
    global output_dir_name
    global output_dir

    # Check length of args
    # Accepted lengths: 2 and 3 (hence 1-2 passed args aside from file)
    #
    # If 1 passed arg...
    if len(args) == 2:
        # Check if passed arg is a dir
        # If so...
        if os.path.isdir(args[1]):
            # Set input_dir global vars
            input_dir_name = args[1]
            input_dir = os.fsencode(input_dir_name)
            # Set output_dir global vars to be the same as input dir
            output_dir_name = input_dir_name
            output_dir = input_dir
        # Otherwise...
        else:
            print('Given path is not a dir')
    # If 2 passed args...
    elif len(args) == 3:
        # Check if passed arg is a dir
        # If so...
        if os.path.isdir(args[1]):
            # Set input_dir global vars
            input_dir_name = args[1]
            input_dir = os.fsencode(input_dir_name)
            # Set output_dir global vars
            output_dir_name = args[2]
            output_dir = os.fsencode(output_dir_name)

            # Try to creat output dir
            try:
                os.mkdir(args[2])
            # If it already exists then just move on
            except FileExistsError:
                pass
            # Handle perm error and quit
            except PermissionError:
                print(f"Permission denied: Unable to create '{args[2]}'!")
                quit()
            # Handle other error and quit
            except Exception as error:
                print(f"An error occurred: {error}")
                quit()
        # otherwise...
        else:
            print('Given path is not a dir!')
    # Otherwise...
    # Not enough or too much args
    else:
        # Alert user accordingly
        if len(args) < 2:
            print('Not enough arguments!')
        else:
            print('Too many arguments!')
        exit()


# Perform conversion
def convert():
    # Use global vars
    global input_dir_name
    global input_dir
    global output_dir_name
    global output_dirs

    # Vars for each file in dir
    input_file_name = ''
    base_file_name = ''
    alac_ext = '.m4a'

    # Boolean to alert user if no conversions happened
    flacs_found = False

    # Loop through input dir
    for file in os.listdir(input_dir):
        # Set current file to filename
        input_file_name = os.fsdecode(file)
        # Check if current file is a FLAC file
        if os.path.splitext(input_file_name)[1] == '.flac':
            # At least one was found, so bool can be set as True
            flacs_found = True
            # Create base file name without extension
            base_file_name = input_file_name[:-5]
            # User FFMPEG to take input file, convert audio to alac, copy video stream (album art), and output to output_dir/base.alac
            os.system(f'ffmpeg -i "{input_dir_name}/{input_file_name}" -c:a alac -c:v copy "{output_dir_name}/{base_file_name}{alac_ext}"')

    # If not conversions happened, alert user
    if not flacs_found:
        print('No flacs found!')


gen_dirs(sys.argv)
convert()
