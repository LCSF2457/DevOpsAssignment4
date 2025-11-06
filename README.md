# Flask App
A simple Flask App to practice environment variables, Docker, Github Actions (CI/CD)

## Features
- Simple Styled Flask App
- Github Actions CI/CD + Dependabot
- Docker Containerization
- Docker Compose
- Environment Variables + Github

## Project Structure
```
├── .github/
│   ├── workflows/
│   │   └── ci.yml      # github actions
│   └── dependabot.yml  # dependabot
├── static              # static assets
├── templates           # flask templates
├── app.py              # main app
├── Dockerfile          # docker image
├── docker-compose.yml  # docker compose configs
├── requirements.txt    # python deps
├── .env.example        # example env (.env is ignored)
├── .env                # env variables
├── .gitignore          # git ignore
└── README.md
```

## Setup
1. Clone repo
```bash
git clone https://github.com/LCSF2457/DevOpsAssignment4
cd DevOpsAssignment4
```

2. Create env file from env.example

3. Run application (make sure Docker is running)
```bash
docker-compose up
```
- Go to http://localhost:5000/
