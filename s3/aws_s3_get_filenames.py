import boto3
import time
from botocore.client import Config

# Please edit the following values to run the script as per your requirements

# Name of the bucket
SRC_BUCKET = 'sample-bucket-name'
# Path inside the bucket
SRC_BUCKET_PREFIX = 'FolderName/SubFolderName/'
# Name of the file in which you want the result to be saved
FILE_NAME = 'filename.txt'

# End of editable field values


client_config = Config(
    retries=dict(max_attempts=3),
    signature_version='s3v4'
)

s3 = boto3.resource('s3', config=client_config)
bucket = s3.Bucket(SRC_BUCKET)


def get_all_filenames():
    file_names = []
    for obj in bucket.objects.filter(Prefix=SRC_BUCKET_PREFIX):
        file_names.append(obj.key)
    return file_names


def extract_file_type_mp4(file_names):
    output_file_names = []
    for file_name in file_names:
        if file_name.endswith('.mp4'):
            output_file_names.append(file_name)

    return output_file_names


def write_to_text_file(contents):
    with open(FILE_NAME, 'w+') as file_writer:
        for object_key in contents:
            file_writer.write("%s\n" % object_key)


if __name__ == '__main__':
    file_names = get_all_filenames()
    contents = extract_file_type_mp4(file_names)
    write_to_text_file(contents)
