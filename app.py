import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Healthcare Operations AI Prompting System™",
    page_icon="🧠",
    layout="wide"
)

WHITE = "#FFFFFF"
BLACK = "#000000"
ORANGE = "#FF8200"

st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {WHITE}; color: {BLACK}; }}
    section[data-testid="stSidebar"] {{ background-color: {BLACK}; }}
    section[data-testid="stSidebar"] * {{ color: {WHITE} !important; }}
    h1, h2, h3 {{ color: {BLACK}; letter-spacing: -0.03em; }}
    p, li, div, span {{ color: {BLACK}; }}
    .hero {{ border: 2px solid {BLACK}; border-left: 12px solid {ORANGE}; border-radius: 18px; padding: 30px; background-color: {WHITE}; margin-bottom: 24px; }}
    .label {{ color: {ORANGE}; font-weight: 900; text-transform: uppercase; letter-spacing: 0.08em; font-size: 0.86rem; margin-bottom: 10px; }}
    .section-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 20px; background-color: {WHITE}; margin-bottom: 18px; }}
    .impact-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 18px; background-color: {WHITE}; min-height: 145px; margin-bottom: 14px; }}
    .impact-label {{ color: {BLACK}; font-size: 0.95rem; font-weight: 900; margin-bottom: 8px; }}
    .impact-text {{ color: {BLACK}; font-size: 0.98rem; line-height: 1.55; }}
    .orange-text {{ color: {ORANGE}; font-weight: 900; }}
    .orange-rule {{ border-top: 4px solid {ORANGE}; margin: 24px 0; }}
    .workflow-strip {{ border: 2px solid {BLACK}; border-radius: 18px; padding: 18px; background-color: {WHITE}; margin: 18px 0; font-weight: 800; line-height: 1.9; }}
    .mode-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 18px; background-color: {WHITE}; margin-bottom: 16px; }}
    .mode-number {{ color: {ORANGE}; font-size: 0.9rem; font-weight: 950; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 6px; }}
    .mode-title {{ color: {BLACK}; font-size: 1.25rem; font-weight: 950; margin-bottom: 8px; }}
    .mode-subhead {{ color: {BLACK}; font-weight: 900; margin-top: 12px; margin-bottom: 4px; }}
    .mode-text {{ color: {BLACK}; line-height: 1.55; }}
    .example-box {{ border-left: 6px solid {ORANGE}; padding-left: 12px; margin-top: 10px; margin-bottom: 10px; }}
    .disclaimer {{ border: 2px solid {ORANGE}; border-radius: 16px; padding: 18px; background-color: {WHITE}; font-weight: 650; }}
    .footer {{ border-top: 2px solid {BLACK}; padding-top: 14px; margin-top: 28px; font-weight: 800; color: {BLACK}; }}
    div[data-testid="stMetric"] {{ border: 1.5px solid {BLACK}; border-radius: 14px; padding: 16px; background-color: {WHITE}; }}
    div[data-testid="stMetricLabel"] p {{ color: {BLACK} !important; font-weight: 850 !important; }}
    div[data-testid="stMetricValue"] {{ color: {ORANGE} !important; font-weight: 950 !important; }}
    </style>
    """,
    unsafe_allow_html=True
)

job_modes = pd.DataFrame([
    ["Brainstorming Mode", "Generate project ideas, LinkedIn post ideas, workflow angles, and improvement opportunities.", "Generate 10 patient access failure points that could create denial risk, staff rework, or patient confusion.", "Workflow ideation", "Shows I can turn healthcare operations problems into structured portfolio ideas.", "Do not claim real employer experience or use real patient examples."],
    ["Skill-Creator Mode", "Build a repeatable framework, checklist, audit tool, or workflow review system.", "Create a front-end denial prevention checklist for registration, eligibility, authorization, and documentation readiness.", "Process design", "Shows I can create reusable healthcare operations tools, not just discuss concepts.", "Use simulated examples only."],
    ["Writing-Plans Mode", "Plan a project, dashboard, case study, or LinkedIn content series.", "Create a 7-day plan for building a simulated prior authorization failure dashboard and recruiter-facing case study.", "Project planning", "Shows I can organize work into phases, milestones, deliverables, risks, and next actions.", "Do not overstate authority or claim professional implementation."],
    ["Executing-Plans Mode", "Build one step at a time inside Google Sheets, GitHub, Streamlit, or LinkedIn.", "Walk through creating a no-PHI Google Sheets audit tool, then turn it into a GitHub README and Streamlit app.", "Implementation discipline", "Shows I can move from idea to finished portfolio asset with clear steps.", "Keep the project educational and no-PHI."],
    ["Design Mode", "Create dashboard layouts, LinkedIn graphics, case study pages, or portfolio visuals.", "Design a clean patient access risk dashboard using white, black, and Tennessee Orange only.", "Professional presentation", "Shows I can communicate workflow findings in a recruiter-facing visual format.", "No misleading clinical, billing, or employer claims."],
    ["Front-End Review Mode", "Review a project for clarity, credibility, recruiter value, and professionalism.", "Check whether a portfolio dashboard is honest, readable, no-PHI, and aligned with entry-level healthcare operations roles.", "Quality review", "Shows I can evaluate my own work for accuracy, scope, professionalism, and credibility.", "Protect accuracy and avoid exaggeration."],
    ["Research Mode", "Review job descriptions, role requirements, current keywords, or placement strategy.", "Compare entry-level patient access, prior authorization, revenue cycle, and health informatics support job postings for common skills.", "Career alignment", "Shows I can connect portfolio projects to actual role requirements and recruiter keywords.", "Do not claim skills that cannot be explained or demonstrated."]
], columns=["AI Job Mode", "When To Use It", "Healthcare Operations Example", "Career Skill Demonstrated", "Recruiter Value", "Risk Guardrail"])

use_cases = pd.DataFrame([
    ["Patient Access", "Appointment reason is unclear before the visit.", "Patient Access Workflow Risk Map"],
    ["Eligibility Verification", "Insurance information is outdated, incomplete, or not verified before service.", "Eligibility Failure Risk Tracker"],
    ["Prior Authorization", "Authorization is missing, pending, or submitted too late.", "Prior Authorization Failure Intelligence System"],
    ["Documentation Readiness", "Documentation does not support the service, authorization, or claim.", "Documentation Integrity Audit"],
    ["Denial Prevention", "Denials appear downstream but often begin upstream.", "Denial Prevention Workflow Map"],
    ["Staff Rework", "Staff spend time correcting issues that should have been prevented earlier.", "Staff Rework Burden Dashboard"],
    ["Patient Experience", "Patients experience delays, confusion, repeated calls, or unclear next steps.", "Patient Journey Operations Profile"],
    ["Revenue Cycle", "Claims are delayed, denied, corrected, appealed, or reworked.", "Revenue Cycle Risk Dashboard"],
    ["AI Governance", "AI outputs may be inaccurate, incomplete, biased, or outside scope.", "Healthcare AI Governance Checklist"]
], columns=["Healthcare Area", "Workflow Problem", "Portfolio Output"])

prompt_library = pd.DataFrame([
    ["Brainstorming", "Act as my healthcare operations brainstorming partner and generate realistic no-PHI portfolio project ideas."],
    ["Skill-Creator", "Act as a healthcare operations skill-builder and create a repeatable workflow risk framework."],
    ["Writing-Plans", "Act as a healthcare operations project planner and create a 7-day build plan."],
    ["Executing-Plans", "Act as my project execution assistant and help me build one step at a time."],
    ["Design Mode", "Act as my portfolio design assistant using white, black, and Tennessee Orange only."],
    ["Front-End Review", "Act as a portfolio reviewer and check clarity, credibility, accuracy, and recruiter value."],
    ["Research Mode", "Act as my healthcare career research assistant and identify role keywords and portfolio ideas."],
    ["Interview Prep", "Act as my interview coach and help me explain this project honestly."],
    ["LinkedIn Post", "Act as my LinkedIn healthcare operations content assistant and create a recruiter-facing post."]
], columns=["Prompt Category", "Prompt Starter"])

project_ideas = pd.DataFrame([
    ["Patient Access Workflow Risk Map", "Patient access failures create downstream delays, denials, and patient confusion."],
    ["Prior Authorization Failure Intelligence System", "Authorization failures create retro authorization risk, denial risk, staff rework, and patient access delays."],
    ["Eligibility Verification Risk Tracker", "Incorrect or outdated coverage information creates claim denials and patient billing confusion."],
    ["Documentation Readiness Audit", "Incomplete documentation creates authorization delays, claim risk, and staff rework."],
    ["Denial Prevention Workflow Map", "Denials often begin before the claim is submitted."],
    ["Patient Journey Operations Profile", "Patients feel workflow breakdowns before leadership sees them in reports."],
    ["Healthcare Operations AI Prompting System", "Vague AI prompts create vague outputs, just like vague workflows create operational drift."],
    ["Revenue Cycle Workflow Intelligence Engine", "Revenue cycle risk builds across patient access, authorization, documentation, claims, denials, A/R, and payment posting."]
], columns=["Project Title", "Workflow Problem"])

st.sidebar.title("Healthcare Operations Intelligence Engine™")
st.sidebar.caption("Where healthcare workflows break before patients, staff, and revenue feel the impact.")
page = st.sidebar.radio("Navigate", ["Home", "AI Job Modes", "Healthcare Use Cases", "Prompt Library", "Portfolio Project Ideas", "Recruiter Talking Points", "LinkedIn Content", "Portfolio Summary", "Disclaimer"])

def hero(title, subtitle):
    st.markdown(f"""
    <div class="hero">
        <div class="label">Healthcare Operations Intelligence Engine™</div>
        <h1>{title}</h1>
        <p style="font-size:1.15rem; line-height:1.6; margin-bottom:0;">{subtitle}</p>
    </div>
    """, unsafe_allow_html=True)

def footer():
    st.markdown("""<div class="footer">Created by Kori Pickle · BSHA Candidate · Simulated no-PHI portfolio project</div>""", unsafe_allow_html=True)

if page == "Home":
    hero("Healthcare Operations AI Prompting System™", "A simulated no-PHI portfolio project showing how responsible AI prompting can support healthcare workflow analysis, denial prevention thinking, patient access review, prior authorization awareness, and recruiter-facing career development.")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Healthcare Operations", "Thinking")
        st.metric("Responsible AI Use", "Guardrailed")
    with col2:
        st.metric("Workflow Analysis", "Structured")
        st.metric("No-PHI Status", "Protected")
    st.markdown('<div class="orange-rule"></div>', unsafe_allow_html=True)
    st.markdown("## Why This Project Matters to Recruiters")
    st.markdown("""<div class="section-card">This project shows how I organize healthcare operations problems before they become downstream risk. It connects responsible AI use to practical healthcare administration skills, including workflow review, patient access awareness, prior authorization readiness, documentation quality, denial prevention, revenue cycle thinking, and professional communication.</div>""", unsafe_allow_html=True)
    st.markdown("## Skills Demonstrated")
    skill_col1, skill_col2 = st.columns(2)
    with skill_col1:
        st.markdown("""<div class="impact-card"><div class="impact-label">Workflow + Revenue Cycle</div><div class="impact-text">Workflow analysis<br>Patient access awareness<br>Prior authorization process awareness<br>Denial prevention thinking</div></div>""", unsafe_allow_html=True)
    with skill_col2:
        st.markdown("""<div class="impact-card"><div class="impact-label">AI + Professional Judgment</div><div class="impact-text">Responsible AI prompting<br>No-PHI project design<br>Healthcare AI governance awareness<br>Recruiter-facing communication</div></div>""", unsafe_allow_html=True)
    st.markdown("## Workflow Intelligence Path")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">Prompt clarity</span> → Workflow question → Risk category → Human review → Prevention action → Portfolio proof</div>""", unsafe_allow_html=True)
    st.markdown("## Project Purpose")
    st.write("This project demonstrates how a BSHA candidate can use AI responsibly as a structured healthcare operations thinking partner. It translates vague requests into specific job modes that support workflow analysis, patient access review, prior authorization risk detection, documentation readiness, denial prevention thinking, revenue cycle process awareness, and career placement preparation.")
    st.markdown("## Career Relevance")
    st.write("This app supports entry-level remote or hybrid healthcare administration, patient access, prior authorization support, eligibility verification, revenue cycle support, denial prevention support, documentation coordination, operations support, and health informatics support positioning.")
    st.markdown("## Core Question")
    st.write("How can AI be used responsibly to help identify where healthcare workflows break before patients, staff, and revenue feel the impact?")
    footer()

