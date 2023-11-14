import torch
from transformers import BertTokenizer, BertForSequenceClassification
from torch.utils.data import DataLoader
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tqdm import tqdm

# Carica il tuo dataset e separa in set di addestramento e test
# X contiene le frasi, y contiene le etichette (0 per autore, 1 per titolo)
# Assicurati di adattare questa parte al tuo dataset
X_train, X_test, y_train, y_test = train_test_split(data['frasi'], data['etichette'], test_size=0.2, random_state=42)

# Carica il tokenizer e il modello BERT pre-addestrato
tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
model = BertForSequenceClassification.from_pretrained('bert-base-uncased', num_labels=2)

# Tokenizza e converte i dati in input comprensibili dal modello
def tokenize_data(text_list):
    inputs = tokenizer(text_list, padding=True, truncation=True, return_tensors="pt")
    return inputs

train_inputs = tokenize_data(X_train)
test_inputs = tokenize_data(X_test)

# Converte le etichette in tensori
train_labels = torch.tensor(y_train.values)
test_labels = torch.tensor(y_test.values)

# Crea i DataLoader per l'addestramento e il test
train_dataset = torch.utils.data.TensorDataset(train_inputs['input_ids'], train_inputs['attention_mask'], train_labels)
test_dataset = torch.utils.data.TensorDataset(test_inputs['input_ids'], test_inputs['attention_mask'], test_labels)

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)
test_dataloader = DataLoader(test_dataset, batch_size=8, shuffle=False)

# Specifica i parametri di addestramento
optimizer = torch.optim.AdamW(model.parameters(), lr=2e-5)
criterion = torch.nn.CrossEntropyLoss()

# Addestra il modello
epochs = 3
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
for epoch in range(epochs):
    model.train()
    total_loss = 0
    for batch in tqdm(train_dataloader, desc="Epoch {}".format(epoch + 1)):
        batch = tuple(t.to(device) for t in batch)
        inputs = {'input_ids': batch[0],
                  'attention_mask': batch[1],
                  'labels': batch[2]}
        optimizer.zero_grad()
        outputs = model(**inputs)
        loss = outputs.loss
        loss.backward()
        optimizer.step()
        total_loss += loss.item()

    avg_train_loss = total_loss / len(train_dataloader)
    print("Average training loss: {}".format(avg_train_loss))

# Valuta il modello sul set di test
model.eval()
predictions = []
true_labels = []
with torch.no_grad():
    for batch in tqdm(test_dataloader, desc="Evaluating"):
        batch = tuple(t.to(device) for t in batch)
        inputs = {'input_ids': batch[0],
                  'attention_mask': batch[1],
                  'labels': batch[2]}
        outputs = model(**inputs)
        logits = outputs.logits
        predictions.extend(torch.argmax(logits, dim=1).cpu().numpy())
        true_labels.extend(inputs['labels'].cpu().numpy())

# Calcola l'accuratezza
accuracy = accuracy_score(true_labels, predictions)
print("Accuracy on test set: {:.2f}%".format(accuracy * 100))
