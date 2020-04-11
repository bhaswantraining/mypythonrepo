import boto3
s3 = boto3.client('s3')
s3.upload_file('s3_Transfer.txt', 'rupatestbucket', 'S3_File.txt')

s3 = boto3.resource('s3')
for i in (s3.buckets.all()):
    print(i)

bucket = s3.Bucket('rupatestbucket')
for obj in bucket.objects.all():
    print(obj.key, obj.last_modified)

bucket.upload_file('Test_file', 'Test_file')
bucket.download_file('S3_File.txt', 'local_file.txt')

#bucket.put_object('Test_file')

for obj in bucket.objects.all():
    if obj.key == 'Test_file':
        print('Test_file present in the bucket')
        body = obj.get()['Body'].read().decode('utf-8')
        #   print(type(body))
        #   print(body)
        line_cnt= 0
        f1 = open('Create_file.txt', 'w')
        for line in body.splitlines():
            print(str(line))
            f1.write(str(line) + "\n")
            line_cnt = line_cnt + 1
            #  print(type(line))

print('File :- ', obj.key , 'has ', line_cnt, 'lines')
