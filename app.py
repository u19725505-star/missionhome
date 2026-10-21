import json
from pathlib import Path
import streamlit as st

st.set_page_config(page_title="MissionHome | Military Family Support", page_icon="🛡️", layout="wide")

DATA_PATH = Path(__file__).parent / "resources.json"

@st.cache_data
def load_resources():
    with DATA_PATH.open("r", encoding="utf-8") as f:
        return json.load(f)

resources = load_resources()

st.markdown("""
<style>
.block-container {max-width: 1120px; padding-top: 2rem; padding-bottom: 3rem;}
.hero {padding: 1.6rem 1.8rem; border-radius: 18px; background: linear-gradient(120deg,#102b46,#1d5365); color: white; margin-bottom: 1.3rem;}
.hero h1 {color:white; font-size:2.4rem; margin-bottom:.25rem;}
.hero p {color:#e1edf3; font-size:1.05rem;}
.small-note {color:#526477; font-size:.9rem;}
</style>
<div class="hero">
  <h1>🛡️ MissionHome</h1>
  <p>Practical support for the people who serve alongside those who serve.</p>
  <p>Find official starting points for housing, essential needs, family readiness, and careers.</p>
</div>
""", unsafe_allow_html=True)

st.info("MissionHome is a navigation aid, not an eligibility decision-maker. Confirm current services, availability, and requirements directly with each provider. This early version links to official sources and does not send your answers to an AI service.")

# Stable widget keys let people clear filters without refreshing the whole page.
if "category_filter" not in st.session_state:
    st.session_state["category_filter"] = "All areas"
if "search_filter" not in st.session_state:
    st.session_state["search_filter"] = ""

left, right = st.columns([1, 2])
with left:
    st.subheader("What would help today?")
    if st.button("Clear filters", use_container_width=True):
        st.session_state["category_filter"] = "All areas"
        st.session_state["search_filter"] = ""
        st.rerun()
    category = st.selectbox(
        "Choose a support area",
        ["All areas"] + sorted({r["category"] for r in resources}),
        key="category_filter",
    )
    search = st.text_input(
        "Search resources",
        placeholder="e.g. relocation, spouse jobs",
        key="search_filter",
        help="You can enter one or more words. Matching is case-insensitive.",
    )
    urgency = st.radio("How urgent is this?", ["Planning ahead", "Need help soon", "Immediate danger"], index=0)
    if urgency == "Immediate danger":
        st.error("If someone is in immediate danger in the United States, call 911. For a mental health crisis, call or text 988. If this is not an emergency, continue below.")
    st.caption("Please don't enter Social Security numbers, bank details, medical records, deployment dates, or unit locations.")

with right:
    st.subheader("Official resource directory")
    filtered = resources
    if category != "All areas":
        filtered = [r for r in filtered if r["category"] == category]
    terms = search.casefold().split()
    if terms:
        def searchable_text(resource):
            fields = [
                resource.get("name", ""),
                resource.get("category", ""),
                resource.get("description", ""),
                resource.get("first_step", ""),
                resource.get("source_owner", ""),
                " ".join(resource.get("keywords", [])),
            ]
            return " ".join(fields).casefold()

        # Every search word must appear somewhere in the resource text.
        # This makes multi-word searches less brittle than exact-phrase matching.
        filtered = [
            r for r in filtered
            if all(term in searchable_text(r) for term in terms)
        ]
    st.caption(f"{len(filtered)} resource(s) match your selection.")
    if not filtered:
        st.warning("No exact matches. Try a broader search or choose All areas.")
    for r in filtered:
        with st.container(border=True):
            st.markdown(f"### {r['name']}")
            st.caption(r["category"])
            st.write(r["description"])
            st.markdown(f"**Good first step:** {r['first_step']}")
            st.link_button("Open official resource ↗", r["url"], use_container_width=False)
            st.caption(f"Source: {r['source_owner']} · Directory reviewed: {r['last_checked']}")

st.divider()
st.subheader("A simple next-step plan")
st.write("Use this checklist to turn a resource search into a manageable next step.")
task1 = st.checkbox("Choose one priority for today")
task2 = st.checkbox("Open the official resource and check current eligibility and availability")
task3 = st.checkbox("Write down questions to ask the provider")
task4 = st.checkbox("Save the provider's official contact details somewhere safe")
if st.button("Show my progress"):
    completed = sum([task1, task2, task3, task4])
    st.success(f"You've completed {completed} of 4 planning steps. Small, verified steps count.")

st.divider()
st.caption("MissionHome prototype · Resource links are provided for navigation, not as an endorsement or guarantee of assistance. Always verify details with the official provider.")
