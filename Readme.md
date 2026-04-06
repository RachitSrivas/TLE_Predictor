# 🚀 AI TLE Predictor

A Machine Learning-powered tool designed to help developers and competitive programmers **proactively avoid Time Limit Exceeded (TLE)** errors.

This project leverages a **custom-built Deep Dense Neural Network** trained on a proprietary synthetic dataset (750 rows) to **predict execution time (in seconds)** before running the code.

---

## 📌 Overview

In competitive programming and real-world development, inefficient algorithms can lead to **TLE (Time Limit Exceeded)** errors. This project solves that problem by estimating execution time based on:

* Input size (**N**)
* Algorithmic time complexity (**Big-O notation**)

The model predicts how long your code will take — helping you optimize before submission.

---

## 🧠 Key Features

* 🔹 **Custom Neural Architecture**
  Built from scratch using a Deep Dense Neural Network for precise predictions.

* 🔹 **Algorithmic Forecasting**
  Supports a wide range of time complexities from:

  * `O(1)`
  * `O(log N)`
  * `O(N)`
  * `O(N log N)`
  * `O(N²)`

* 🔹 **Execution Time Prediction**
  Outputs estimated runtime in **seconds** before actual execution.

* 🔹 **Live Deployment**
  Fully functional web app built using **Streamlit** with an intuitive UI.

---

## 🛠️ Tech Stack

* **Python**
* **TensorFlow / Keras**
* **NumPy / Pandas**
* **Streamlit**

---

## 📊 Model Details

* Model Type: Deep Dense Neural Network
* Dataset: Synthetic dataset (750 rows)
* Input Features:

  * Input size (N)
  * Encoded algorithm complexity
* Output:

  * Predicted execution time (in seconds)

---

## 🌐 Live Application

The model is deployed using Streamlit, allowing users to:

* Enter input size (N)
* Select algorithm complexity
* Instantly get predicted execution time

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/ai-tle-predictor.git

# Navigate to project folder
cd ai-tle-predictor

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit app
streamlit run app.py
```

---

## 📈 Use Cases

* Competitive Programming (Codeforces, LeetCode, etc.)
* Algorithm Optimization
* Performance Analysis
* Interview Preparation

---

## 🎯 Future Improvements

* Expand dataset for higher accuracy
* Support more complex time complexities (e.g., exponential)
* Integrate real benchmark datasets
* Add visualization for time growth trends

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📬 Contact

For queries or collaborations, feel free to connect!

---

⭐ If you found this project helpful, don’t forget to give it a star!