elif page == "AI Job Modes":
    hero("AI Job Modes", "Use the right AI role for the healthcare operations task in front of you.")
    st.markdown("## Why This Page Matters")
    st.markdown("""<div class="section-card">This page turns AI from a generic answer box into a structured workflow support tool. Each mode gives AI a specific job so the output is easier to review, safer to use, and more connected to patient access, prior authorization, documentation readiness, denial prevention, revenue cycle, and career placement preparation.</div>""", unsafe_allow_html=True)
    for index, row in job_modes.iterrows():
        st.markdown(f"""
        <div class="mode-card">
            <div class="mode-number">Mode {index + 1}</div>
            <div class="mode-title">{row['AI Job Mode']}</div>
            <div class="mode-subhead">When to use it</div>
            <div class="mode-text">{row['When To Use It']}</div>
            <div class="example-box">
                <div class="mode-subhead">Healthcare operations example</div>
                <div class="mode-text">{row['Healthcare Operations Example']}</div>
            </div>
            <div class="mode-subhead">Career skill demonstrated</div>
            <div class="mode-text">{row['Career Skill Demonstrated']}</div>
            <div class="mode-subhead">Recruiter value</div>
            <div class="mode-text">{row['Recruiter Value']}</div>
            <div class="mode-subhead">Guardrail</div>
            <div class="mode-text">{row['Risk Guardrail']}</div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("## Recruiter-Facing Takeaway")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">I do not just ask AI questions.</span> I assign AI a clear healthcare operations role, define the scope, protect privacy, connect the output to real workflow concepts, and review the result before using it as portfolio material.</div>""", unsafe_allow_html=True)
    footer()

