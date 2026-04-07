$env:PATH += ";C:\Program Files\Amazon\AWSCLIV2"

mkdir scikit_layer
mkdir scikit_layer\python

pip install scikit-learn --target scikit_layer\python --platform manylinux2014_x86_64 --only-binary=:all: --python-version 3.11

cd scikit_layer
Compress-Archive -Path python -DestinationPath ..\scikit_layer.zip -Force
cd ..

aws s3 cp scikit_layer.zip s3://airhealth-predictor-bucket/scikit_layer.zip

aws lambda publish-layer-version --layer-name scikit-learn-layer --content S3Bucket=airhealth-predictor-bucket, S3Key=scikit_layer.zip --compatible-runtimes python3.11 --region ap-south-1
