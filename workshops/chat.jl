using HTTP
using JSON3

function send_prompt(prompt::String, model::String="mistral:7b")
    url = "http://localhost:11434/api/generate"
    headers = ["Content-Type" => "application/json"]
    
    body = JSON3.write(Dict(
        "model" => model,
        "prompt" => prompt,
        "stream" => false
    ))
    
    response = HTTP.post(url, headers, body)
    result = JSON3.read(response.body)
    return result.response
end

function chat()
    println("Chat with AI (type 'exit' to quit)")
    println("Loading model...")
    println("Note: Working in the REPL in VS Code is tricky with user input.")
    println("Thus, you first need to enter some random value and press enter.")
    println("Then, you can start chatting by asking a question.")
    println("Afterwards, you can continue by asking questions and pressing enter.")
    println("To prevent this, you have to run the code in a terminal directly.")
    
    while true
        print("\nYou: ")
        user_input = readline()
        
        if lowercase(user_input) == "exit"
            println("\nGoodbye!")
            break
        end
        
        try
            response = send_prompt(user_input)
            println("\nAI: ", response)
        catch e
            println("\nError: Make sure Ollama is running and the model is installed.")
            println("You can install the model with: ollama pull mistral:7b")
            break
        end
    end
end

# Start the chat
chat()
