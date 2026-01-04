# Expiry-Aware-Grocery-Inventory-Management

1) What is this project doing?

This project monitors grocery items and determines their expiry condition by analyzing expiry dates from a CSV file.

It helps to:

-Identify Safe products
-Detect Near-expiry products
-Find Expired products
-Reduce food wastage
-Improve inventory management
Project Domain

2) What type of project is this?

Primary Domain:
🔹 Artificial Intelligence (AI)
🔹 Machine Learning (ML)
🔹 Data Analytics

✅ Application Domain

-Smart Inventory Management
-Retail & Grocery Stores
-Food Safety Systems
-Sustainability & Waste Reduction

3) What role does AI / ML play here?
   
🧠 AI Role

-Automates decision making
-Eliminates manual checking
-Smart classification of inventory

🤖 ML Role (Future Enhancement)

-Your trained ML model can:
-Predict expiry risk before actual expiry
-Suggest discounts
-Recommend stock rotation
-Improve supply planning

4) What algorithm is used in your project?

Your project uses TWO methods:

1️⃣ Rule-Based Algorithm (Main Working System)
👉 This is the main algorithm actually running in your web application.
🔸 How it works (Simple):

-The system checks the expiry date
-It calculates days left from today
-Based on days left, it decides the status

🔸 Logic:

If days ≤ 0 → ❌ Expired

If days ≤ 30 → ⚠ Near Expiry

If days > 30 → ✅ Safe

📌 This is called a Rule-Based Classification Algorithm.

2️⃣ Random Forest Algorithm (Machine Learning – Advanced Part)
👉 Used in your ML model (model.py)
🔸 What it does:

-Learns from past grocery data
-Predicts expiry risk (Low / Medium / High)

🔸 Inputs:

-Days to expiry
-Stock quantity
-Sales rate
-Storage type

🔸 Why Random Forest?

-Combines many decision trees
-Gives better accuracy
-Reduces wrong prediction
