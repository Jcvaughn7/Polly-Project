import boto3
import os

base_dir = os.getcwd()  # Points to the repo root when run in GitHub Actions or locally
input_file = os.path.join(base_dir, "speech.txt")
output_file = os.path.join(base_dir, "output.mp3")


bucket_name = 'mypollyprojectbucketjcv'
s3_key = "polly-audio/output.mp3"
region = 'us-east-1'

with open(input_file, 'r') as f:
    text_to_speak = f.read().strip()

polly = boto3.client('polly', region_name=region)

response = polly.synthesize_speech(
    Text=text_to_speak,
    OutputFormat='mp3',
    VoiceId='Joanna',
    Engine='neural'
)

if "AudioStream" in response:
    with open(output_file, 'wb') as f:
        f.write(response['AudioStream'].read())
    print(f"✅ MP3 saved at: {output_file}")
else:
    print("❌ Polly response did not include AudioStream.")
    exit(1)

s3 = boto3.client('s3', region_name=region)

try:
    s3.upload_file(output_file, bucket_name, s3_key)
    print(f"✅ Uploaded to S3: s3://{bucket_name}/{s3_key}")
except Exception as e:
    print("❌ Failed to upload to S3:", e)
