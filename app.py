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
    .section-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 20px; background-color: {WHITE}; margin-bottom: 18px; line-height: 1.65; }}
    .impact-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 18px; background-color: {WHITE}; min-height: 145px; margin-bottom: 14px; }}
    .impact-label {{ color: {BLACK}; font-size: 0.95rem; font-weight: 900; margin-bottom: 8px; }}
    .impact-text {{ color: {BLACK}; font-size: 0.98rem; line-height: 1.55; }}
    .orange-text {{ color: {ORANGE}; font-weight: 900; }}
    .orange-rule {{ border-top: 4px solid {ORANGE}; margin: 24px 0; }}
    .workflow-strip {{ border: 2px solid {BLACK}; border-radius: 18px; padding: 18px; background-color: {WHITE}; margin: 18px 0; font-weight: 800; line-height: 1.9; }}
    .mode-card, .usecase-card, .prompt-card, .route-card, .framework-card {{ border: 1.5px solid {BLACK}; border-radius: 16px; padding: 18px; background-color: {WHITE}; margin-bottom: 16px; }}
    .mode-number, .usecase-area, .prompt-category, .route-letter, .framework-number {{ color: {ORANGE}; font-size: 0.9rem; font-weight: 950; letter-spacing: 0.05em; text-transform: uppercase; margin-bottom: 6px; }}
    .mode-title, .usecase-title, .prompt-title, .route-title, .framework-title {{ color: {BLACK}; font-size: 1.25rem; font-weight: 950; margin-bottom: 8px; }}
    .mode-subhead, .usecase-subhead, .prompt-subhead, .route-subhead, .framework-subhead {{ color: {BLACK}; font-weight: 900; margin-top: 12px; margin-bottom: 4px; }}
    .mode-text, .usecase-text, .prompt-text, .route-text, .framework-text {{ color: {BLACK}; line-height: 1.55; }}
    .example-box {{ border-left: 6px solid {ORANGE}; padding-left: 12px; margin-top: 10px; margin-bottom: 10px; }}
    .output-pill {{ display: inline-block; border: 1.5px solid {BLACK}; border-radius: 999px; padding: 6px 12px; margin-top: 10px; font-weight: 900; color: {BLACK}; background-color: {WHITE}; }}
    .disclaimer {{ border: 2px solid {ORANGE}; border-radius: 16px; padding: 18px; background-color: {WHITE}; font-weight: 650; }}
    .footer {{ border-top: 2px solid {BLACK}; padding-top: 14px; margin-top: 28px; font-weight: 800; color: {BLACK}; }}
    div[data-testid="stMetric"] {{ border: 1.5px solid {BLACK}; border-radius: 14px; padding: 16px; background-color: {WHITE}; }}
    div[data-testid="stMetricLabel"] p {{ color: {BLACK} !important; font-weight: 850 !important; }}
    div[data-testid="stMetricValue"] {{ color: {ORANGE} !important; font-weight: 950 !important; }}
    textarea {{ color: {BLACK} !important; background-color: {WHITE} !important; border: 1.5px solid {BLACK} !important; }}
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
    ["Patient Access", "Front-end intake", "Appointment reason is unclear before the visit.", "The wrong workflow path may begin before the patient is seen.", "Patient Access Workflow Risk Map", "Patient access workflow thinking"],
    ["Eligibility Verification", "Coverage validation", "Insurance information is outdated, incomplete, or not verified before service.", "Eligibility errors can create claim denials, patient confusion, and rework.", "Eligibility Failure Risk Tracker", "Revenue cycle awareness"],
    ["Prior Authorization", "Authorization readiness", "Authorization is missing, pending, or submitted too late.", "Late or missing authorization can create delays, retro-auth risk, and denial exposure.", "Prior Authorization Failure Intelligence System", "Prior authorization workflow analysis"],
    ["Documentation Readiness", "Clinical/admin documentation support", "Documentation does not support the service, authorization, or claim.", "Incomplete documentation can delay authorization, claims, appeals, and handoffs.", "Documentation Integrity Audit", "Documentation workflow awareness"],
    ["Denial Prevention", "Upstream risk detection", "Denials appear downstream but often begin upstream.", "The claim may fail because intake, eligibility, authorization, or documentation lost control earlier.", "Denial Prevention Workflow Map", "Root-cause thinking"],
    ["Staff Rework", "Operational burden", "Staff spend time correcting issues that should have been prevented earlier.", "Rework increases backlog, call volume, handoff friction, and staff workload.", "Staff Rework Burden Dashboard", "Operational risk analysis"],
    ["Patient Experience", "Patient journey friction", "Patients experience delays, confusion, repeated calls, or unclear next steps.", "The patient feels workflow breakdowns before the dashboard shows them.", "Patient Journey Operations Profile", "Patient-centered operations"],
    ["Revenue Cycle", "Financial workflow impact", "Claims are delayed, denied, corrected, appealed, or reworked.", "Upstream process issues can affect clean claim rate, A/R, cash flow, and avoidable corrections.", "Revenue Cycle Risk Dashboard", "Revenue cycle process understanding"],
    ["AI Governance", "Responsible AI use", "AI outputs may be inaccurate, incomplete, biased, or outside scope.", "Human review, privacy protection, and no-PHI boundaries must stay visible.", "Healthcare AI Governance Checklist", "Responsible AI awareness"]
], columns=["Healthcare Area", "Workflow Stage", "Workflow Problem", "Operational Risk", "Portfolio Output", "Skill Demonstrated"])

