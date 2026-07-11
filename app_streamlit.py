"""
InterviewMate – Agentic AI Interview Trainer
Direct IBM watsonx.ai API integration (Project ID + Region URL + API Key + Model ID)
No IBM watsonx Orchestrate required.

Run locally:
    pip install -r requirements.txt
    streamlit run app_streamlit.py

Set your credentials as environment variables (or Streamlit secrets when deployed):
    WATSONX_API_KEY   - your IBM Cloud API key
    WATSONX_URL       - regional URL, e.g. https://us-south.ml.cloud.ibm.com
    WATSONX_PROJECT_ID - your watsonx.ai Project ID
    WATSONX_MODEL_ID  - e.g. ibm/granite-4-h-small (fallback: meta-llama/llama-3-3-70b-instruct)
"""

import os
import streamlit as st
from ibm_watsonx_ai import Credentials, APIClient
from ibm_watsonx_ai.foundation_models import ModelInference

# ---------------------------------------------------------------------------
# 1. Load credentials (env vars locally, st.secrets when deployed on Streamlit Cloud)
# ---------------------------------------------------------------------------
def get_secret(key: str, default: str = "") -> str:
    try:
        if key in st.secrets:
            return st.secrets[key]
    except Exception:
        pass
    return os.environ.get(key, default)

API_KEY = get_secret("WATSONX_API_KEY")
REGION_URL = get_secret("WATSONX_URL", "https://eu-de.ml.cloud.ibm.com")
PROJECT_ID = get_secret("WATSONX_PROJECT_ID")
MODEL_ID = get_secret("WATSONX_MODEL_ID", "ibm/granite-4-h-small")

# ---------------------------------------------------------------------------
# 2. Load the knowledge base (simple RAG via prompt-stuffing — small enough to fit in context)
# ---------------------------------------------------------------------------
@st.cache_data
def load_knowledge_base() -> str:
    kb_path = os.path.join(os.path.dirname(__file__), "Interview_Question_Bank_KnowledgeBase.md")
    if os.path.exists(kb_path):
        with open(kb_path, "r", encoding="utf-8") as f:
            return f.read()
    return ""

KNOWLEDGE_BASE = load_knowledge_base()

SYSTEM_PROMPT = f"""You are InterviewMate, an AI interview coach that helps students and job
seekers prepare for placements.

When a user shares their target job role, experience level, or resume details:
1. Ask clarifying questions if role/experience level is missing.
2. Generate 5-7 tailored interview questions (mix of technical and behavioral) based on
   their role and experience, using the reference knowledge base below where relevant.
3. If the user answers a question, evaluate their response, point out gaps, and provide
   a model answer with improvement tips.
4. Keep a supportive, encouraging tone - the goal is to build confidence.
5. At the end of a session, summarize the candidate's readiness with a score out of 10
   and the top 2-3 areas to improve.

Reference knowledge base:
---
{KNOWLEDGE_BASE}
---
"""

# ---------------------------------------------------------------------------
# 3. Initialize the watsonx.ai model client (cached across reruns)
# ---------------------------------------------------------------------------
@st.cache_resource
def get_model():
    credentials = Credentials(url=REGION_URL, api_key=API_KEY)
    client = APIClient(credentials, project_id=PROJECT_ID)
    model = ModelInference(api_client=client, model_id=MODEL_ID)
    return model


def get_ai_response(chat_history):
    model = get_model()
    messages = [{"role": "system", "content": SYSTEM_PROMPT}] + chat_history
    response = model.chat(messages=messages)
    ai_text = response["choices"][0]["message"]["content"]
    usage = response.get("usage", {})
    return ai_text, usage


# ---------------------------------------------------------------------------
# 4. Streamlit UI
# ---------------------------------------------------------------------------
st.set_page_config(
    page_title="InterviewMate",
    page_icon=":material/chat:",
    layout="centered",
)

# ── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("### :material/settings: Session")
    st.divider()

    with st.container(border=True):
        st.caption("Model")
        st.markdown(f"`{MODEL_ID}`")
        st.caption("Region")
        st.markdown(f"`{REGION_URL}`")

    st.space("small")

    with st.container(border=True):
        st.caption("Tokens used this session")
        st.metric(
            label="Total tokens",
            value=st.session_state.get("total_tokens", 0),
            label_visibility="collapsed",
        )

    st.space("small")

    if st.button(
        "Reset conversation",
        icon=":material/refresh:",
        type="primary",
    ):
        st.session_state.messages = []
        st.session_state.total_tokens = 0
        st.rerun()

    st.divider()

    # ── Theme toggle ──────────────────────────────────────────────────────────
    _is_dark = st.context.theme.type == "dark"
    _label   = ":material/light_mode: Switch to light mode" if _is_dark else ":material/dark_mode: Switch to dark mode"

    if st.button(_label, key="theme_toggle"):
        # Programmatically click Streamlit's built-in theme toggle checkbox.
        # The checkbox lives inside the settings panel; we open that panel
        # and click the toggle in the same JS tick so no manual interaction is needed.
        st.html("""
        <script>
        (function () {
          // Try the already-open settings panel first.
          function clickToggle() {
            var cb = document.querySelector('[data-testid="stThemeToggle"] input[type="checkbox"]');
            if (cb) { cb.click(); return true; }
            return false;
          }
          if (!clickToggle()) {
            // Panel not open yet — click the toolbar Settings button to open it.
            var btn = document.querySelector('[data-testid="stToolbarActionButtonIcon"]');
            if (btn) {
              btn.closest('button').click();
              // Give the panel time to mount, then toggle.
              setTimeout(clickToggle, 200);
            }
          }
        })();
        </script>
        """)

    st.caption("Powered by IBM watsonx.ai")

# ── Main header ───────────────────────────────────────────────────────────────
with st.container(horizontal_alignment="center"):
    st.markdown("# :material/chat: InterviewMate")
    st.caption("AI-powered interview coach — built on IBM watsonx.ai")

# ── Credentials warning ───────────────────────────────────────────────────────
if not API_KEY or not PROJECT_ID:
    st.warning(
        "Credentials not found. Set **WATSONX_API_KEY**, **WATSONX_URL**, and "
        "**WATSONX_PROJECT_ID** as environment variables or Streamlit secrets before chatting.",
        icon=":material/warning:",
    )

# ── Session state ─────────────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.total_tokens = 0

# ── Suggestion chips (shown only on an empty conversation) ────────────────────
SUGGESTIONS = {
    ":blue[:material/work:] Software developer fresher":
        "I'm a fresher applying for a Software Developer role with an IoT project. Ask me interview questions.",
    ":blue[:material/analytics:] Data science intern":
        "I'm a final-year student applying for a Data Science internship. I know Python and ML basics. Quiz me.",
    ":blue[:material/manage_accounts:] Product manager":
        "I'm targeting a Product Manager role with 2 years of experience. Give me a mock interview.",
    ":blue[:material/quiz:] Evaluate my answer":
        "I just answered: 'A linked list is a data structure where each node points to the next.' How did I do?",
}

if not st.session_state.messages:
    selected = st.pills(
        "Suggested prompts",
        list(SUGGESTIONS.keys()),
        label_visibility="collapsed",
    )
    if selected:
        st.session_state.messages.append({"role": "user", "content": SUGGESTIONS[selected]})
        st.rerun()

# ── Chat history ──────────────────────────────────────────────────────────────
for msg in st.session_state.messages:
    avatar = ":material/person:" if msg["role"] == "user" else ":material/smart_toy:"
    with st.chat_message(msg["role"], avatar=avatar):
        st.markdown(msg["content"])

# ── Chat input ────────────────────────────────────────────────────────────────
prompt = st.chat_input(
    "e.g. I'm a fresher applying for a Software Developer role. Ask me interview questions.",
    submit_mode="disable",
)

if prompt:
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user", avatar=":material/person:"):
        st.markdown(prompt)

    with st.chat_message("assistant", avatar=":material/smart_toy:"):
        with st.spinner("Thinking…"):
            try:
                reply, usage = get_ai_response(st.session_state.messages)
                st.markdown(reply)
                if usage:
                    st.session_state.total_tokens += usage.get("total_tokens", 0)
                    st.caption(
                        f":material/token: {usage.get('total_tokens', 'N/A')} tokens "
                        f"(prompt: {usage.get('prompt_tokens', 'N/A')}, "
                        f"completion: {usage.get('completion_tokens', 'N/A')}) · "
                        f"session total: {st.session_state.total_tokens}"
                    )
            except Exception as e:
                reply = f"Error calling watsonx.ai: {e}"
                st.error(reply, icon=":material/error:")

    st.session_state.messages.append({"role": "assistant", "content": reply})
