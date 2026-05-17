from fastapi import FastAPI
from pydantic import BaseModel
from google import genai
from dotenv import load_dotenv
import os
load_dotenv()
# 1. Initialize FastAPI
app = FastAPI(title="Simple GenAI API")
 
# 2. Initialize the Gemini Client with your hardcoded key
#GEMINI_API_KEY = "your_api_key_here"  # Replace with your actual key
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)
 
# 3. Define what the incoming request data should look like
class QueryRequest(BaseModel):
    prompt: str
 
# 4. Health check endpoint
@app.get("/health")
async def health_check():
    """Simple health check to verify the service is running."""
    return {"status": "ok"}
 
# 5. Create the API endpoint
@app.post("/ask")
async def ask_gemini(request: QueryRequest):
    """
    Takes a prompt, waits for Gemini to finish generating the entire
    response, and returns it as a standard JSON object.
    """
    # This matches your simple code exactly
    response = client.models.generate_content(
        model='gemini-2.5-flash',
        contents=request.prompt,
    )
    
    # Return the text back to the client as JSON
    return {"response": response.text}