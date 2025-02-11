# 將資料格式轉換為 FHIR 格式並透過 API 傳值

1. **使用公用伺服器傳值**

   將資料傳入以下 URL：
   ```
   http://hapi.fhir.org/baseR4/Patient
   ```

2. **以 Patient 資料表為例**

   - 其他資料表需根據 FHIR 規定格式傳送指定值。
   - 確保資料符合 FHIR 標準，以便正確傳輸和解析。

> **注意：** FHIR（Fast Healthcare Interoperability Resources）是一種用於交換電子健康記錄的標準，確保資料的互操作性和一致性。
