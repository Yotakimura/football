import streamlit as st
import datetime

def main():
    st.header("Team Calendar & Scheduling")

    if "events" not in st.session_state:
        st.session_state["events"] = []
    if "rsvp" not in st.session_state:
        st.session_state["rsvp"] = {}

    # Add a new event
    st.subheader("Add New Event")
    with st.form("add_event_form"):
        event_name = st.text_input("Event Name")
        event_type = st.selectbox("Event Type", ["Practice", "Game", "Meeting", "Other"])
        event_date = st.date_input("Event Date", min_value=datetime.date.today())
        event_time = st.time_input("Event Time", value=datetime.time(17, 0))
        event_desc = st.text_area("Description / Notes")
        add_event_btn = st.form_submit_button("Add Event")
        if add_event_btn and event_name:
            st.session_state["events"].append({
                "name": event_name,
                "type": event_type,
                "date": event_date,
                "time": event_time,
                "desc": event_desc,
                "id": f"{event_name}_{event_date}_{event_time}"
            })
            st.success(f"Event '{event_name}' added.")

    # List upcoming events
    st.subheader("Upcoming Events")
    if st.session_state["events"]:
        # Sort by date and time
        upcoming = sorted(st.session_state["events"], key=lambda e: (e["date"], e["time"]))
        for event in upcoming:
            event_id = event["id"]
            st.markdown(f"""
**{event['name']}**  
_Type:_ {event['type']}  
**When:** {event['date']} {event['time'].strftime('%I:%M %p')}  
{event['desc']}
""")
            # RSVP Section
            with st.expander("RSVP / Mark Availability", expanded=False):
                player = st.text_input(f"Your Name for {event_id}", key=f"rsvp_name_{event_id}")
                status = st.radio(
                    "Will you attend?",
                    ["Attending", "Not Attending", "Maybe"],
                    key=f"rsvp_status_{event_id}"
                )
                submit_rsvp = st.button("Submit RSVP", key=f"rsvp_btn_{event_id}")
                if submit_rsvp and player:
                    if event_id not in st.session_state["rsvp"]:
                        st.session_state["rsvp"][event_id] = {}
                    st.session_state["rsvp"][event_id][player] = status
                    st.success("RSVP submitted!")

            # Show RSVP Summary
            if event_id in st.session_state["rsvp"]:
                st.write("**RSVPs:**")
                rsvps = st.session_state["rsvp"][event_id]
                for pname, avail in rsvps.items():
                    st.write(f"- {pname}: {avail}")
            st.markdown("---")
    else:
        st.info("No events scheduled yet! Add an event above.")
