import spacy
from collections import Counter
import pandas as pd

nlp = spacy.load("spacy_model")

with open("buzzwords.txt") as file:
    content = file.read().strip().split("\n")
    buzzwords = set(content)

with open("action_verbs.txt") as file:
    content = file.read().strip().split("\n")
    action_verbs = set(content)


def get_skills(text: str):
    doc = nlp(text)
    skills = [ent.text.capitalize() for ent in doc.ents if ent.label_ == "SKILL"]
    count = Counter(skills)
    data = []
    for i, item in enumerate(count.items(), start=1):
        skill, val = item
        data.append([i, skill, val])
    return pd.DataFrame(data, columns=["ID", "Skill", "Frequency"])

def get_buzzwords(text: str):
    words = set()
    for word in buzzwords:
        if word.lower() in text.lower():
            words.add(word)
    return words

def get_action_verbs(text: str):
    words = set()
    for word in action_verbs:
        if word.lower() in text.lower():
            words.add(word)
    return words

