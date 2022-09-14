class Config :
    JWT_SECRET_KEY = 'JWT_SECRET_KEY'
    JWT_ACCESS_TOKEN_EXPIRES = False
    PROPAGATE_EXCEPTIONS = True

    ACCESS_KEY = 'ACCESS_KEY'
    SECRET_ACCESS = 'SECRET_ACCESS'
    # S3 버킷이름과, 기본 URL 주소 셋팅
    S3_BUCKET = 'S3_BUCKET'
    S3_LOCATION = 'S3_LOCATION'