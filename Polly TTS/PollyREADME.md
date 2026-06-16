## Polly

Simple voices that sound great!

## Setup

1) Go to the AWS homepage and click create account. Choose the free account plan.

2) In the top search bar, type IAM (Identity and Access Management) and click it. Name the user whatever, then under permissions, choose Attach policies directly. Search for AmazonPollyFullAccess, check the box next to it, and finish creating the user.

3) Click on your username in the IAM dashboard, Look for the security credentials tabm, scroll down to access keys and click create access key. Copy the Access key ID and put it into your environment variables with the name "AWS_ACCESS_KEY". Do the same with your secret with the name "AWS_SECRET"

## Usage

make sure to run run "pip install -r requirements.txt" in the terminal to install all the modules.

once you've installed the requirements, copy the azure file into a project of your choice.
then you can use
```python
from Polly_Text_to_speech import speak

speak("X")
```

booyah pal