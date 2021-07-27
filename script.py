from transformers import pipeline
from tika import parser
from googletrans import Translator

translator = Translator()

summarization = pipeline("summarization")
original_text = parser.from_file("./ML.pdf")
original_text = original_text["content"]

original_text = original_text[:1024]


summary_text = summarization(original_text)[0]["summary_text"]
result = translator.translate(summary_text, src="en", dest="de")

with open("summary.txt", "w") as text_file:
    text_file.write(result.text)
