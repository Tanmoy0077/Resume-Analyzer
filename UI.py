import streamlit as st
from pdfminer.high_level import extract_text
from utils import *
from plotly.subplots import make_subplots
import plotly.graph_objects as go

st.title(":spiral_note_pad: Resume Analyzer")
st.subheader("Check how your resume aligns with the job :100:")

file = st.file_uploader(":arrow_up: Upload your resume", type=['pdf'])
jd = st.text_area(
   "Paste your job description below"
)
btn = st.button("Analyze")

if btn:
   if file is None:
      st.error("Please upload the Resume")
   elif not jd:
      st.error("Please paste the job description and press Ctrl+Enter")
   else:
      text = extract_text(file).strip()
      resume_skills = get_skills(text)
      job_skills = get_skills(jd.strip())
      fig = make_subplots(rows=1, cols=2,specs=[[{'type':'domain'}, {'type':'domain'}]], subplot_titles=("Skills in Resume", "Skills in Job Description"))

      fig.add_trace(
         go.Pie(labels=resume_skills['Skill'].values, values=resume_skills["Frequency"].values),
         row=1, col=1
      )
      fig.add_trace(
         go.Pie(labels=job_skills['Skill'].values, values=job_skills["Frequency"].values),
         row=1, col=2
      )

      st.plotly_chart(fig)

      matched_skills = set(job_skills['Skill']).intersection(set(resume_skills["Skill"]))
      missing_skills = set(job_skills['Skill']) - set(resume_skills["Skill"])
      action_verbs = get_action_verbs(text)
      buzzwords = get_buzzwords(text)

      col1, col2, col3 = st.columns(3)

      match_pct = (len(matched_skills)/len(set(job_skills["Skill"])))*100

      col1.metric(label="Action Verbs", value=f"{len(action_verbs)}")      
      col2.metric(label="Buzzwords", value=f"{len(buzzwords)}") 
      col3.metric(label="Skill Match Percentage", value=f"{match_pct:.2f}%")
      
      if(len(missing_skills) > 0):  
         col3.subheader("Missing Skills")
         for item in missing_skills:
               col3.markdown(f"""- {item}""")
         col3.text("Try adding these skills in your resume")
      else:
         col3.text("Great Job! your skills perfectly align with the job description")
      
      if(len(buzzwords) > 0):
         col2.subheader("Buzzwords")
         for item in buzzwords:
               col2.markdown(f"""- {item}""")
         col2.text("Try removing these words from your resume")
      else:
         col2.text("Great Job! your resume doesn't contain any buzzwords")

      if(len(action_verbs) > 0):
         col1.subheader("Action Verbs")
         for item in action_verbs:
               col1.markdown(f"""- {item}""")
         
      else:
         col1.text("Try adding action verbs in your resume to showcase your responsibilites")
      


