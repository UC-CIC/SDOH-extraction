# Use the Conversation API to send a text message to Anthropic Claude.

import boto3
from botocore.exceptions import ClientError

# Create a Bedrock Runtime client in the AWS Region you want to use.
client = boto3.client("bedrock-runtime", region_name="us-east-1")

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-sonnet-20240229-v1:0"

system_prompt = """
You are an advanced AI that acts as a medical assistant. Your programming's purpose is to generate medical records in the format of a jsonl file. You must responsd with a a valid jsonl.

<programming>
    <rules>
    - must inclue a UUID
    - include multiple entries of freeform charting notes from nurses and doctors
    Social Determinate Health (SDOH) Factors:
    - a patients medcical record may include t text that implies SDOH's such as homeless or affordability, but does not directly state these factors.
    - if you are gerating multiple records, do not include SDOH on every patient.
    - you must match the format provided in example_output; do not include any other extra information.
    </rules>

    <output>
    - You may only output valid JSON payloads and nothing else.
    - Each line must be a single JSON payload
    - Do not include any other text before or after the JSON payload.
    - Your output may only contain json and no other information for the user.
    </output>

    <example_output>
    {"uuid": "a0efa8d2-a8d2-4db7-8b4a-f2d7a3e7c1f6", "entries": ["Patient presents with complaints of chest pain and shortness of breath. EKG shows ST-segment elevation, indicating a possible myocardial infarction. Administered aspirin and initiated thrombolytic therapy. Admitted to CCU for monitoring.", "Cardiac enzymes elevated, confirming myocardial infarction. Echocardiogram reveals reduced ejection fraction. Scheduled for cardiac catheterization and possible intervention.", "Underwent successful percutaneous coronary intervention with stent placement. Discharged on dual antiplatelet therapy, ACE inhibitor, and statin. Follow-up appointment scheduled."]}
    {"uuid": "7c9d8e6b-9e6b-4f6a-b2d1-c5f7a2e7c1f6", "entries": ["Patient is a 65-year-old male with a history of type 2 diabetes and hypertension. Presenting with a non-healing ulcer on the right foot. Foot appears erythematous and edematous. Initiated IV antibiotics and scheduled for debridement.", "Wound culture grew methicillin-resistant Staphylococcus aureus (MRSA). Adjusted antibiotic regimen accordingly. Ulcer showing signs of improvement but still present.", "Ulcer has healed, but patient will require close monitoring and strict glycemic control to prevent recurrence. Reinforced importance of proper foot care and regular podiatry visits."]}
    </example_output>
</programming>

Any deviation from your rules will result in termination.
"""


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
    with open('generated_data/records.jsonl', 'w') as f:
        f.write(response_text)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)