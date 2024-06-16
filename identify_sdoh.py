# Use the Conversation API to send a text message to Anthropic Claude.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

system_prompt = """You are an advanced AI that acts as a medical assistant. Your programming's purpose is to read medical records in the format of JSON and identify charting notes that may
indicate Social Determinates of Health.  For example, there may be a note indicating the patient struggled to sleep as it was cold outside. This could indicate a homelessness SDOH. Ouptut in the format of:
<record="uuid">
    <Detected_SDOH="SDOH">
        <Trigger>Text you identified</Trigger>
        <Trigger>Text you identified</Trigger>
    </Detected_SDOH>
</record>
"""



with open('generated_data/records.json', 'r') as f:
    # Read the contents of the file
    contents = f.read()
    
    # Print the contents of the file
    #print(contents)

# Start a conversation with the user message.
user_message = "Generate a record."
conversation = [
    {
        "role": "user",
        "content": [{"text": contents}],
    }
]

try:
    # Send the message to the model, using a basic inference configuration.
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        system=[{"text":system_prompt}],
        inferenceConfig={"maxTokens": 512, "temperature": 0.5, "topP": 0.9},
    )

    # Extract and print the response text.
    response_text = response["output"]["message"]["content"][0]["text"]
    print(response_text)
    with open('generated_data/identified_sdoh.xml', 'w') as f:
        f.write(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)