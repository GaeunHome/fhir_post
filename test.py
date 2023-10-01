import json
import requests

def convert_to_fhir(data):
    # 表單資料轉換為FHIR資源的程式碼
    fhir_data = {
        "resourceType": "Patient",
        "identifier": [ {
            "value": data["identifier"]
        } ],
        "name": [
            {
                "family": data["lastName"],
                "given": data["firstName"]
            }
        ],
        "gender": data["gender"],
        "birthDate": data["birthDate"],
        "address": [
            {
                "use": "home",
                "line": data["addressLine"],
                "city": data["city"],
                "state": data["state"],
                "postalCode": data["postalCode"]
            }
        ],
        "contact": [
            {
                "relationship": [
                    {
                        "coding": [
                            {
                                "system": "http://terminology.hl7.org/CodeSystem/v2-0131",
                                "code": "C",
                                "display": "Emergency contact"
                            }
                        ]
                    }
                ],
                "name": {
                    "family": data["contactLastName"],
                    "given": data["contactFirstName"],
                    "text": data["contactFullName"]
                },
                "telecom": [
                    {
                        "system": "phone",
                        "value": data["contactPhone"]
                    }
                ]
            }
        ]
    }
    return fhir_data

def send_fhir_data(fhir_data):
    # 將FHIR格式的資料傳送出去
    # 替換成實際的FHIR服務端點URL
    # 測試用伺服器
    # 參考https://hapi.fhir.org/
    url = "http://hapi.fhir.org/baseR4/Patient"
    headers = {"Content-Type": "application/json"}
    response = requests.post(url, headers=headers, data=json.dumps(fhir_data))
    if response.status_code == 201:
        print("資料成功傳送！")
    else:
        print("資料傳送失敗。錯誤碼：", response.status_code)

# 假設表單有以下欄位
form_data = {
    "identifier": "PAC02",
    "firstName": "四",
    "lastName": "李",
    "gender": "female",
    "birthDate": "1980-01-01",
    "addressLine": ["123 Main St"],
    "city": "City",
    "state": "State",
    "postalCode": "12345",
    "contactFirstName": "五",
    "contactLastName": "王",
    "contactFullName": "王五",
    "contactPhone": "9876543210"
}
# 將表單資料轉換成FHIR格式
fhir_data = convert_to_fhir(form_data)
# 傳送FHIR格式的資料
send_fhir_data(fhir_data)
# 輸出FHIR格式的資料
print(json.dumps(fhir_data, indent=4))
