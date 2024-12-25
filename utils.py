import spacy
from spacy import displacy
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

# if __name__ == "__main__":
#     text = """We are seeking a dedicated Human Resources Generalist to manage all aspects of the employee lifecycle, from recruitment and onboarding to performance management and employee relations, ensuring a positive employee experience while upholding compliance with employment laws.
# Key Responsibilities:
# Talent Acquisition:
# Develop and execute recruitment strategies to attract top talent across various roles.
# Screen resumes, conduct interviews, and assess candidate qualifications.
# Manage job postings on multiple platforms and maintain applicant tracking systems.
# Coordinate reference checks and pre-employment screenings.
# Onboard new hires, including paperwork processing, orientation, and introductions to company culture.
# Employee Relations:
# Address employee concerns, complaints, and grievances promptly and professionally.
# Facilitate conflict resolution between employees and managers.
# Conduct investigations into workplace issues as needed.
# Provide guidance to managers on disciplinary actions and performance management.
# Performance Management:
# Implement and administer performance review processes.
# Develop performance improvement plans for employees requiring additional support.
# Track employee performance metrics and provide feedback to managers.
# Compensation and Benefits:
# Manage employee benefits programs, including health insurance, retirement plans, and time off policies.
# Process payroll accurately and on time.
# Conduct salary reviews and recommend adjustments as needed.
# Compliance:
# Ensure adherence to all federal, state, and local employment laws.
# Maintain employee records and documentation in compliance with regulations.
# Stay updated on HR trends and legal changes impacting the workplace.
# Training and Development:
# Identify training needs for employees across departments.
# Develop and deliver training programs on various topics like company policies, safety procedures, and professional development.
# Qualifications:
# Bachelor's degree in Human Resources, Business Administration, or related field.
# 2+ years of experience in a generalist HR role.
# Strong understanding of employment laws and compliance requirements.
# Excellent communication and interpersonal skills.
# Proficiency in Microsoft Office Suite and HR management systems.
# Ability to prioritize tasks and manage multiple projects simultaneously.
# Strong problem-solving and decision-making abilities."""

#     get_unique_skills(text)
