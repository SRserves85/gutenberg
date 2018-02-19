import glob
import json
import re

import boto3

from multiprocessing import Process, Pool


def upload_gutenberg(path):
    """ Takes a tuple of (i, path) and uploads information from path to s3
    """

    # crete boto object

    s3 = boto3.resource('s3')

    # split the tuple
    out = {}
    try:
        with open(path) as f:
            lines = f.read()

            # match the book id
            _id = re.search('\[EBook(.*?)\]', lines)

            if _id == None:
                return

            _id = _id.group()[8:-1]

            out[_id] = blob[_id]
            out[_id]['txt'] = lines
            f.close()
            print('found_file: {}'.format(path))

            with open('data/s3/{}.json'.format(_id), 'w') as f:
                json.dump(out, f)
            del out

            # # create and upload to s3
            # s3.Object('sr-guten', 'data/{}.json'.format(_id)).put(Body=json.dumps(out))
            # print('uploaded: {} to s3'.format(path))

    except UnicodeDecodeError:
        pass

    except Exception as e:
        print(e)
        pass

if __name__ == '__main__':

    with open('gutenberg-metadata/gutenberg-metadata.json') as f:
        blob = json.load(f)

    i = 0
    proc = Pool()
    proc.map(upload_gutenberg, glob.iglob('data/gutenberg/**/*.txt', recursive=True), chunksize=20)
