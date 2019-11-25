from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import glob

gauth = GoogleAuth()
gauth.LocalWebserverAuth()

drive = GoogleDrive(gauth)


def get_file_names():
    return glob.glob('tmp/*.mp*')


def clean_up_file_name(file_name):
    split_name_by_slash = file_name.split('/')
    clean_name = split_name_by_slash.pop(1).split('.')
    return clean_name.pop(0)


def upload_to_drive(file_name):
    clean_file_name = clean_up_file_name(file_name)
    file_boy = drive.CreateFile(
        {'title': clean_file_name,
         'mimeType': 'audio/mpeg',
         "parents":
            [{"kind": "drive#fileLink", "id": "1vM5tZ1llHtF1luqAjiLPrth0xPXWJHxW"}]
         })
    file_boy.SetContentFile(file_name)
    file_boy.Upload()


def main():
    file_names = get_file_names()
    for f in file_names:
        upload_to_drive(f)


main()
