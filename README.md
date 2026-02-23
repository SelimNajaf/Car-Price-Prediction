# Car Price Predictor: End-to-End ML Pipeline

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Scikit-Learn](https://img.shields.io/badge/scikit--learn-%23F7931E.svg?style=for-the-badge&logo=scikit-learn&logoColor=white)
![License](https://img.shields.io/badge/license-MIT-green?style=for-the-badge)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen?style=for-the-badge)

## 📖 Project Overview
The **Car Price Predictor** is a complete, end-to-end Machine Learning solution designed to estimate the market value of used cars. This project demonstrates the full data science lifecycle: from synthetic data generation and preprocessing to model evaluation and eventual deployment as an interactive web application. 

By leveraging a robust `scikit-learn` pipeline and a sleek `Streamlit` interface, this project allows users to input car specifications and instantly receive an accurate price prediction formatted in Azerbaijani Manat (AZN).

## ✨ Key Features
*   **Automated Data Generation:** Programmatically generates a highly realistic synthetic dataset of 1,000 cars based on a logical pricing formula (factoring in brand premium, age, engine size, mileage, and fuel type).
*   **Robust Preprocessing:** Utilizes `ColumnTransformer` to seamlessly handle both numerical scaling (`StandardScaler`) and categorical encoding (`OneHotEncoder`).
*   **Model Benchmarking:** Trains and evaluates both `LinearRegression` and `RandomForestRegressor` to select the optimal algorithm for the dataset.
*   **Unified ML Pipeline:** Packages data preprocessing and the predictive model into a single serialized `.joblib` pipeline, preventing data leakage and simplifying deployment.
*   **Interactive Web App:** A user-friendly Streamlit application featuring sliders and dropdowns for intuitive price estimation.

## 📊 Data Description
Since real-world data can be messy or proprietary, this project auto-generates a synthetic dataset (`cars_data.csv`) of 1,000 samples. The pricing logic mimics real-world automotive depreciation and premium scaling:
*   **Features:**
    *   `brand`: Toyota, BMW, Mercedes, Hyundai, Kia
    *   `year`: Manufacturing year (2005 - 2024)
    *   `engine`: Engine volume in Liters (1.6 to 4.4)
    *   `mileage`: Odometer reading in kilometers (0 - 300,000)
    *   `fuel`: Petrol or Diesel
*   **Target:** `price` (Calculated using a hidden base formula + random real-world variance noise).

## 🛠️ Project Architecture

```text
├── car_price_prediction.ipynb  # Data generation & model training script
├── app.py                                     # Streamlit web application interface
├── cars_data.csv                              # Generated synthetic dataset (Output)
├── car_price_prediction.joblib                # Serialized Scikit-Learn pipeline (Output)
└── README.md                                  # Project documentation
```

## 🚀 Installation & Prerequisites

To run this project locally, ensure you have Python 3.8+ installed. 

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SelimNajaf/Car-Price-Prediction/tree/main]
   cd [Insert Repository Directory Name]
   ```

2. **Install the required dependencies:**
   It is highly recommended to use a virtual environment.
   ```bash
   pip install numpy pandas scikit-learn joblib streamlit
   ```

## 💻 Usage / How to Run

### Step 1: Generate Data & Train the Model
First, run the data generation and training script. This will create the `cars_data.csv` dataset, train the models, evaluate their accuracy, and export the trained model pipeline as `car_price_prediction.joblib`.

*If using a standard Python script:*
```bash
python train_model.py
```
*(If using Jupyter Notebook, simply execute all cells in the provided notebook).*

### Step 2: Launch the Web Application
Once the `.joblib` model file is generated, you can spin up the Streamlit interface.

```bash
streamlit run app.py
```
This will automatically open a new tab in your default web browser (usually at `http://localhost:8501`) where you can interact with the predictive model.

## 📈 Results / Outputs

During the model evaluation phase, the algorithms achieved the following Mean Absolute Errors (MAE):
*   **Linear Regression MAE:** `1475.25`
*   **Random Forest MAE:** `2529.87`

**Why did Linear Regression win?** 
Because the underlying synthetic dataset was generated using a strictly linear additive formula, the Linear Regression model easily captured the exact mathematical weights, significantly outperforming the tree-based Random Forest model.

**App Output:**
Users interacting with the Streamlit app will experience a clean interface and receive a dynamically calculated price output, for example: 
> 💰 **The estimated price of this car is approximately 24,500 AZN**

## 🤝 Contributing
Contributions are welcome! If you'd like to improve the prediction logic, add new features, or integrate a real-world dataset:
1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact
**Selim Najaf**

*   **LinkedIn:** [linkedin.com/in/selimnajaf-data-analyst](https://www.linkedin.com/in/selimnajaf/)
*   **GitHub:** [github.com/SelimNajaf](https://github.com/SelimNajaf)

*If you found this project helpful, please consider giving it a ⭐ on GitHub!*