elif page == "Healthcare Use Cases":
    hero("Healthcare Use Cases", "Each AI job mode connects to a healthcare operations learning area using simulated examples only.")
    st.dataframe(use_cases, use_container_width=True, hide_index=True)
    footer()

elif page == "Prompt Library":
    hero("Prompt Library", "Reusable prompts for responsible healthcare operations portfolio building.")
    st.dataframe(prompt_library, use_container_width=True, hide_index=True)
    selected = st.selectbox("Choose a prompt category", prompt_library["Prompt Category"])
    prompt = prompt_library[prompt_library["Prompt Category"] == selected].iloc[0]["Prompt Starter"]
    st.code(prompt, language="text")
    footer()

elif page == "Portfolio Project Ideas":
    hero("Portfolio Project Ideas", "Simulated no-PHI projects that demonstrate healthcare operations thinking without claiming formal work experience.")
    st.dataframe(project_ideas, use_container_width=True, hide_index=True)
    footer()

elif page == "Recruiter Talking Points":
    hero("Recruiter Talking Points", "Clear, honest language for explaining this project without exaggerating experience.")
    st.markdown("### Tell me about your portfolio.")
    st.write("My portfolio includes simulated no-PHI healthcare operations projects that show how I think through patient access, prior authorization, denial prevention, documentation workflow, revenue cycle risk, and patient experience.")
    st.markdown("### How do you use AI?")
    st.write("I use AI as a structured thinking partner, not as a replacement for human judgment. I use it to organize workflow questions, build simulated project frameworks, identify operational risk categories, and improve how I explain healthcare operations problems.")
    st.markdown("### Do you have healthcare work experience?")
    st.write("I do not have formal healthcare work experience yet. I am building credibility through my BSHA coursework, healthcare operations portfolio projects, LinkedIn content, networking, and my patient-to-professional perspective.")
    footer()

