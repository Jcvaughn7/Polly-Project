name: Run Polly and Upload to S3

on:
  push:
    branches:
      - main
  pull_request:
    branches:
      - main

jobs:
  polly-task:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Install dependencies
        run: |
          pip install --upgrade pip
          pip install boto3 botocore

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: us-east-1

      - name: Run Polly S3 Script
        run: |
          python your_script.py  # replace with the actual filename

      - name: Upload MP3 output
        uses: actions/upload-artifact@v4
        with:
          name: polly-audio
          path: polly-audio/beta.mp3
