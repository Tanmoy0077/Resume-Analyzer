import streamlit as st
from pdfminer.high_level import extract_text
from utils import *
import pandas as pd
import plotly.express as px
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
      text = extract_text(file)
      resume_skills = get_skills(text.strip())
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
      match_pct = (len(matched_skills)/len(set(job_skills["Skill"])))*100
      st.metric(label="Skill Match Percentage", value=f"{match_pct}%")
      
      if(len(missing_skills) > 0):
         st.subheader("Missing Skills")
         for item in missing_skills:
               st.markdown(f"""- {item}""")
      else:
         st.text("Great Job! your skills perfectly align with the job description")

