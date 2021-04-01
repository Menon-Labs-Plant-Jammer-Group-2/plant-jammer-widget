# Welcome!

- This is our repository that we will use to build the widget, the `backend` and `frontend` is in their respective folders
- Never push to `main` branch! Whenever you start working on a ticket, create a new branch and then push it to the branch you just created
- For help Stack Overflow, Github and [FastAPI discord](!https://discord.gg/VQjSZaeJmf) and [Vue.js discord](!https://discord.com/invite/HBherRA) are excellent
- Remember to store any confidential information like the API key in `.env` file, we don't want this to be released to the public

## Getting started

### Frontend

To get the frontend up and running

```bash
cd frontend
npm run serve
```

You should be able to go to `http://localhost:8080/` and see the frontend there

### Backend

To get the backend up and running

```bash
cd backend
source bin/activate # to activate the virtual environment
python3 -m pip install -r requirements.txt # to install all dependencies
uvicorn main:app --reload # run the server
```

To use the API key, you must run `export=API_KEY # replace the actual API key with API_KEY` and make sure that a `.env` file exists in the `backend` folder so that the backend code will be able to access the environment variable from the operating system

## Technologies used

- Vue.js for frontend
- FastAPI for backend