prompt_library = pd.DataFrame([
    ["Brainstorming", "Generate project ideas and workflow angles", "Act as my healthcare operations brainstorming partner. I am a BSHA candidate with no formal healthcare work experience. Generate realistic zero-cost simulated no-PHI portfolio project ideas focused on patient access, prior authorization, denial prevention, eligibility verification, documentation workflow, revenue cycle, health informatics, quality improvement, and patient experience. For each idea, include the project title, workflow problem, simulated data needed, dashboard output, skills demonstrated, and how to explain it to recruiters.", "Portfolio project idea list", "Do not invent work history, employer examples, clinical authority, or real patient scenarios."],
    ["Skill-Creator", "Build repeatable frameworks and checklists", "Act as a healthcare operations skill-builder. Create a repeatable framework I can use to analyze where healthcare workflows break before they become denials, delays, staff rework, patient confusion, or revenue cycle risk. Include intake question, workflow stage, failure signal, downstream risk, patient impact, staff impact, revenue impact, prevention action, KPI to monitor, and recruiter-facing skill demonstrated.", "Checklist, audit tool, or workflow framework", "Use simulated examples only and keep scope educational."],
    ["Writing-Plans", "Plan a portfolio project before building", "Act as a healthcare operations project planner. Create a 7-day build plan for a simulated no-PHI portfolio project called [PROJECT NAME]. Include day-by-day tasks, what to build in Google Sheets, what to write in Google Docs, what to post on LinkedIn, what to add to GitHub, what to say in interviews, and what not to claim.", "Step-by-step project plan", "Do not claim professional implementation or employer results."],
    ["Executing-Plans", "Build one step at a time", "Act as my healthcare operations project execution assistant. Help me build [PROJECT NAME] one step at a time. Do not give me everything at once. Start with Step 1 only. For each step, tell me exactly where to build it, exactly what to name it, exactly what columns or sections to create, what copy-paste text to use, how this helps my career placement, and what screenshot or proof I should save for my portfolio.", "Actionable build instructions", "Keep the project no-PHI and pause before major build decisions."],
    ["Design Mode", "Design dashboards, graphics, and portfolio pages", "Act as my healthcare operations portfolio design assistant. Design a premium recruiter-facing layout for [PROJECT NAME]. Use white background #FFFFFF, black typography #000000, Tennessee Orange #FF8200 as the only accent color, premium healthcare consulting style, large whitespace, mobile-first readability, and no blue, teal, bronze, gold, brown-orange, or gray-heavy styling.", "Layout and visual direction", "Protect brand consistency and avoid misleading claims."],
    ["Front-End Review", "Review finished work before posting", "Act as a healthcare operations portfolio reviewer. Review this project for recruiter visibility, professionalism, clarity, credibility, and accuracy. Check whether it looks entry-level but serious, avoids exaggerating my experience, clearly explains the workflow problem, shows healthcare operations thinking, aligns with my brand, and belongs in LinkedIn Featured.", "Quality review and improvement list", "Remove anything that overstates experience, authority, or results."],
    ["Research Mode", "Connect projects to job-market language", "Act as my healthcare career research assistant. Research current entry-level remote or hybrid healthcare administration roles related to patient access, prior authorization, revenue cycle, denial prevention, eligibility verification, documentation support, operations coordination, and health informatics support. Find common job titles, skills, keywords, tasks, portfolio project ideas, LinkedIn skills, and what I should not claim without work experience.", "Role keywords and career strategy", "Only use skills I can explain, demonstrate, or honestly describe as learning."],
    ["Interview Prep", "Explain projects to recruiters honestly", "Act as my healthcare operations interview coach. Help me explain my simulated no-PHI portfolio project to a recruiter honestly. I do not have formal healthcare work experience yet, so help me explain what I built, why I built it, what healthcare operations problem it demonstrates, what skills it shows, and what I am still learning.", "Interview talking points", "Stay honest about student status and no formal work experience."],
    ["LinkedIn Post", "Turn projects into professional posts", "Act as my LinkedIn healthcare operations content assistant. Turn this project into a professional LinkedIn post that is clear, credible, student-appropriate, and recruiter-facing. Do not exaggerate my experience. Do not use hashtags unless absolutely necessary. End with Created by Kori Pickle.", "LinkedIn post draft", "No fake experience, no inflated claims, and no unnecessary hashtags."]
], columns=["Prompt Category", "Best Used For", "Copy-Paste Prompt", "Output Expected", "Guardrail"])

