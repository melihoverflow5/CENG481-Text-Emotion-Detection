from flask import Flask, request, jsonify
from transformers import AutoConfig, AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn as nn
import torch.nn.functional as F
from safetensors.torch import load_file

app = Flask(__name__)

label_map = {0: "sadness", 1: "joy", 2: "love", 3: "anger", 4: "fear", 5: "surprise"}
dropout_rate = 0.49034896247785176
checkpoint = "model"  # folder path

# Load config, tokenizer, model
config = AutoConfig.from_pretrained(checkpoint, num_labels=6)
tokenizer = AutoTokenizer.from_pretrained(checkpoint)
model = AutoModelForSequenceClassification.from_config(config)

# Replace classifier head
model.classifier = nn.Sequential(
    nn.Dropout(dropout_rate),
    nn.Linear(config.hidden_size, 256),
    nn.ReLU(),
    nn.Dropout(dropout_rate),
    nn.Linear(256, 6)
)

# Load weights
state_dict = load_file(f"{checkpoint}/model.safetensors")
model.load_state_dict(state_dict)
model.eval()

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.json
    text = data.get("text", "")
    if not text:
        return jsonify({"error": "No input text provided"}), 400

    # Tokenize input text
    inputs = tokenizer(text, return_tensors="pt", padding="max_length", truncation=True, max_length=128).to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        logits = outputs.logits

    # Softmax probabilities
    probs = F.softmax(logits, dim=-1).cpu().numpy().flatten()
    pred_idx = int(probs.argmax())
    pred_label = label_map[pred_idx]

    return jsonify({
        "input": text,
        "predicted_label": pred_label,
        "predicted_index": pred_idx,
        "label_probabilities": {label_map[i]: float(probs[i]) for i in range(len(probs))}
    })

if __name__ == "__main__":
    app.run(debug=True)
