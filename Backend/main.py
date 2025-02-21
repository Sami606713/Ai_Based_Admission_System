# Load the agents
from Agents.conversation_agent import conversation_agent
from Agents.gather_data_agent import AdmissionAgent
from router.query_router import route_query
import streamlit as st  

# Initialize session state variables
if "in_admission" not in st.session_state:
    st.session_state.in_admission = False  # Track if admission process is active
if "admission_complete" not in st.session_state:
    st.session_state.admission_complete = False  # Track if admission is completed

st.title("LangChain")

query = st.chat_input("You: ")
if query:
    # If admission is in progress
    if st.session_state.in_admission and not st.session_state.admission_complete:
        st.write("🔵 Admission in progress")
        st.error(query)
        response = AdmissionAgent(query)  # Continue admission conversation
        
        # ✅ Extract the AI message content (response[0])
        response_text = response[0] if isinstance(response, tuple) else response

        st.success(response_text)

        # Example condition to check if admission is complete
        if "admission completed" in response_text.lower():
            st.session_state.admission_complete = True
            st.session_state.in_admission = False
            st.success("✅ Admission process completed. You can now continue the conversation.")

    # If admission is not in progress, route the query
    else:
        intent = route_query(query=query)
        st.error(f"Intent: {intent} Query: {query}")

        if intent == "information":
            response = conversation_agent(query)
            response_text = response[0] if isinstance(response, tuple) else response
            st.success(response_text)

        elif intent == "admission":
            st.session_state.in_admission = True
            st.session_state.admission_complete = False
            response = AdmissionAgent(query)
            response_text = response[0] if isinstance(response, tuple) else response
            st.success(response_text)
