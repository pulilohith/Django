def handle_file_upload(f):
    with open('Upbytes/static/Upload_Files/' + f.name, 'wb+') as des:
        for chunk in f.chunks():
            des.write(chunk)
