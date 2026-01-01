"""
OpenAI API Assignment
======================
Try using your own OpenAI API key and complete the tasks below!

Setup:
1. Install openai: pip install openai
2. Set your API key as an environment variable or pass it directly
"""

from openai import OpenAI
import os

# Initialize the client (reads from OPENAI_API_KEY environment variable by default)
# Or use: client = OpenAI(api_key="your-key-here")
client = OpenAI()


# =============================================================================
# TASK 1: Basic Chat Completion
# Complete this function to send a message to GPT and return the response
# =============================================================================
def ask_gpt(prompt: str) -> str:
    """
    Send a prompt to GPT and return the response.
    
    Args:
        prompt: The question or message to send to GPT
        
    Returns:
        The AI's response as a string
    """
    # TODO: Use client.chat.completions.create() to get a response
    # Hint: Use model="gpt-4o-mini" for a fast, affordable option
    # Hint: The messages parameter should be a list of dicts with "role" and "content"
    
    pass  # Replace this with your code


# =============================================================================
# TASK 2: Conversation with History
# Complete this function to have a multi-turn conversation
# =============================================================================
def chat_with_history(messages: list, new_message: str) -> tuple[str, list]:
    """
    Continue a conversation with GPT, maintaining history.
    
    Args:
        messages: List of previous messages [{"role": "user/assistant", "content": "..."}]
        new_message: The new user message to add
        
    Returns:
        Tuple of (assistant's response, updated messages list)
    """
    # TODO: Add the new_message to messages list with role "user"
    # TODO: Send all messages to the API
    # TODO: Add the assistant's response to messages list
    # TODO: Return the response and updated messages
    
    pass  # Replace this with your code


# =============================================================================
# TASK 3: Creative Application (Choose One!)
# Pick one of these mini-projects to implement
# =============================================================================

# Option A: Story Generator
def generate_story(theme: str, length: str = "short") -> str:
    """Generate a creative story based on a theme."""
    # TODO: Implement this function
    pass


# Option B: Code Explainer
def explain_code(code: str) -> str:
    """Explain what a piece of code does in simple terms."""
    # TODO: Implement this function
    pass


# Option C: Quiz Generator
def generate_quiz(topic: str, num_questions: int = 3) -> list:
    """Generate quiz questions on a topic."""
    # TODO: Implement this function
    pass


# =============================================================================
# Test your implementations below!
# =============================================================================
if __name__ == "__main__":
    # Test Task 1
    print("=== Task 1: Basic Chat ===")
    response = ask_gpt("What is Python in one sentence?")
    print(f"Response: {response}\n")
    
    # Test Task 2
    print("=== Task 2: Chat with History ===")
    messages = []
    response, messages = chat_with_history(messages, "Hi! My name is Alex.")
    print(f"Assistant: {response}")
    response, messages = chat_with_history(messages, "What's my name?")
    print(f"Assistant: {response}\n")
    
    # Test Task 3 (uncomment the one you implemented)
    print("=== Task 3: Creative Application ===")
    # print(generate_story("a robot learning to paint"))
    # print(explain_code("print([x**2 for x in range(10) if x % 2 == 0])"))
    # print(generate_quiz("Python basics", 3))