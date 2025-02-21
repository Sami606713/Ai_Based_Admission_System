# Load the agents
from Agents.conversation_agent import conversation_agent
from Agents.gather_data_agent import AdmissionAgent
from router.query_router import route_query



if __name__ =="__main__":
    query = input("You: ")

    # Step 1: Route the query to determine the intent
    intent = route_query(query=query)
    print("Intent: ",intent)
    # if intent == "information":
    #     result = conversation_agent.run(query)
        

    # elif intent == "admission":
    #     result = gather_data_agent.run(query)
    #     print(result)