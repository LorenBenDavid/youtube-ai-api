# YouTube Q\&A AI

This is a Flask web app that allows users to ask questions about the content of any YouTube video. The app automatically retrieves the transcript from the video and uses OpenAI to provide concise answers.

## 🚀 Features

* Input a YouTube URL and a question
* Automatically fetches transcript from the video
* Uses OpenAI's GPT model to answer the question based on transcript
* Built with Flask, LangChain, and YouTube Transcript API
* Responsive UI with Tailwind CSS

## 🧠 How It Works

1. User pastes a YouTube video link and types a question
2. The backend uses `youtube-transcript-api` to fetch the transcript
3. The transcript is split into chunks and embedded using `OpenAIEmbeddings`
4. A vector store (FAISS) is created to allow semantic search
5. LangChain selects the most relevant chunks to answer the question using GPT-3.5

## 🧱 Stack

* Python 3.11+
* Flask
* LangChain
* OpenAI API
* FAISS
* YouTube Transcript API
* TailwindCSS (via CDN)

## 🌐 Live Demo

Deploy on Railway, Render, or your own VPS (e.g. AWS EC2).

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/<your-username>/youtube-ai-api.git
cd youtube-ai-api
```

### 2. Set up virtual environment

```bash
python3 -m venv env
source env/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your OpenAI API key

Create a `.env` file with:

```env
OPENAI_API_KEY=sk-...
```

### 5. Run the app

```bash
python app.py
```

Go to `http://localhost:5050`

## 🐳 Optional: Docker Setup

Coming soon

## 📝 Deployment Tips

* For Railway: set environment variable `OPENAI_API_KEY`
* YouTube Transcript API may be blocked on cloud IPs like Render or Railway
* For reliable deployments, use a VPS (like AWS EC2 or Hetzner)

## 📄 License

MIT License

## 🙋‍♂️ Author

[Loren Ben David](https://github.com/LorenBenDavid)
