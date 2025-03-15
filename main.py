import argparse
from ollama import Client

def main():
  parser = argparse.ArgumentParser(prog='siri-kokoAI', description='Siri-Koko AI communicator')
  parser.add_argument('-t', '--text', type=str, required=True, help='Text to be sent to ollama')
  parser.add_argument('--host', type=str, default='http://localhost:11434', help='Ollama host (default: http://localhost:11434)')
  parser.add_argument('-m', '--model', type=str, default='llama3.2', help='Ollama model to use (default: llama3.2). The model must be running on the Ollama server.')
  args = parser.parse_args()

  try:
    client = Client(host=args.host)

    response = client.generate(model=args.model, prompt=args.text)
    print(response.get('response', 'No response received from Koko AI.'))
  except Exception as e:
    print(f"Error: {e}")
    exit(1)

if __name__ == "__main__": 
  main()
