# Salary Predictor Model

## Overview

The Salary Predictor Model is a regression application that estimates annual salaries by analyzing user-provided professional and demographic features. Trained using Random Forest Regressor from scikit-learn, the model provides quick and accurate predictions suitable for career planning and HR analytics.

## Features

- Predicts salary based on:
  - Education Level
  - Job Title
  - Industry
  - Location
  - Company Size
  - Years of Experience
  - Certifications
  - Age
  - Working Hours
- Web interface using Flask or Streamlit
- Model pipeline saved with scikit-learn

## Getting Started

1. **Clone the Repository**
    ```
    git clone https://github.com/your-username/salary-predictor.git
    cd salary-predictor
    ```

2. **Install Dependencies**
    ```
    pip install -r requirements.txt
    ```

3. **Run the Application**
    For Flask:
    ```
    python app.py
    ```
    For Streamlit:
    ```
    streamlit run salary_predictor_app.py
    ```

4. **Access the UI**
    - Flask: Visit `http://127.0.0.1:5000/` in your browser
    - Streamlit: See the provided local URL

## Model Details

- Algorithm: Random Forest Regression (scikit-learn)
- Input: Professional & demographic details
- Output: Predicted annual salary

## Usage

- Fill out all user details in the web form.
- Click "Predict Salary" for instant predictions.

## Project Structure

- `salary_predictor_model.joblib` – Trained model file
- `app.py` / `salary_predictor_app.py` – App scripts
- `requirements.txt` – Python dependencies
- `salary_train_5000.csv` – Example dataset

## Contributing

Contributions welcome! Open an issue or submit a pull request.

## License

[MIT](LICENSE)
