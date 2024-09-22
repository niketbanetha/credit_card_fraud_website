import streamlit as st

introduction_page = st.Page("pages/introduction.py", title="Project Detail")
team_information_page = st.Page("pages/team_information.py", title="Team Member Details")
pp_flow_chart = st.Page("pages/project_plan_pages/flow_chart.py", title="Flow Chart")
pp_page_2 = st.Page("pages/project_plan_pages/page_2.py", title="Problem Sub-domain Research")
pp_page_3 = st.Page("pages/project_plan_pages/page_3.py", title="Analyzing Research Paper")
pp_page_4 = st.Page("pages/project_plan_pages/page_4.py", title="Dataset Research")
pp_page_5 = st.Page("pages/project_plan_pages/page_5.py", title="Algorithm Analysis")
pp_page_6 = st.Page("pages/project_plan_pages/page_6.py", title="Algorithm Selection")
pp_page_7 = st.Page("pages/project_plan_pages/page_7.py", title="User Interface")

pg = st.navigation(
    {"Home": [introduction_page],
     "Team Information": [team_information_page],
     "Project Plan": [pp_flow_chart, pp_page_2, pp_page_3, pp_page_4, pp_page_5, pp_page_6, pp_page_7],
     "Implementation Plan": [],
     "Code Explanation": [],
     "Check for fraud": [],
     "Future Uses": []}) 

pg.run()

