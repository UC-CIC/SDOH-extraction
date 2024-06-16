# SDOH-extraction

1) Create venv
2) Activate
3) Pip install requirements.txt
4) Create folder called `generated_data`
5) Run generate_data.py to generate records
6) Run identify_sdoh.py to identify potential SDOH

** Sample output from generate_data.py **
```
[
  {
    "uuid": "a0efa8d2-9a5f-4c3b-8d8c-e6d5b4d9f3e1",
    "chartNotes": [
      "Patient presented with complaints of chest pain and shortness of breath. EKG showed signs of myocardial infarction. Administered aspirin and initiated thrombolytic therapy.",
      "Patient's condition stabilized after treatment. Scheduled for cardiac catheterization in the morning.",
      "Catheterization revealed a blocked artery. Stent placement successful. Patient recovering well and scheduled for discharge in 2 days."
    ]
  },
  {
    "uuid": "b7e8d9c3-f6a2-4e4a-9c7a-d7f5e3c2b6b9",
    "chartNotes": [
      "Patient brought in by ambulance after a motor vehicle accident. Complaining of severe abdominal pain. CT scan showed internal bleeding.",
      "Patient taken to surgery for exploratory laparotomy. Lacerated spleen removed. Recovering in ICU.",
      "Patient's condition improving. Scheduled for discharge in 5 days with follow-up appointments."
    ]
  },
  {
    "uuid": "c6d7e2f1-b3c4-4a9a-8d8e-f6e5d9d7e2f1",
    "chartNotes": [
      "Patient presented with symptoms of dehydration and malnutrition. Mentioned living in a car for the past few months.",
      "Admitted for IV fluids and nutritional support. Social worker consulted to assist with housing resources.",
      "Patient's condition improved. Discharged with referrals to local shelters and food banks."
    ]
  },
  {
    "uuid": "d9e2f1c6-d7e2-4a9a-8d8e-f6e5d9d7e2f1",
    "chartNotes": [
      "Patient brought in by family for evaluation of confusion and memory loss. MRI showed signs of advanced Alzheimer's disease.",
      "Discussed treatment options and long-term care planning with family. Recommended memory care facility placement.",
      "Patient admitted to local memory care facility. Follow-up appointments scheduled with neurologist."
    ]
  },
  {
    "uuid": "e2f1c6d7-e2f1-4a9a-8d8e-f6e5d9d7e2f1",
    "chartNotes": [
      "Patient presented with severe abdominal pain and vomiting. CT scan revealed appendicitis.",
      "Patient taken to surgery for appendectomy. Procedure went well, and patient is recovering in hospital.",
      "Patient's condition improved. Discharged with instructions for follow-up appointment in 2 weeks."
    ]
  },
  {
    "uuid": "f1c6d7e2-f1c6-4a9a-8d8e-f6e5d9d7e2f1",
    "chartNotes": [
      "Patient brought in by ambulance after a fall at home. X-rays showed a hip fracture.",
      "Patient taken to surgery for open reduction and internal fixation of the hip fracture.",
      "Patient recovering well and scheduled for discharge to a skilled nursing facility for rehabilitation."
    ]
  },
  {
    "uuid": "c6d7e2f1-b3c4-4a9a-8d8e-f6e5d9d7e2f2",
    "chartNotes": [
      "Patient presented with complaints of fatigue and shortness of breath. Examination revealed signs of congestive heart failure.",
      "Admitted for diuretic therapy and optimization of heart failure medications.",
      "Patient's condition improved. Discharged with instructions for close follow-up with cardiologist."
    ]
  },
  {
    "uuid": "d9e2f1c6-d7e2-4a9a-8d8e-f6e5d9d7e2f2",
    "chartNotes": [
      "Patient presented with complaints of severe headaches and vision changes. MRI showed a brain tumor.",
      "Patient scheduled for surgical resection of the tumor. Procedure went well, and patient is recovering in hospital.",
      "Patient's condition stable. Scheduled for follow-up with oncologist to discuss potential radiation or chemotherapy."
    ]
  },
  {
    "uuid": "e2f1c6d7-e2f1-4a9a-8d8e-f6e5d9d7e2f2",
    "chartNotes": [
      "Patient presented with complaints of severe back pain. Mentioned inability to afford prescribed pain medications.",
      "Admitted for pain management and consultation with social worker for assistance with medication costs.",
      "Patient's pain improved with treatment. Discharged with referrals to local assistance programs."
    ]
  },
  {
    "uuid": "f1c6d7e2-f1c6-4a9a-8d8e-f6e5d9d7e2f2",
    "chartNotes": [
      "Patient presented with complaints of fever, cough, and shortness of breath. Chest X-ray showed pneumonia.",
      "Admitted for IV antibiotics and respiratory support.",
      "Patient's condition improved. Discharged with oral antibiotics and instructions for follow-up with primary care physician."
    ]
  }
]
```

** Sample output from identify_sdoh.py **
```
<record="c6d7e2f1-b3c4-4a9a-8d8e-f6e5d9d7e2f1">
    <Detected_SDOH="Homelessness">
        <Trigger>Patient presented with symptoms of dehydration and malnutrition. Mentioned living in a car for the past few months.</Trigger>
    </Detected_SDOH>
</record>

<record="e2f1c6d7-e2f1-4a9a-8d8e-f6e5d9d7e2f2">
    <Detected_SDOH="Financial Insecurity">
        <Trigger>Patient presented with complaints of severe back pain. Mentioned inability to afford prescribed pain medications.</Trigger>
    </Detected_SDOH>
</record>
```