route_framework = pd.DataFrame([
    ["R", "Role", "Tell AI what job it is doing.", "Act as a healthcare operations workflow analyst.", "Prevents generic answers by assigning a clear operating role."],
    ["O", "Objective", "Tell AI what problem you are solving.", "Identify where the prior authorization workflow lost control.", "Connects the prompt to a specific workflow problem and outcome."],
    ["U", "Use Case", "Name the healthcare area.", "Focus on patient access, eligibility, prior authorization, documentation readiness, denial prevention, revenue cycle, or patient experience.", "Keeps the output aligned with recognizable healthcare operations work."],
    ["T", "Trust Boundary", "Set privacy, scope, and honesty rules.", "Use simulated no-PHI examples only. Do not claim employer experience or clinical authority.", "Protects credibility, privacy, and professional scope."],
    ["E", "Expected Output", "Tell AI what to produce.", "Create a dashboard table, audit checklist, case study, recruiter talking points, LinkedIn post, or GitHub README.", "Turns the prompt into portfolio proof instead of a one-off answer."]
], columns=["Letter", "Framework Step", "Meaning", "Example", "Career Value"])

supporting_frameworks = pd.DataFrame([
    ["CLARITY", "Give AI a full job definition.", "Context → Look & Feel → Ask → Rules → Input → Target → Your role", "Use when building LinkedIn posts, dashboards, case studies, or recruiter explanations."],
    ["SOCRATES", "Think through a problem carefully.", "Situation → Objective → Constraints → Role → Action → Thinking → Evaluation → Summary", "Use when analyzing a workflow breakdown or denial prevention problem."],
    ["ANTICIPATE", "Plan ahead before a problem happens.", "Audience → Need → Task → Information → Constraints → Illustrate → Plan → Act → Test → Enhance", "Use when building prevention-focused tools like registration audits or authorization readiness checklists."],
    ["PARTNER", "Treat AI like a structured project partner.", "Purpose → Audience → Research → Think → Narrow → Execute → Review", "Use when building Streamlit apps, Google Sheets dashboards, GitHub READMEs, or portfolio posts."],
    ["TRUST", "Ask AI to explain, structure, and tailor the output.", "Task → Reason → Understand → Structure → Tailor", "Use when explaining healthcare operations concepts in a recruiter-facing way."],
    ["RIPPLE", "Map downstream effects from an upstream issue.", "Role → Input → Process → Points → Layout → Evaluate", "Use when asking where the workflow first lost control."],
    ["CATCH", "Quality-check before publishing.", "Context → Aim → Tone → Criteria → Help", "Use before posting on LinkedIn or adding a project to your portfolio."],
    ["MAGIC", "Create content with a clear purpose.", "Motivation → Audience → Goal → Input → Create", "Use for LinkedIn posts, infographics, and project summaries."]
], columns=["Framework", "Plain-English Meaning", "Structure", "Healthcare Career Use"])

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
page = st.sidebar.radio("Navigate", ["Home", "AI Job Modes", "Healthcare Use Cases", "Prompt Library", "Responsible Prompting Framework", "Portfolio Project Ideas", "Recruiter Talking Points", "LinkedIn Content", "Portfolio Summary", "Disclaimer"])

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
        st.markdown(f"""<div class="mode-card"><div class="mode-number">Mode {index + 1}</div><div class="mode-title">{row['AI Job Mode']}</div><div class="mode-subhead">When to use it</div><div class="mode-text">{row['When To Use It']}</div><div class="example-box"><div class="mode-subhead">Healthcare operations example</div><div class="mode-text">{row['Healthcare Operations Example']}</div></div><div class="mode-subhead">Career skill demonstrated</div><div class="mode-text">{row['Career Skill Demonstrated']}</div><div class="mode-subhead">Recruiter value</div><div class="mode-text">{row['Recruiter Value']}</div><div class="mode-subhead">Guardrail</div><div class="mode-text">{row['Risk Guardrail']}</div></div>""", unsafe_allow_html=True)
    st.markdown("## Recruiter-Facing Takeaway")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">I do not just ask AI questions.</span> I assign AI a clear healthcare operations role, define the scope, protect privacy, connect the output to real workflow concepts, and review the result before using it as portfolio material.</div>""", unsafe_allow_html=True)
    footer()

