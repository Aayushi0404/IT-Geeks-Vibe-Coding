import streamlit as st
import google.generativeai as genai
import json
import time

# --- 1. PASTE YOUR GEMINI API KEY HERE ---
api_key = "PASTE_YOUR_GEMINI_API_KEY_HERE"


# Configure Gemini
genai.configure(api_key=api_key)
# Gemini 1.5 Flash handles 1 MILLION tokens easily!
model = genai.GenerativeModel('gemini-3.6-flash', generation_config={"response_mime_type": "application/json"})

def analyze_rulebook(question, rulebook_text):
    prompt = f"""
    You are an expert strict academic rulebook analyzer. 
    Analyze the entire text to answer the user's question.
    You MUST output a valid JSON object with three exact keys:
    "state": strictly one of ["ANSWERED", "NOT_COVERED", "CONTRADICTION"]
    "answer": Brief explanation of what you found. If not covered, say so.
    "citations": The exact sentence(s) from the text. If contradiction, quote both conflicting sections.

    Rulebook Text:
    {rulebook_text}

    Question: {question}
    """
    
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        return {"error": str(e)}

# --- UI SETTINGS ---
st.set_page_config(page_title="Rulebook AI", layout="wide", initial_sidebar_state="expanded")

try:
    with open("rulebook.md", "r", encoding="utf-8") as f:
        rulebook = f.read()
except FileNotFoundError:
    st.error("⚠️ Please run `python generate_data.py` first to generate the rulebook!")
    st.stop()

# --- SIDEBAR EVAL DASHBOARD ---
with st.sidebar:
    st.title("📊 Eval Dashboard")
    st.markdown("Run the automated test suite to check system accuracy.")
    
    if st.button("Run Live Eval (Sample)"):
        test_q = [
            {"q": "What is the penalty for paying tuition late?", "expected": "CONTRADICTION"},
            {"q": "What happens if I miss the exam due to a wedding?", "expected": "NOT_COVERED"},
            {"q": "What is the exact due date for Odd Semester fee payment?", "expected": "ANSWERED"}
        ]
        score = 0
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, t in enumerate(test_q):
            status_text.text(f"Testing: {t['q']}...")
            res = analyze_rulebook(t['q'], rulebook)
            if not res.get("error") and res.get("state") == t['expected']:
                score += 1
            progress_bar.progress((i + 1) / len(test_q))
            time.sleep(2) # Safe delay
            
        status_text.empty()
        st.success(f"🏆 Quick Eval Score: {score}/{len(test_q)}")
        st.metric(label="System Accuracy", value=f"{(score/len(test_q))*100:.0f}%")

# --- MAIN DASHBOARD ---
st.title("📚 The Rulebook That Argues With Itself")
st.markdown("Ask a question. The AI will find the answer, admit if it's missing, or catch conflicting rules.")

col1, col2 = st.columns([1.5, 1])

with col1:
    st.subheader("💬 Ask the Rulebook")
    question = st.text_input("Type your question here:", placeholder="E.g., What is the penalty for paying tuition late?")
    
    if st.button("Analyze Rulebook", type="primary"):
        if question:
            with st.spinner("Scanning 6,000 words using Gemini 1M Context..."):
                result = analyze_rulebook(question, rulebook)
                
                if "error" in result:
                    st.error(f"🚨 API Error: {result['error']}")
                else:
                    state = result.get("state")
                    answer = result.get("answer")
                    citations = result.get("citations")
                    
                    if state == "ANSWERED":
                        st.success("✅ **STATUS: ANSWERED** - Information found cleanly.")
                    elif state == "NOT_COVERED":
                        st.warning("🤷 **STATUS: NOT_COVERED** - The rulebook does not mention this.")
                    elif state == "CONTRADICTION":
                        st.error("🚨 **STATUS: CONTRADICTION DETECTED** - Conflicting rules found!")
                    
                    st.markdown(f"**Answer:** {answer}")
                    st.info(f"**Citations:**\n\n{citations}")

with col2:
    st.subheader("📄 Document Context")
    with st.expander("View Full Rulebook", expanded=True):
        st.text_area("Read-only view", rulebook, height=500, disabled=True)