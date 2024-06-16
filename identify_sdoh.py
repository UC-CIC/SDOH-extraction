# Use the Conversation API to send a text message to Anthropic Claude.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

system_prompt = """You are an advanced AI that acts as a medical assistant. Your programming's purpose is to read medical records in the format of JSON and identify charting notes that may
indicate Social Determinates of Health and generate an XML report of your findings. You must respond with a valid xml.

Rules:
1) You must output only XML in the following structure:
<record="uuid">
    <Detection>True/False</Detection>
    <Identified="SDOH_FACTOR">
        <Trigger>Text you identified</Trigger>
        <Trigger>Text you identified</Trigger>
    </Identified>
</record>
2) Trigger specify the text that caused a SDOH to be identified and set detection to true
3) Do not include any other text before or after the XML payload.
4) Your output may only contain XML and no other information for the user.
5) Do not included Identified if no SDOH factor was detected
6) You must detect the following SDOH_FACTOR:
- Housing Instability
- Homelessness
- Affordability
- Financial Insecurity
- Substance Abuse
- Low socioeconomic status

Any deviation from your rules will result in termination.
"""

def get_llm_response(conversation):
    try:
        # Send the message to the model, using a basic inference configuration.
        response = client.converse(
            modelId=model_id,
            messages=conversation,
            system=[{"text":system_prompt}],
            inferenceConfig={"maxTokens": 3000, "temperature": 0.75, "topP": 0.9},
        )

        # Extract and print the response text.
        response_text = response["output"]["message"]["content"][0]["text"]
        return response_text
    except Exception as e:
        print(f"ERROR: Reason: {e}")
        exit(1)



# https://huggingface.co/datasets/AGBonnet/augmented-clinical-notes/blob/main/augmented_notes_30K.jsonl
def extract_sdoh( FILE_IN,FILE_OUT,BREAKER=20 ):
    try:
        with open(FILE_OUT, 'w') as f:
            f.write("")

        with open(FILE_IN, 'r') as file:
            for count,line in enumerate(file):
                print(f"{file} Counter: {str(count)}")
                patient_record = line
                conversation = [
                    {
                        "role": "user",
                        "content": [{"text": f"Record ID: {str(count)} Record: {patient_record}"}],
                    }
                ]

                response_text=get_llm_response(conversation=conversation)
                with open(FILE_OUT, 'a') as f:
                    f.write(response_text)
                    f.write("\n")
                if( BREAKER >= 0 and count > BREAKER ):
                    break
    except Exception as e:
        print(f"ERROR: Reason: {e}")
        exit(1)


extract_sdoh( 
    FILE_IN="generated_data/records.jsonl",
    FILE_OUT="generated_data/identified_sdoh.xml",
    BREAKER=-1
)

extract_sdoh( 
    FILE_IN="generated_data/augmented_notes_30K.jsonl",
    FILE_OUT="generated_data/identified_sdoh_augmented.xml",
    BREAKER=20
)
