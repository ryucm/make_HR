import boto3

# s3 클라이언트 생성
s3 = boto3.client('s3')

response = s3.list_buckets()

# 업로드할 파일의 이름
filename = ['saramin.csv','jobkorea.csv']


# 업로드할 s3 버킷
bucket_name = 'sorabbang'

# 첫번째 매개변수 : 로컬에서 올릴 파일이름
# 두번째 매개변수 : s3 버킷 이름
# 세번째 매개변수 : 버킷에 저장될 파일 이름
for i in filename:
    s3.upload_file(i, bucket_name, i)