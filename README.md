🌱 Crop Health Prediction Using Random Forest

📌 Project Overview

The Crop Health Prediction project is a Machine Learning application designed to predict crop health based on the available crop and environmental parameters in the dataset.

The project uses a Random Forest Machine Learning model for prediction and provides an interactive Streamlit web application through which users can enter the required input values and receive a prediction.

This project demonstrates the complete Machine Learning workflow, including:

- Data collection and exploration
- Data preprocessing
- Feature analysis
- Machine Learning model training
- Model evaluation
- Model saving using Joblib
- Prediction through a Streamlit application

---

🎯 Objectives

The main objectives of this project are:

1. To analyze crop-related data.
2. To preprocess the dataset for Machine Learning.
3. To train a Random Forest classification model.
4. To evaluate the trained model.
5. To save the trained model as a ".joblib" file.
6. To develop an interactive Streamlit application.
7. To provide crop health predictions based on user-provided inputs.

---

🛠️ Technologies Used

Programming Language

- Python

Machine Learning

- Scikit-learn
- Random Forest Classifier

Data Processing

- Pandas
- NumPy

Data Visualization

- Matplotlib
- Seaborn

Model Storage

- Joblib

Application

- Streamlit

Development Environment

- Jupyter Notebook

Version Control

- Git
- GitHub
- Git LFS

---

📂 Project Structure

Crop-Prediction-Project/
│
├── Crop Disease Prediction.ipynb
│
├── app.py
│
├── requirements.txt
│
├── Crop Health Random Forest Model.joblib
│
├── Crop Health Random Forest Predictions.csv
│
├── README.md
│
├── .gitignore
│
└── .gitattributes

---

📊 Dataset

The project uses the following CSV file:

Crop Health Random Forest Predictions.csv

The dataset contains the information used for developing and testing the Machine Learning model.

The dataset is loaded using Pandas and processed before being provided to the Machine Learning model.

Example:

import pandas as pd

data = pd.read_csv("Crop Health Random Forest Predictions.csv")

---

🤖 Machine Learning Model

The project uses a Random Forest Classifier.

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to produce a prediction.

The general workflow is:

Dataset
   ↓
Data Preprocessing
   ↓
Feature Selection
   ↓
Train/Test Split
   ↓
Random Forest Model
   ↓
Model Evaluation
   ↓
Save Model
   ↓
Streamlit Application
   ↓
Crop Health Prediction

The trained model is saved using Joblib:

Crop Health Random Forest Model.joblib

The saved model allows the Streamlit application to make predictions without retraining the model every time the application starts.

---

📓 Jupyter Notebook

The file:

Crop Disease Prediction.ipynb

contains the Machine Learning development process.

It includes the relevant steps for:

- Importing libraries
- Loading the dataset
- Exploring the data
- Data preprocessing
- Preparing features and target
- Training the Random Forest model
- Evaluating the model
- Generating predictions
- Saving the trained model

---

🌐 Streamlit Application

The project includes a Streamlit application:

app.py

The application provides an interactive interface for entering the required crop-related information and obtaining a prediction from the trained Random Forest model.

The application loads the saved ".joblib" model and uses it to generate predictions.

---

⚙️ Installation

1. Clone the Repository

Clone this repository using Git:

git clone YOUR_GITHUB_REPOSITORY_URL

Move into the project directory:

cd Crop-Prediction-Project

---

2. Install Required Libraries

Make sure Python is installed.

Install the dependencies using:

py -m pip install -r requirements.txt

---

▶️ Running the Application

Start the Streamlit application using:

py -m streamlit run app.py

After running the command, Streamlit will provide a local URL similar to:

http://localhost:8501

Open the URL in a web browser to access the application.

---

💻 Running the Jupyter Notebook

To open the Jupyter Notebook, run:

jupyter notebook

Then open:

Crop Disease Prediction.ipynb

You can run the notebook cells to explore the dataset, preprocessing steps, model training, and evaluation.

---

📦 Requirements

The required Python libraries are listed in:

requirements.txt

Install all dependencies with:

py -m pip install -r requirements.txt

---

💾 Saved Model

The trained Random Forest model is stored as:

Crop Health Random Forest Model.joblib

The application uses this saved model for prediction.

Example:

import joblib

model = joblib.load("Crop Health Random Forest Model.joblib")

Because the model file is relatively large, Git LFS is used to manage the ".joblib" file in the GitHub repository.

---

🔮 Prediction Process

The application follows this general process:

User Input
    ↓
Input Validation / Preprocessing
    ↓
Trained Random Forest Model
    ↓
Prediction
    ↓
Display Result

The user provides the required input values through the Streamlit interface. These values are processed and passed to the trained model, which generates the corresponding prediction.

---

📈 Model Evaluation

The Machine Learning model is evaluated using appropriate classification metrics during the development process.

The evaluation results can be found in:

Crop Disease Prediction.ipynb

The notebook provides the detailed model-training and evaluation workflow.

---

🔐 Important Notes

- The ".joblib" model file is required for the Streamlit application to make predictions.
- The dataset should be available at the expected file path if the application or notebook requires it.
- The Python dependencies should be installed before running the application.
- The Streamlit application must be running before accessing "localhost:8501".

---

🚀 Future Enhancements

Possible future improvements include:

- Adding more crop and environmental data
- Improving model performance through hyperparameter tuning
- Comparing Random Forest with other Machine Learning algorithms
- Adding additional visualization features
- Improving the Streamlit user interface
- Deploying the application to a cloud platform
- Adding more detailed crop health recommendations

---

👩‍💻 Project Files

File| Description
"Crop Disease Prediction.ipynb"| Jupyter Notebook containing the ML workflow
"app.py"| Streamlit application
"requirements.txt"| Python dependencies
"Crop Health Random Forest Model.joblib"| Trained Random Forest model
"Crop Health Random Forest Predictions.csv"| Project dataset/prediction data
"README.md"| Project documentation
".gitignore"| Files excluded from Git
".gitattributes"| Git LFS configuration

---

📄 License

This project is created for educational and project-development purposes.

---

🙏 Acknowledgement

This project was developed as part of a Machine Learning/Capstone project to demonstrate the application of Machine Learning techniques for crop health prediction.
