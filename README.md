# SiriKokoAI  

**SiriKokoAI** is a simple script that allows you to interact with **Ollama** via **Apple Shortcuts** and **SSH**, enabling you to send text queries and receive AI-generated responses. This script is designed for quick interactions and does not maintain chat history.  

## 🚀 Features  
- Uses **Ollama** as the backend AI model  
- Runs on a remote server via **SSH**  
- Can be executed directly from **Siri** using a pre-configured shortcut  
- Supports basic query execution with a chosen **Ollama model**  

## 📋 Requirements  
Before using SiriKokoAI, ensure you have:  
- **Ollama** installed and running on your server. Follow the setup guide: [Ollama Installation & Usage](https://ollama.com)  
- A **server with Python** and the required dependencies installed  
- SSH access to the server (username, password, and script path must be configured)  
- Apple **Shortcuts** installed on your iPhone/iPad  

## 🛠 Installation  

### 1️⃣ Install Dependencies on Your Server  
Connect to your server and run:  
```bash
pip install ollama argparse
```

### 2️⃣ Download & Set Up Siri Shortcut  
Install the **Siri Shortcut** from this link:  
🔗 [Siri Shortcut for SiriKokoAI](https://www.icloud.com/shortcuts/0e44f5eddd2640e5b45927fab5dd833c)  

### 3️⃣ Configure Shortcut Parameters  
Inside the **Shortcut**, configure:  
- **Ollama Host:** The URL where Ollama is running  
- **SSH Connection:** Server IP, username, and password  
- **Script Path:** The location of `main.py` on your server  

### 4️⃣ Run the Script via Siri  
Simply say:  
🗣 **"Hey Siri, Local AI Assistant"**  
Siri will then trigger the shortcut and start the conversation with the AI.  

## 📝 Usage  
The script is executed via SSH and runs:  
```bash
python3 ~/kokoai/main.py --host "OLLAMA_HOST" -m "MODEL" -t "USER_INPUT"
```
Example:  
```bash
python3 ~/kokoai/main.py --host "http://localhost:11434" -m "llama3.2" -t "What is the capital of France?"
```

## ⚖️ License  
This project is licensed under the **Apache 2.0 License**. See [LICENSE](LICENSE) for details.  
