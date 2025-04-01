import requests
import json

def ask_llm(prompt, model="mistral:7b"):
    """
    Send a prompt to a locally running Ollama model and get the response.
    
    Args:
        prompt (str): The question or prompt to send to the model
        model (str): The name of the model to use (default: "mistral:7b")
    
    Returns:
        str: The model's response
    """

    url = "http://localhost:11434/api/generate"
    
    data = {
        "model": model,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  # Raise an exception for bad status
        result = response.json()
        return result["response"]
    except requests.exceptions.RequestException as e:
        return f"Error: {str(e)}\nMake sure Ollama is running locally!"

def main():
    print("Local LLM Chat (type 'quit' to exit)")
    print("-" * 50)
    
    while True:
        user_input = input("\nYour question: ")
        
        if user_input.lower() in ['quit', 'exit']:
            print("\nGoodbye!")
            break
            
        response = ask_llm(user_input)
        print("\nResponse:", response)

if __name__ == "__main__":
    main()