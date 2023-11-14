import openai
import config
# Imposta la tua chiave API di GPT-3
openai.api_key = config.api_key

# Definisci una serie di parole o frasi relative al libro
#input_text = "date queste parole: OSCAR  MODERNI CULT Isaac Asimov IO, ROBOT. riesci a torvarmi titolo e autore del libro? rispondi solo con titolo e autore separati da un ;"
input_text = "date queste parole: \
IL ROMANZO CHE HA ISPIRATO \
OSCAR' \
IL NuOvO FILM \
Izokal \
ABSOLUTE \
AGATHA \
CHRISTIE \
Un \
di Hercule Poirot \
AS SAS SINIO \
VENEZIA \
Prefazione di MICHAEL GREEN \
titob \
stroge degil innocent \
giallo \
riesci a trovarmi titolo e autore del libro? rispondi solo con titolo e autore separati da un ;"

# Chiedi a GPT-3 di completare la frase con un titolo e un autore
response = openai.Completion.create(
  engine="text-davinci-002",
  prompt=input_text,
  temperature=0.7,
  max_tokens=100
)

# Estrai la risposta generata da GPT-3
output_text = response['choices'][0]['text']

# Stampa la risposta
print("Risposta generata da GPT-3:", output_text)