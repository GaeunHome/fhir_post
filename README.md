# 將資料格式轉換為 FHIR 格式並透過 API 傳值

[![Python](https://img.shields.io/badge/Python-3-3776AB)](https://www.python.org/)
[![FHIR](https://img.shields.io/badge/FHIR-R4-E44D26)](https://www.hl7.org/fhir/)

## 專案描述

將資料轉換為 FHIR 標準格式，並透過 API 傳送至 FHIR 伺服器。

## 使用方式

1. **使用公用伺服器傳值**

   將資料傳入以下 URL：
   ```
   http://hapi.fhir.org/baseR4/Patient
   ```

2. **以 Patient 資料表為例**

   - 其他資料表需根據 FHIR 規定格式傳送指定值。
   - 確保資料符合 FHIR 標準，以便正確傳輸和解析。

> **注意：** FHIR（Fast Healthcare Interoperability Resources）是一種用於交換電子健康記錄的標準，確保資料的互操作性和一致性。

## 專案結構

```
fhir_post/
├── test.py         # FHIR 資料傳送主程式
├── .gitignore
└── README.md
```

## 執行方式

```bash
python test.py
```
