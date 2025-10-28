sample_user_data = {
  "data": {
      "profile": {
        "name": "Prinom",
        "age": 32,
        "gender": "male",
        "height_cm": 165,
        "weight_kg": 68
      },
      "wearable": {
        "ts": "2025-09-09T23:30:00",
        "total_sleep_duration_min": 360,
        "sleep_quality_score": 65,
        "sleep_stages": {
          "deep": 60,
          "rem": 90,
          "light": 210
        },
        "notes": "Late caffeine at 9pm"
      },
      "nutrition": {
        "ts": "2025-09-09T21:00:00",
        "meal": "dinner",
        "calories": 850,
        "caffeine_mg": 80,
        "water_ml": 300
      },
      "detailed_lab_report": {
        "report_date": "14-Apr-2023",
          "test_1": {
            "test_name": "Hemoglobin",
            "value": 15.6,
            "unit": "g/dL",
            "ref_ranges": "13.0-17.0",
            "status": "within"
          },
          "test_2": {
            "test_name": "RBC",
            "value": 5.16,
            "unit": "10^6/cu.mm",
            "ref_ranges": "4.5-5.5",
            "status": "within"
          },
          "test_3": {
            "test_name": "HCT (Hematocrit)",
            "value": 44.6,
            "unit": "%",
            "ref_ranges": "40-50",
            "status": "within"
          },
          "test_4": {
            "test_name": "MCV (Mean Corpuscular Volume)",
            "value": 86.5,
            "unit": "fL",
            "ref_ranges": "83-101",
            "status": "within"
          },
          "test_5": {
            "test_name": "MCH (Mean Corpuscular Hemoglobin)",
            "value": 30.3,
            "unit": "pg",
            "ref_ranges": "27-32",
            "status": "within"
          },
          "test_6": {
            "test_name": "MCHC (Mean Corpuscular Hemoglobin Concentration)",
            "value": 35,
            "unit": "g/dL",
            "ref_ranges": "31.5-34.5",
            "status": "above"
          },
          "test_7": {
            "test_name": "RDW-CV (Red Cell Distribution Width - Coefficient of Variation)",
            "value": 16.2,
            "unit": "%",
            "ref_ranges": "11.6-14",
            "status": "above"
          },
          "test_8": {
            "test_name": "Total Leucocyte Count",
            "value": 6.26,
            "unit": "10^3/μL",
            "ref_ranges": "4-10",
            "status": "within"
          },
          "test_9": {
            "test_name": "Neutrophils",
            "value": 55,
            "unit": "%",
            "ref_ranges": "40-80",
            "status": "within"
          },
          "test_10": {
            "test_name": "Lymphocytes",
            "value": 34,
            "unit": "%",
            "ref_ranges": "20-40",
            "status": "within"
          },
          "test_11": {
            "test_name": "Monocytes",
            "value": 9,
            "unit": "%",
            "ref_ranges": "1-10",
            "status": "within"
          },
          "test_12": {
            "test_name": "Eosinophils",
            "value": 2,
            "unit": "%",
            "ref_ranges": "1-6",
            "status": "within"
          },
          "test_13": {
            "test_name": "Basophils",
            "value": 0,
            "unit": "%",
            "ref_ranges": "0-2",
            "status": "within"
          },
          "test_14": {
            "test_name": "Absolute Neutrophil Count",
            "value": 3.44,
            "unit": "10^3/μL",
            "ref_ranges": "2-7",
            "status": "within"
          },
          "test_15": {
            "test_name": "Absolute Lymphocyte Count",
            "value": 2.13,
            "unit": "10^3/μL",
            "ref_ranges": "1-3",
            "status": "within"
          },
          "test_16": {
            "test_name": "Absolute Monocyte Count",
            "value": 0.56,
            "unit": "10^3/μL",
            "ref_ranges": "0.1-1",
            "status": "within"
          },
          "test_17": {
            "test_name": "Absolute Eosinophil Count",
            "value": 0.13,
            "unit": "10^3/μL",
            "ref_ranges": "0.02-0.5",
            "status": "within"
          },
          "test_18": {
            "test_name": "Absolute Basophil Count",
            "value": 0,
            "unit": "10^3/μL",
            "ref_ranges": "0.02-0.1",
            "status": "below"
          },
          "test_19": {
            "test_name": "Platelet Count",
            "value": 281,
            "unit": "10^3/μL",
            "ref_ranges": "150-410",
            "status": "within"
          },
          "test_20": {
            "test_name": "MPV (Mean Platelet Volume)",
            "value": 10.2,
            "unit": "fL",
            "ref_ranges": "6.5-12",
            "status": "within"
          },
          "test_21": {
            "test_name": "PDW (Platelet Distribution Width)",
            "value": 16,
            "unit": "fL",
            "ref_ranges": "11-22",
            "status": "within"
          },
          "wellness_insight": "Overall, your blood tests show a healthy balance of blood components, which indicates good blood function. Keeping up with regular physical activity such as brisk walking or yoga can help maintain your current health status. Though some values like MCHC and RDW-CV are slightly elevated, ensure you maintain a balanced diet rich in fruits, vegetables, and whole grains to support your blood health. Staying hydrated and managing stress through mindfulness and relaxation techniques might also be beneficial. Continue with regular check-ups to monitor any changes."
        },
      "xray_report": {
        "examination": "X-Ray of Left Leg (AP & Lateral View)",
        "clinical_history": "History of trauma, pain, and swelling in the left leg.",
        "findings": {
          "fracture": "Linear fracture in the mid-shaft of the tibia with mild displacement",
          "soft_tissue": "Surrounding soft tissue swelling present",
          "fibula": "Intact",
          "joints": "No evidence of joint involvement",
          "alignment": "Bony alignment preserved"
        },
        "impression": {
          "impression_1": "Fracture of the mid-shaft of the left tibia with mild displacement",
          "impression_2": "Recommend orthopedic consultation and possible immobilization/casting"
        },
        "radiologist": "Dr. John Doe",
        "date": "2025-09-15"
      },
      "Diabetic_report": {
        "examination": "Diabetes Monitoring Report",
        "clinical_history": "Known case of Type 2 Diabetes Mellitus. Complaints of occasional fatigue and increased thirst.",
        "lab_findings": {
          "fasting_blood_sugar": {
            "value": 148,
            "unit": "mg/dL",
            "reference_range": "70 - 99",
            "status": "High"
          },
          "postprandial_blood_sugar": {
            "value": 210,
            "unit": "mg/dL",
            "reference_range": "Less than 140",
            "status": "High"
          },
          "hba1c": {
            "value": 8.2,
            "unit": "%",
            "reference_range": "4.0 - 5.6",
            "status": "High"
          },
          "cholesterol": {
            "total": {
              "value": 220,
              "unit": "mg/dL",
              "reference_range": "< 200",
              "status": "Borderline High"
            },
            "hdl": {
              "value": 38,
              "unit": "mg/dL",
              "reference_range": "> 40",
              "status": "Low"
            },
            "ldl": {
              "value": 135,
              "unit": "mg/dL",
              "reference_range": "< 100",
              "status": "High"
            }
          }
        },
        "impression": {
          "impression_1": "Uncontrolled Type 2 Diabetes Mellitus (HbA1c 8.2%)",
          "impression_2": "Elevated fasting and postprandial blood sugar levels",
          "impression_3": "Borderline dyslipidemia with low HDL and high LDL"
        },
        "consulting_doctor": "Dr. Sarah Khan (Endocrinologist)",
        "date": "2025-09-15"
      }

  }
}