elif page == "Healthcare Use Cases":
    hero("Healthcare Use Cases", "How responsible AI prompting supports simulated healthcare operations workflow analysis.")
    st.markdown("## Why This Page Matters")
    st.markdown("""<div class="section-card">This page connects AI prompting to healthcare operations work areas recruiters recognize. Each use case shows the workflow problem, the operational risk, the portfolio output, and the skill demonstrated using simulated no-PHI examples only.</div>""", unsafe_allow_html=True)
    for index, row in use_cases.iterrows():
        st.markdown(f"""<div class="usecase-card"><div class="usecase-area">Use Case {index + 1}</div><div class="usecase-title">{row['Healthcare Area']}</div><div class="usecase-subhead">Workflow stage</div><div class="usecase-text">{row['Workflow Stage']}</div><div class="example-box"><div class="usecase-subhead">Workflow problem</div><div class="usecase-text">{row['Workflow Problem']}</div></div><div class="usecase-subhead">Operational risk</div><div class="usecase-text">{row['Operational Risk']}</div><div class="usecase-subhead">Skill demonstrated</div><div class="usecase-text">{row['Skill Demonstrated']}</div><div class="output-pill">Portfolio Output: {row['Portfolio Output']}</div></div>""", unsafe_allow_html=True)
    st.markdown("## Recruiter-Facing Takeaway")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">These use cases show practical healthcare operations thinking.</span> The focus is not clinical authority. The focus is workflow awareness, risk detection, documentation readiness, denial prevention, patient access, revenue cycle impact, and responsible AI use.</div>""", unsafe_allow_html=True)
    footer()

elif page == "Prompt Library":
    hero("Prompt Library", "Copy-paste prompts for responsible healthcare operations portfolio building.")
    st.markdown("## Why This Page Matters")
    st.markdown("""<div class="section-card">This page gives me reusable prompt templates that support healthcare operations learning, portfolio development, LinkedIn content, recruiter preparation, and responsible AI use. Each prompt includes a purpose, expected output, and guardrail so the work stays realistic, no-PHI, and student-appropriate.</div>""", unsafe_allow_html=True)
    for index, row in prompt_library.iterrows():
        st.markdown(f"""<div class="prompt-card"><div class="prompt-category">Prompt {index + 1}</div><div class="prompt-title">{row['Prompt Category']}</div><div class="prompt-subhead">Best used for</div><div class="prompt-text">{row['Best Used For']}</div><div class="prompt-subhead">Output expected</div><div class="prompt-text">{row['Output Expected']}</div><div class="example-box"><div class="prompt-subhead">Guardrail</div><div class="prompt-text">{row['Guardrail']}</div></div></div>""", unsafe_allow_html=True)
    st.markdown("## Copy-Paste Prompt Selector")
    selected = st.selectbox("Choose a prompt category", prompt_library["Prompt Category"])
    selected_row = prompt_library[prompt_library["Prompt Category"] == selected].iloc[0]
    st.text_area("Copy-paste prompt", value=selected_row["Copy-Paste Prompt"], height=260)
    st.markdown("## Recruiter-Facing Takeaway")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">This prompt library shows repeatable work habits.</span> It proves I can define the task, set scope, protect privacy, request useful outputs, and review AI-supported work before using it in a professional portfolio.</div>""", unsafe_allow_html=True)
    footer()

