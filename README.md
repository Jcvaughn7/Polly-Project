Polly Audio Conversion Project

This project uses **GitHub Actions** workflows and **AWS Polly** to convert text files into speech audio files (`.mp3`) and upload them to an AWS S3 bucket.



 Workflow Overview

 1. `on_pull_request.yml`  
 Triggers:** On pull requests targeting the `main` branch  
 Function:** Runs the Polly synthesis Python script, then uploads the generated audio as `beta.mp3` to the S3 bucket under the `polly-audio/` folder  
 Purpose:** To test audio changes during development without affecting production files  

 2. `on_merge.yml`  
 Triggers:** On push events to the `main` branch (after pull request merges)  
 Function:** Runs the Polly synthesis Python script, then uploads the generated audio as `prod.mp3` to the S3 bucket under the `polly-audio/` folder  
 Purpose:** To deploy stable, production-ready audio files  



 How to Use

1. Make changes** to `speech.txt` or other relevant files.
2. Create a Pull Request** against the `main` branch.
3. The `on_pull_request` workflow** will run, generating a beta audio file (`beta.mp3`).
4. After approval and merging, the **`on_merge` workflow** runs, generating the production audio file (`prod.mp3`).



 Requirements

 Python 3.x  
 AWS CLI configured with proper IAM permissions  
 AWS credentials stored as GitHub secrets:  
  - `AWS_ACCESS_KEY_ID`  
  - `AWS_SECRET_ACCESS_KEY`



 Files of Note
 `Synthesize.py` — Python script using AWS Polly to convert text to speech  
 `speech.txt` — Input text file for speech synthesis  
 `.github/workflows/on_pull_request.yml` — GitHub Actions workflow for pull requests  
 `.github/workflows/on_merge.yml` — GitHub Actions workflow for merges  


 AWS S3 Bucket Structure

