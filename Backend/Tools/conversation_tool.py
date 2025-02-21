from langchain_community.tools import TavilySearchResults
from dotenv import load_dotenv  
import os
load_dotenv()



TAVILY_API_KEY= os.getenv("TAVILY_API_KEY")
def search_tool(query:str): 
        
        # Tavily Search Tool
        tool = TavilySearchResults(
            max_results=10,
            search_depth="advanced",
            include_answer=True,
            include_raw_content=True,
            include_images=True,
            tavily_api_key=TAVILY_API_KEY,
            include_domains=['https://www.uoh.edu.pk/',"https://www.uoh.edu.pk/portal","https://www.uoh.edu.pk/portal#gsc.tab=0","https://www.uoh.edu.pk/admissions/",'https://www.uoh.edu.pk/admissions/fee','https://www.uoh.edu.pk/admissions/schedule','http://www.uoh.edu.pk/admissions/facilities','http://www.uoh.edu.pk/admissions/eligibility','https://www.uoh.edu.pk/administration.php?page=vice-chancellor-office#gsc.tab=0','https://www.uoh.edu.pk/administration.php?page=student-financical-aid-office#gsc.tab=0','https://www.uoh.edu.pk/administration.php?page=registrar-office#gsc.tab=0','https://www.uoh.edu.pk/administration.php?page=quality-enhancement-cell#gsc.tab=0','https://www.uoh.edu.pk/academics#gsc.tab=0'],
            name="Univerity Search Tool",         
            description="tool can search the user query on the provided website and provide the response.",    
        )

        result = tool.invoke(query)
        return result

if __name__ == "__main__":
        query = "What is the fee structure of the university of Haripur?"
        response = search_tool(query)
        print(response)