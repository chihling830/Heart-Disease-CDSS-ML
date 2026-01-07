# 心臟疾病臨床決策輔助系統（CDSS）
### 可解釋機器學習於醫療風險評估之應用

## 專案概述
本專案建構一套以**可解釋機器學習（Explainable Machine Learning）**為核心的**心臟疾病臨床決策輔助系統（Clinical Decision Support System, CDSS）**。

除模型預測效能外，本研究重點在於：
- **特徵重要性（Feature Importance）分析**
- **SHAP（SHapley Additive Explanations）可解釋性方法**
- 將模型輸出轉化為**具實務意義的臨床判斷依據**

本專案嘗試銜接**學術研究與醫療實務應用**，使機器學習模型成為可信賴的決策輔助工具，而非黑盒預測器。

---

## 研究動機與臨床情境
心臟疾病診斷涉及多項交互影響的風險因子，如血壓、膽固醇、心電圖結果及運動誘發症狀，臨床判斷高度仰賴醫師經驗。

即使機器學習模型具備良好預測能力，**缺乏可解釋性仍是臨床應用的主要障礙**。

本研究透過：
- 多模型比較分析
- 系統性特徵重要性檢視
- SHAP 解釋個體與整體預測結果
- 將解釋結果轉換為 CDSS 情境下的臨床建議

以提升模型於實務醫療決策中的可行性。

---

## 資料集
- **來源**：UCI Machine Learning Repository – Heart Disease Cleveland Dataset
- **資料筆數**：304 筆（清理後 297 筆）
- **特徵數量**：14 項臨床指標
- **目標變數**：是否罹患心臟疾病（二元分類）

主要特徵包含：
- 年齡、靜止血壓、膽固醇
- 最大運動心率（thalach）
- ST 段壓低（oldpeak）
- 胸痛類型（cp）
- 心肌灌流狀態（thal）
- 主要血管數量（ca）

---

## 研究方法與流程

### 資料前處理
- 缺失值處理
- 類別變數 One-Hot Encoding
- 數值特徵標準化（StandardScaler）
- Stratified 10-fold Cross-Validation

### 模型比較
- 邏輯斯回歸（Logistic Regression）
- 決策樹（Decision Tree）
- 隨機森林（Random Forest）
- 支援向量機（SVM：Linear / RBF）
- XGBoost

### 評估指標
- Accuracy
- Precision / Recall
- F1-score
- ROC-AUC
- Confusion Matrix

---

## 特徵重要性與可解釋性分析（核心貢獻）

### 線性模型（Logistic Regression、Linear SVM）
主要正向風險因子：
- **oldpeak**（運動後 ST 段壓低）
- **trestbps**（靜止血壓）
- **chol**（膽固醇）

保護性因子：
- **thalach**（最大運動心率）
- **age**（年齡）

此類模型適合用於**風險方向性與臨床邏輯解釋**。

---

### 樹狀模型（Random Forest、XGBoost）
高重要性特徵包含：
- **thal**（心肌灌流狀態）
- **cp**（胸痛類型）
- **ca**（主要血管狹窄數）
- **exang**（運動誘發心絞痛）

能有效捕捉**非線性與複合風險關係**。

---

### SHAP 分析
SHAP 用於：
- 整體特徵重要性分析
- 個別病患預測解釋
- 視覺化特徵對預測結果的正負影響


---

## 從可解釋 AI 到臨床決策輔助
本研究進一步將模型解釋結果轉化為健檢與臨床複查建議：

- 協助辨識傳統指標模糊但具高風險之病患
- 明確指出影響單一預測結果的關鍵生理因子
- 支援醫師進行後續檢查與風險分級決策