elif page == "Responsible Prompting Framework":
    hero("Responsible Prompting Framework", "A healthcare operations framework for turning vague AI requests into structured, no-PHI portfolio outputs.")
    st.markdown("## Core Insight")
    st.markdown("""<div class="section-card"><span class="orange-text">AI gives better results when the job is clearly defined.</span> Healthcare workflows also perform better when roles, handoffs, verification points, documentation expectations, and escalation rules are clear. This page turns generic prompting advice into a healthcare operations career-placement system.</div>""", unsafe_allow_html=True)
    st.markdown("## Guessing vs. Directing")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""<div class="impact-card"><div class="impact-label">Weak prompt</div><div class="impact-text">Help me with healthcare administration.<br><br>This usually creates generic advice because the AI has no role, context, boundary, or expected output.</div></div>""", unsafe_allow_html=True)
    with col2:
        st.markdown("""<div class="impact-card"><div class="impact-label">Structured prompt</div><div class="impact-text">Act as a healthcare operations workflow analyst. Identify where patient access, eligibility, prior authorization, and documentation failures could create downstream denial risk, staff rework, patient confusion, and revenue cycle delays. Use simulated no-PHI examples only.</div></div>""", unsafe_allow_html=True)
    st.markdown("## Healthcare Operations AI Prompting Framework™")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">R.O.U.T.E.</span> = Role → Objective → Use Case → Trust Boundary → Expected Output</div>""", unsafe_allow_html=True)
    for index, row in route_framework.iterrows():
        st.markdown(f"""<div class="route-card"><div class="route-letter">{row['Letter']}</div><div class="route-title">{row['Framework Step']}</div><div class="route-subhead">What it means</div><div class="route-text">{row['Meaning']}</div><div class="example-box"><div class="route-subhead">Example</div><div class="route-text">{row['Example']}</div></div><div class="route-subhead">Career value</div><div class="route-text">{row['Career Value']}</div></div>""", unsafe_allow_html=True)
    st.markdown("## Supporting Prompt Frameworks")
    st.markdown("""<div class="section-card">These are supporting frameworks I studied, but <span class="orange-text">R.O.U.T.E.</span> is the healthcare operations version I use for my own portfolio work.</div>""", unsafe_allow_html=True)
    for index, row in supporting_frameworks.iterrows():
        st.markdown(f"""<div class="framework-card"><div class="framework-number">Framework {index + 1}</div><div class="framework-title">{row['Framework']}</div><div class="framework-subhead">Plain-English meaning</div><div class="framework-text">{row['Plain-English Meaning']}</div><div class="framework-subhead">Structure</div><div class="framework-text">{row['Structure']}</div><div class="framework-subhead">Healthcare career use</div><div class="framework-text">{row['Healthcare Career Use']}</div></div>""", unsafe_allow_html=True)
    st.markdown("## Copy-Paste R.O.U.T.E. Prompt")
    route_prompt = """Act as my healthcare operations workflow intelligence assistant.

My goal is to build a simulated no-PHI healthcare operations portfolio project that helps me demonstrate practical thinking for entry-level healthcare administration, patient access, prior authorization, denial prevention, revenue cycle, documentation workflow, health informatics, and patient experience roles.

Role:
Act as a healthcare operations workflow analyst.

Objective:
Help me identify where a healthcare workflow may lose control before patients, staff, and revenue feel the downstream impact.

Use Case:
Focus on [PATIENT ACCESS / ELIGIBILITY / PRIOR AUTHORIZATION / DOCUMENTATION READINESS / DENIAL PREVENTION / REVENUE CYCLE / PATIENT EXPERIENCE].

Trust Boundary:
Use simulated educational examples only. Do not use PHI, real patient data, payer data, employer data, claims data, or clinical decision-making. Do not invent work experience, job titles, certifications, or professional authority.

Expected Output:
Create a structured portfolio-ready output with:
1. Workflow problem
2. Failure point
3. Downstream risk
4. Patient impact
5. Staff rework impact
6. Revenue cycle impact
7. Prevention action
8. KPI or signal to monitor
9. Recruiter-facing skill demonstrated
10. Honest student explanation

End by answering:
Where did the workflow first lose control?"""
    st.text_area("Copy-paste prompt", value=route_prompt, height=420)
    st.markdown("## Recruiter-Facing Takeaway")
    st.markdown("""<div class="workflow-strip"><span class="orange-text">This framework shows that I am not using AI randomly.</span> I define the role, set the objective, name the healthcare use case, protect privacy, and request a portfolio-ready output that supports patient access, prior authorization, denial prevention, documentation readiness, revenue cycle thinking, and responsible AI use.</div>""", unsafe_allow_html=True)
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