elif page == "LinkedIn Content":
    hero("LinkedIn Content", "A recruiter-facing launch post for this project.")
    st.code("""I built a simulated no-PHI portfolio project called Healthcare Operations AI Prompting System™.

The purpose is simple:

Show how AI can support healthcare operations thinking when the prompt gives AI a specific job.

Instead of asking vague questions, this project organizes AI into job modes:

Brainstorming Mode
Skill-Creator Mode
Writing-Plans Mode
Executing-Plans Mode
Design Mode
Front-End Review Mode
Research Mode

Each mode connects to healthcare operations use cases such as patient access workflow review, eligibility verification risk, prior authorization failure prevention, documentation readiness, denial prevention, revenue cycle workflow analysis, patient experience friction, and responsible AI use.

This project does not use real patient data, PHI, payer data, claims data, or employer data.

Created by Kori Pickle""", language="text")
    footer()

elif page == "Portfolio Summary":
    hero("Portfolio Summary", "A concise recruiter-facing summary of what this project demonstrates.")
    st.subheader("Project Type")
    st.write("Simulated no-PHI healthcare operations portfolio project")
    st.subheader("Skills Demonstrated")
    st.write("Healthcare operations thinking, workflow analysis, denial prevention awareness, prior authorization process awareness, patient access risk identification, documentation workflow awareness, responsible AI prompting, project planning, portfolio development, and professional communication.")
    st.subheader("Recruiter-Facing Explanation")
    st.write("I created this project to show how I use AI responsibly as a healthcare operations thinking partner. Because I do not have formal healthcare work experience yet, I used simulated no-PHI examples only.")
    footer()

elif page == "Disclaimer":
    hero("Disclaimer", "Privacy, scope, and responsible-use guardrails for this simulated project.")
    st.markdown("""<div class="disclaimer">This project uses simulated educational examples only. It does not include real patient data, PHI, payer data, employer data, claims data, or clinical decision-making. It is intended for healthcare operations learning, portfolio development, and career placement preparation.</div>""", unsafe_allow_html=True)
    st.subheader("What This Project Does Not Claim")
    st.write("It does not claim formal healthcare work experience, clinical authority, billing authority, coding authority, reimbursement authority, legal authority, or patient-care decision-making.")
    footer()
