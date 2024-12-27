
# Project Structure:
#
# my-lambda-project/
# ├── src/
# │   └── app.py
# ├── template.yaml
# ├── .circleci/
# │   └── config.yml
# └── requirements.txt

# src/app.py
def lambda_handler(event, context):
    return {
        'statusCode': 200,
        'body': {
            'message': 'Hello from Lambda!'
        }
    }