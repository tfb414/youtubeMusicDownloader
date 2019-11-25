from ffmpy import FFmpeg
import os

# add error handling if it has already been converted
# get the -y command to work


def convert_to_mp3(file_name_with_extension, file_name):
    input = f'tmp/{file_name_with_extension}'
    output = f'tmp/{file_name}.mp3'
    ff = FFmpeg(
        inputs={input: None},
        outputs={output: None}
    )
    ff.run()


def get_file_names():
    return os.listdir("tmp")


def main():
    file_names = get_file_names()
    print(file_names)

    for f in file_names:
        split_file_name = f.split('.')
        if (split_file_name[1] != 'mp3' and split_file_name[1] != 'mp4' and split_file_name[1] != 'DS_Store'):
            convert_to_mp3(f, split_file_name[0])


main()
