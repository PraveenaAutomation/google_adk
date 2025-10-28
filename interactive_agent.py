#!/usr/bin/env python3
"""
Interactive Google ADK Multi-Tool Agent
"""

import sys
import os

# Add the multi_tool_agent directory to the path
sys.path.append(os.path.join(os.path.dirname(__file__), 'multi_tool_agent'))

from multi_tool_agent.agent import root_agent

def main():
    print("🤖 Google ADK Multi-Tool Agent - Interactive Mode")
    print("=" * 50)
    print("Available tools: Weather and Time")
    print("Supported city: New York")
    print("Type 'quit' or 'exit' to stop")
    print("=" * 50)
    
    while True:
        try:
            # Get user input
            user_input = input("\n💬 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("👋 Goodbye!")
                break
            
            if not user_input:
                continue
            
            # Run the agent
            print("🤖 Agent: Thinking...")
            response = root_agent.run(user_input)
            print(f"🤖 Agent: {response}")
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()



