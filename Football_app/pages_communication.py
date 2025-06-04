import streamlit as st
import datetime

# --- Team Message Board ---
st.header("Team Message Board")

if "messages" not in st.session_state:
    st.session_state["messages"] = []

with st.form("post_message"):
    category = st.selectbox("Category", ["Announcement", "Motivation", "Note"])
    message = st.text_area("Your message")
    submit = st.form_submit_button("Post")
    if submit and message:
        st.session_state["messages"].append({
            "date": datetime.datetime.now(),
            "category": category,
            "message": message
        })

st.subheader("Messages")
filter_category = st.selectbox("Filter by category", ["All"] + ["Announcement", "Motivation", "Note"], key="filter_cat")
sorted_msgs = sorted(st.session_state["messages"], key=lambda x: x["date"], reverse=True)
for msg in sorted_msgs:
    if filter_category == "All" or msg["category"] == filter_category:
        st.info(f"[{msg['category']}] {msg['date'].strftime('%Y-%m-%d %H:%M')}\n\n{msg['message']}")

# --- Feedback Forms ---
st.header("Feedback Forms")
if "feedback" not in st.session_state:
    st.session_state["feedback"] = []

with st.form("feedback_form"):
    feedback = st.text_area("Submit your feedback (can be anonymous)")
    name = st.text_input("Name (leave blank for anonymous)")
    submit_feedback = st.form_submit_button("Send Feedback")
    if submit_feedback and feedback:
        st.session_state["feedback"].append({
            "name": name if name else "Anonymous",
            "feedback": feedback,
            "date": datetime.datetime.now(),
            "response": "",
            "responded": False
        })

st.subheader("Feedback Received")
for i, fb in enumerate(st.session_state["feedback"]):
    st.write(f"**From:** {fb['name']} | **Date:** {fb['date'].strftime('%Y-%m-%d %H:%M')}")
    st.write(f"_{fb['feedback']}_")
    if not fb["responded"]:
        with st.form(f"response_form_{i}"):
            response = st.text_input("Coach's Response", key=f"resp_{i}")
            respond_btn = st.form_submit_button("Respond")
            if respond_btn and response:
                fb["response"] = response
                fb["responded"] = True
    elif fb["response"]:
        st.success(f"Coach: {fb['response']}")
    st.markdown("---")

# --- Q&A Section ---
st.header("Q&A Section")
if "questions" not in st.session_state:
    st.session_state["questions"] = []

with st.form("question_form"):
    q = st.text_input("Ask a question")
    asker = st.text_input("Your name (optional)")
    submit_q = st.form_submit_button("Post Question")
    if submit_q and q:
        st.session_state["questions"].append({
            "question": q,
            "asker": asker if asker else "Anonymous",
            "answer": "",
            "answered": False,
            "date": datetime.datetime.now()
        })

st.subheader("Questions")
for i, qa in enumerate(st.session_state["questions"]):
    st.write(f"**Q:** {qa['question']} _(by {qa['asker']}, {qa['date'].strftime('%Y-%m-%d %H:%M')})_")
    if not qa["answered"]:
        with st.form(f"answer_form_{i}"):
            ans = st.text_input("Coach's Answer", key=f"ans_{i}")
            mark_ans = st.form_submit_button("Mark as Answered")
            if mark_ans and ans:
                qa["answer"] = ans
                qa["answered"] = True
    else:
        st.success(f"**A:** {qa['answer']}")
    st.markdown("---")
