# 🎭 Emotion Detection in Text using DeBERTa-v3

This project uses a fine-tuned DeBERTa-v3-large model to detect emotions in text. It supports 6 emotion categories: **sadness, joy, love, anger, fear,** and **surprise**. The model is served via a Flask API and accessed through a user-friendly Streamlit interface.

---

## 📦 Features

- ⚡️ Fast emotion detection using a custom fine-tuned DeBERTa model
- 🌐 Flask REST API for backend prediction
- 🖥️ Streamlit app for interactive frontend visualization
- 📊 Emotion probabilities with bar charts
- 🧠 Pretrained model hosted externally (due to file size)

---

## 📁 Project Structure

```
CENG481-Text-Emotion-Detection/
├── app.py               # Flask API
├── streamlit_app.py     # Streamlit frontend
├── run.py               # Runs both Flask and Streamlit
├── requirements.txt     # Python dependencies
├── .gitignore
├── README.md
```

---

## 💾 Model & Data

Due to GitHub file size limits, the trained model and data are hosted on Google Drive.

**Download from:**  
📁 [Google Drive Folder](https://drive.google.com/drive/folders/1mGK_loCEl-wCkAGF3O-P3GJxm88qjmGG?usp=sharing)

From that folder:
- Navigate to: `results/checkpoint-6750`
- Download the entire folder to your local machine
- Rename the folder to `model` and place it in the root project directory

Your folder structure should now look like:

```
CENG481-Text-Emotion-Detection/
├── model/
│   ├── config.json
│   ├── tokenizer.json
│   ├── tokenizer_config.json
│   ├── model.safetensors
│   └── ...
```

---

## ⚙️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/your-username/CENG481-Text-Emotion-Detection.git
cd CENG481-Text-Emotion-Detection
```

2. **Set up a virtual environment**
```bash
python -m venv .venv
source .venv/bin/activate  # on Windows use `.venv\Scripts\activate`
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download the model**  
   See the [Model & Data](#-model--data) section above.

---

## 🚀 Running the App

Run both the Flask API and Streamlit UI using:

```bash
python run.py
```

- Flask API will start on `http://localhost:5000/predict`
- Streamlit app will open in your browser at `http://localhost:8501`

---

## 📤 API Usage

You can test the prediction endpoint with Postman or cURL:

**POST** `http://localhost:5000/predict`  
**Body:**
```json
{
  "text": "I’m feeling great today!"
}
```

**Response:**
```json
{
  "input": "I’m feeling great today!",
  "predicted_label": "joy",
  "predicted_index": 1,
  "label_probabilities": {
    "sadness": 0.01,
    "joy": 0.95,
    "love": 0.02,
    "anger": 0.005,
    "fear": 0.01,
    "surprise": 0.005
  }
}
```

---

## 🙋‍♂️ Contact

For any issues, feel free to open an [issue](https://github.com/your-username/CENG481-Text-Emotion-Detection/issues)

---

## 📝 License

This project is licensed under the MIT License.
