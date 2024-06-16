# Use the Conversation API to send a text message to Anthropic Claude.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

system_prompt = """You are to generate a patient medical record which is in the format of EPIC EMR. 
Records:
- must inclue a UUID
- include multiple entries of freeform charting notes from nurses and doctors
Social Determinate Health (SDOH) Factors:
- a patients medcical record may include t text that implies SDOH's such as homeless or affordability, but does not directly state these factors.
- if you are gerating multiple records, do not include SDOH on every patient.
Output:
Your output contain only a valid JSON payload and no markdown formatting."""


# Start a conversation with the user message.
user_message = "Generate ten patient records."
conversation = [
    {
        "role": "user",
        "content": [{"text": user_message}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        system=[{"text":system_prompt}],
        inferenceConfig={"maxTokens": 4096, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    #print(response_text)
    with open('generated_data/records.json', 'w') as f:
        f.write(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)