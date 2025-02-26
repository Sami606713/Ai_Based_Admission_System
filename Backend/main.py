import streamlit as st  

# Load the agents
from Agents.conversation_agent import conversation_agent
from Agents.gather_data_agent import AdmissionAgent
from router.query_router import route_query
from Tools.gather_data_tool import data_gather_tool

# ========================== #
#    Load Tools and Memory
# ========================== #
tools, memory = data_gather_tool()

# ========================== #
#    Initialize Session State
# ========================== #
if "in_admission" not in st.session_state:
    st.session_state.in_admission = False  # Track if admission process is active
if "admission_complete" not in st.session_state:
    st.session_state.admission_complete = False  # Track if admission is completed
if "memory" not in st.session_state:
    st.session_state.memory = memory  # Store memory in session state

# ========================== #
#           UI Title
# ========================== #
st.title("LangChain")

# ========================== #
#       User Interaction
# ========================== #
query = st.chat_input("You: ")
if query:
    # If admission is in progress
    if st.session_state.in_admission and not st.session_state.admission_complete:
        st.write("🔵 Admission in progress")
        st.error(f"Query: {query}")
        # ✅ Continue admission conversation
        response, st.session_state.memory = AdmissionAgent(query, st.session_state.memory)
        response_text = response[0] if isinstance(response, tuple) else response
        st.success(response_text)

        # ✅ Check if admission process is complete
        if "admission completed" in response_text.lower():
            st.session_state.admission_complete = True
            st.session_state.in_admission = False
            st.success("✅ Admission process completed. You can now continue the conversation.")

    # If admission is not in progress, route the query
    else:
        intent = route_query(query=query)
        st.error(f"Intent: {intent} | Query: {query} {type(intent)}")
        
        # response = conversation_agent(query)
        # response_text = response[0] if isinstance(response, tuple) else response
        # st.success(response_text)

        if intent == "information":
            print("Routing to conversation......")
            response = conversation_agent(query)
            response_text = response[0] if isinstance(response, tuple) else response
            st.success(response_text)

        elif intent == "admission":
            print("Routing to admission......") 
            st.session_state.in_admission = True
            st.session_state.admission_complete = False
            response, st.session_state.memory = AdmissionAgent(query, st.session_state.memory)
            response_text = response[0] if isinstance(response, tuple) else response
            st.success(response_text)
