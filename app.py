import json
from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="MissionHome AI | Family Support Copilot",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded",
)

DATA_PATH = Path(__file__).parent / "resources.json"

@st.cache_data
def load_resources():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

resources = load_resources()

# A futuristic visual system; animations are decorative and do not imply live model activity.
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Mono:wght@400;500&family=Inter:wght@400;500;600;700;800&display=swap');
:root { color-scheme: dark; }
.stApp {
  background: radial-gradient(ellipse at 48% 0%, #0b2944 0%, #061522 38%, #030a12 100%);
  color: #e8f5ff;
}
html, body, [class*="css"] { font-family: 'Inter', sans-serif; }
.block-container {max-width: 1500px; padding-top: 1.4rem; padding-bottom: 2.5rem;}
[data-testid="stSidebar"] {background: linear-gradient(180deg,#071a2b,#040d17); border-right:1px solid #123d59;}
[data-testid="stSidebar"] * {color:#d9edff;}
h1,h2,h3 {letter-spacing:-.035em;}
h1 {font-weight:800;}
p, li {line-height:1.55;}
.hero {
  border:1px solid #14517a; border-radius:22px; padding:1.6rem 1.8rem;
  background:linear-gradient(115deg,rgba(9,40,67,.96),rgba(5,18,32,.96));
  box-shadow:0 0 35px rgba(0,153,255,.08); margin-bottom:1.2rem;
}
.eyebrow {font-family:'DM Mono',monospace; text-transform:uppercase; letter-spacing:.16em;
  color:#53c9ff; font-size:.72rem;}
.hero h1 {color:#f0f9ff; font-size:clamp(2rem,4vw,3.15rem); margin:.35rem 0 .2rem;}
.hero p {color:#b8d4e9; margin:.25rem 0;}
.glow {color:#62d1ff;}
.panel {background:rgba(5,20,34,.78); border:1px solid #164364; border-radius:17px;
  padding:1.15rem 1.2rem; margin-bottom:.9rem;}
.panel-title {color:#dff4ff;font-size:1.08rem;font-weight:700;margin-bottom:.5rem;}
.muted {color:#9ab8cf;font-size:.88rem;}
.status {display:inline-block;border:1px solid #176c80;background:#062b37;color:#72f2d0;
  padding:.28rem .65rem;border-radius:999px;font-family:'DM Mono',monospace;font-size:.72rem;}
.chat-bot {background:linear-gradient(135deg,#0b2944,#081a2b);border:1px solid #17557b;
  border-radius:4px 18px 18px 18px;padding:1rem;margin:.6rem 0;}
.chat-user {background:linear-gradient(135deg,#07538a,#07365d);border:1px solid #1888c4;
  border-radius:18px 4px 18px 18px;padding:1rem;margin:.6rem 0;}
.step-number {color:#5bd2ff;font-family:'DM Mono',monospace;font-size:.8rem;}
div.stButton > button, div.stLinkButton > a {
  border-radius:11px; border:1px solid #1873a5; transition:all .15s ease;
}
div.stButton > button:hover, div.stLinkButton > a:hover {
  border-color:#63d8ff; box-shadow:0 0 16px rgba(36,174,255,.14); color:#fff;
}
div[data-testid="stForm"] {background:rgba(6,25,42,.7);border:1px solid #164364;border-radius:16px;padding:1rem;}
hr {border-color:#16354d;}
[data-testid="stMetric"] {background:rgba(6,27,45,.7);border:1px solid #164364;padding:.8rem;border-radius:13px;}
.stCaption, [data-testid="stCaptionContainer"] {color:#8eacc3;}
footer {visibility:hidden;}
</style>
""", unsafe_allow_html=True)

# App navigation
with st.sidebar:
    st.markdown('<div style="font-size:2.1rem">🛡️</div><div style="font-size:1.45rem;font-weight:800">MissionHome</div><div style="color:#62cfff;font-size:.82rem">FAMILY SUPPORT COPILOT</div>', unsafe_allow_html=True)
    st.divider()
    page = st.radio(
        "NAVIGATION",
        ["⌂  Command Center", "✧  Mission Copilot", "▤  Official Resources", "✓  My Action Plan"],
        label_visibility="collapsed",
    )
    st.divider()
    st.markdown('<div class="eyebrow">CORE PRINCIPLE</div><p style="font-size:.9rem">Real people. Real needs. Verified support.</p>', unsafe_allow_html=True)
    st.caption("Privacy first · Official sources · Human choice")
    st.markdown("---")
    st.markdown('<span class="status">PROTOTYPE MODE</span>', unsafe_allow_html=True)
    st.caption("The AI model is not connected in this version. No answers are sent to an AI service.")

if "scenario" not in st.session_state:
    st.session_state.scenario = "Childcare fell through"
if "priority" not in st.session_state:
    st.session_state.priority = "Today / next 24 hours"
if "details" not in st.session_state:
    st.session_state.details = ""
if "plan_ready" not in st.session_state:
    st.session_state.plan_ready = False

def resource_matches(*terms):
    matched = []
    for item in resources:
        text = " ".join([
            item.get("name", ""), item.get("category", ""), item.get("description", ""),
            item.get("first_step", ""), " ".join(item.get("keywords", []))
        ]).casefold()
        if any(term.casefold() in text for term in terms):
            matched.append(item)
    return matched

def resource_card(item):
    with st.container(border=True):
        st.markdown(f"**{item['name']}**")
        st.caption(f"{item['category']} · Source: {item['source_owner']}")
        st.write(item["description"])
        st.markdown(f"**Suggested first step:** {item['first_step']}")
        st.link_button("Open official source ↗", item["url"], key="link_" + item["name"], use_container_width=True)

if page == "⌂  Command Center":
    st.markdown("""
    <div class="hero">
      <div class="eyebrow">MISSIONHOME / SUPPORT INTELLIGENCE</div>
      <h1>Your family matters.<br><span class="glow">Let's find the next step.</span></h1>
      <p>A calmer starting point when service, family life, and urgent needs collide.</p>
      <div style="margin-top:1rem"><span class="status">● READY TO LISTEN</span> &nbsp; <span class="muted">Official resources · Human-led decisions</span></div>
    </div>
    """, unsafe_allow_html=True)
    a, b, c = st.columns(3)
    with a:
        st.markdown('<div class="panel"><div class="eyebrow">01 / TALK IT THROUGH</div><div class="panel-title">Mission Copilot</div><p class="muted">Answer a few guided questions and shape a manageable next step.</p></div>', unsafe_allow_html=True)
        if st.button("Open Mission Copilot →", use_container_width=True):
            st.session_state["page_nav_hint"] = "copilot"
            st.info("Choose **✧ Mission Copilot** in the left navigation to continue.")
    with b:
        st.markdown('<div class="panel"><div class="eyebrow">02 / FIND SUPPORT</div><div class="panel-title">Verified resources</div><p class="muted">Browse official starting points for essential needs, housing, family readiness, and careers.</p></div>', unsafe_allow_html=True)
        if st.button("Explore resources →", use_container_width=True):
            st.info("Choose **▤ Official Resources** in the left navigation.")
    with c:
        st.markdown('<div class="panel"><div class="eyebrow">03 / TAKE ACTION</div><div class="panel-title">Your action plan</div><p class="muted">Turn a stressful situation into small steps, provider questions, and a fallback.</p></div>', unsafe_allow_html=True)
        if st.button("View action plan →", use_container_width=True):
            st.info("Choose **✓ My Action Plan** in the left navigation.")
    st.markdown("### How MissionHome helps")
    x, y = st.columns([1.25, 1])
    with x:
        st.markdown('<div class="panel"><div class="panel-title">From uncertainty to a next step</div><p>① Understand what needs attention first</p><p>② Identify official services that may be relevant</p><p>③ Prepare useful questions for the provider</p><p>④ Keep a backup option if the first path does not work</p></div>', unsafe_allow_html=True)
    with y:
        st.markdown('<div class="panel"><div class="panel-title">A few important boundaries</div><p class="muted">MissionHome is a navigation aid, not an eligibility decision-maker or emergency dispatch service.</p><p class="muted">Do not enter Social Security numbers, bank details, medical records, deployment dates, classified information, or unit locations.</p><p class="muted">For immediate danger in the U.S., call 911. For a mental health crisis, call or text 988.</p></div>', unsafe_allow_html=True)
    st.caption("Prototype note: the interface is JARVIS-inspired, but a live AI model has not been connected yet.")

elif page == "✧  Mission Copilot":
    st.markdown('<div class="eyebrow">MISSION COPILOT / GUIDED INTAKE</div><h1>Let’s work through this <span class="glow">together.</span></h1><p class="muted">You do not need to share names or identifying details. Start with the issue, not private information.</p>', unsafe_allow_html=True)
    st.markdown('<div class="chat-bot"><b>MISSIONHOME</b><br>Hi. What is putting the most pressure on you right now? We can break it into smaller steps and find official places to start.</div>', unsafe_allow_html=True)
    with st.form("copilot_form"):
        scenario = st.radio(
            "1. What kind of support would help most?",
            [
                "Childcare fell through",
                "Housing or relocation",
                "Food or essential needs",
                "Financial pressure",
                "Family stress or deployment transition",
                "Spouse career or employment",
                "Something else",
            ],
            index=[
                "Childcare fell through", "Housing or relocation", "Food or essential needs",
                "Financial pressure", "Family stress or deployment transition",
                "Spouse career or employment", "Something else",
            ].index(st.session_state.scenario),
        )
        priority = st.radio(
            "2. When do you need a next step?",
            ["Right now / today", "Today / next 24 hours", "This week", "Planning ahead"],
            index=1,
        )
        details = st.text_area(
            "3. What would be useful for us to understand? (optional)",
            value=st.session_state.details,
            placeholder="For example: I need a backup plan for tomorrow morning. Please don't include personal or operational details.",
            max_chars=600,
            help="Avoid names, exact locations, deployment dates, unit information, account numbers, or medical records.",
        )
        submitted = st.form_submit_button("Build my support plan →", use_container_width=True)
    if submitted:
        st.session_state.scenario = scenario
        st.session_state.priority = priority
        st.session_state.details = details
        st.session_state.plan_ready = True
    if st.session_state.plan_ready:
        st.divider()
        st.markdown('<div class="chat-user"><b>YOUR PRIORITY</b><br>' + st.session_state.scenario + '<br><span class="muted">' + st.session_state.priority + '</span></div>', unsafe_allow_html=True)
        st.markdown('<div class="chat-bot"><b>MISSIONHOME / SUPPORT PLAN PREVIEW</b><br>I hear that this needs attention. Here is a practical starting point. This is a transparent, rule-based prototype—not a live AI-generated response. Please verify availability and eligibility directly with each provider.</div>', unsafe_allow_html=True)
        scenario_lower = st.session_state.scenario.casefold()
        if "childcare" in scenario_lower or "family stress" in scenario_lower:
            suggestions = resource_matches("family", "deployment", "counseling", "installation")
            actions = [
                "Write down the immediate need and the time by which support is required.",
                "Contact the relevant official family-support or installation office and ask about current options, eligibility, hours, and backup choices.",
                "If the first option is unavailable, ask the provider which official alternative they recommend and note the next contact.",
            ]
            questions = [
                "What support is available for my situation, and who is eligible?",
                "What are the current hours, costs (if any), and availability?",
                "If you cannot help directly, which official office should I contact next?",
            ]
        elif "housing" in scenario_lower:
            suggestions = resource_matches("housing", "relocation", "installation", "veteran")
            actions = [
                "Write down the housing or move-related problem and the deadline you are working toward.",
                "Use the official installation directory or relevant government portal to locate a starting office.",
                "Confirm current availability, documents needed, and a backup contact directly with the provider.",
            ]
            questions = [
                "Which services fit my circumstances and location?",
                "What documents should I prepare, and what should I avoid sending by email?",
                "What is the next step if there is no immediate availability?",
            ]
        elif "food" in scenario_lower or "essential" in scenario_lower:
            suggestions = resource_matches("food", "essentials", "SNAP", "WIC", "resources")
            actions = [
                "Identify the immediate essentials needed and how soon they are needed.",
                "Review the official food-assistance guidance and contact providers to confirm local availability and eligibility.",
                "If the first provider cannot help, ask for a referral to another official or community resource.",
            ]
            questions = [
                "Is there help available for my household's situation?",
                "How do I confirm local availability and eligibility?",
                "Who can I contact if I need support sooner?",
            ]
        elif "financial" in scenario_lower:
            suggestions = resource_matches("financial", "money", "budget", "bills")
            actions = [
                "List the most time-sensitive bill or financial concern without sharing account numbers.",
                "Review official financial-counseling options and ask the provider what support is available.",
                "Before making a major financial decision, confirm details with a qualified counselor or the relevant institution.",
            ]
            questions = [
                "Can I access counseling for this concern?",
                "What information should I prepare for the conversation?",
                "Are there official referrals for time-sensitive needs?",
            ]
        elif "career" in scenario_lower:
            suggestions = resource_matches("employment", "career", "spouse", "job")
            actions = [
                "Choose the kind of role or career support you want to pursue first.",
                "Review the official federal jobs portal and military spouse employment resources.",
                "Check each opportunity's requirements and current closing date before applying.",
            ]
            questions = [
                "Which programs or employers support military spouses?",
                "What eligibility or documentation does this opportunity require?",
                "Where can I get help translating my experience into a civilian résumé?",
            ]
        else:
            suggestions = resource_matches("resources", "family", "support", "counseling")
            actions = [
                "Name one practical outcome you want help with first.",
                "Open a relevant official starting point below and confirm the right contact.",
                "Ask the provider for the next step and a referral if it is not the right office.",
            ]
            questions = [
                "Is this the right office for my situation?",
                "What should I do first?",
                "If you cannot help, where should I go next?",
            ]
        st.markdown("### Your first three steps")
        for i, action in enumerate(actions, 1):
            st.markdown(f'<div class="panel"><span class="step-number">STEP 0{i}</span><br>{action}</div>', unsafe_allow_html=True)
        st.markdown("### Questions you can ask")
        for q in questions:
            st.markdown(f"- {q}")
        st.session_state["generated_actions"] = actions
        st.session_state["generated_questions"] = questions
        st.session_state["suggested_resources"] = [r["name"] for r in suggestions[:5]]
        st.markdown("### Official starting points")
        if suggestions:
            for item in suggestions[:4]:
                resource_card(item)
        else:
            st.info("Open Official Resources to browse the full directory.")
        st.caption("No live AI inference is running. This prototype maps your selected topic to curated resources and prewritten planning steps.")

elif page == "▤  Official Resources":
    st.markdown('<div class="eyebrow">RESOURCE DIRECTORY / OFFICIAL STARTING POINTS</div><h1>Trusted places to <span class="glow">start.</span></h1><p class="muted">These links are starting points, not guarantees of eligibility or availability. Confirm details directly with each provider.</p>', unsafe_allow_html=True)
    category_options = ["All areas"] + sorted({r["category"] for r in resources})
    selected_category = st.selectbox("Filter by support area", category_options)
    query = st.text_input("Search official resources", placeholder="Try: food, relocation, spouse employment")
    shown = resources
    if selected_category != "All areas":
        shown = [r for r in shown if r["category"] == selected_category]
    terms = query.casefold().split()
    if terms:
        def searchable(resource):
            return " ".join([
                resource.get("name", ""), resource.get("category", ""), resource.get("description", ""),
                resource.get("first_step", ""), resource.get("source_owner", ""),
                " ".join(resource.get("keywords", []))
            ]).casefold()
        shown = [r for r in shown if all(term in searchable(r) for term in terms)]
    if not shown:
        st.warning("No exact matches. Showing the full directory so you can still find a starting point.")
        shown = resources
    st.caption(f"Showing {len(shown)} official resource(s).")
    for start in range(0, len(shown), 2):
        cols = st.columns(2)
        for col, item in zip(cols, shown[start:start+2]):
            with col:
                resource_card(item)

elif page == "✓  My Action Plan":
    st.markdown('<div class="eyebrow">MY PLAN / SMALL STEPS COUNT</div><h1>Your next steps, <span class="glow">at your pace.</span></h1>', unsafe_allow_html=True)
    if not st.session_state.plan_ready:
        st.info("Your plan will appear here after you use Mission Copilot. You can also start with this general checklist.")
        actions = [
            "Choose the most time-sensitive need.",
            "Open one official resource and confirm current details.",
            "Write down questions for the provider.",
            "Ask for a referral or backup option if needed.",
        ]
        questions = []
    else:
        st.markdown(f"**Focus:** {st.session_state.scenario}  \n**Timeframe:** {st.session_state.priority}")
        actions = st.session_state.get("generated_actions", [
            "Choose the most time-sensitive need.",
            "Open one official resource and confirm current details.",
            "Write down questions for the provider.",
        ])
        questions = st.session_state.get("generated_questions", [])
    st.markdown("### Checklist")
    done = 0
    for idx, action in enumerate(actions):
        if st.checkbox(action, key=f"plan_step_{idx}"):
            done += 1
    st.progress(done / max(len(actions), 1), text=f"{done} of {len(actions)} steps checked off")
    if questions:
        st.markdown("### Questions to take with you")
        for question in questions:
            st.markdown(f"- {question}")
    st.markdown("### Need another starting point?")
    for item in resources[:3]:
        resource_card(item)
    st.caption("Checklist progress is held in this app session; it is not a secure case-management system.")

st.divider()
st.markdown('<div class="muted">MISSIONHOME · Because your mission matters — at home too. &nbsp; | &nbsp; Official resources only &nbsp; | &nbsp; Prototype: live AI not yet connected</div>', unsafe_allow_html=True)
