# Welcome!

- This is our repository that we will use to build the widget, the `backend` and `frontend` is in their respective folders
- Never push to `main` branch! Whenever you start working on a ticket, create a new branch and then push it to the branch you just created
- For help Stack Overflow, Github and [FastAPI discord](https://discord.gg/VQjSZaeJmf) and [Vue.js discord](https://discord.com/invite/HBherRA) are excellent
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

Also thanks to the awesomeness of FastAPI, if you go to `localhost:(whatever port number you specified, default is 80)\docs`. You can see all the available endpoints plus query parameters and variables. Very easy to play around with it and will help you gain a better understanding of what's going on!

## Considerations

- Create a better folder structure
- Put repeated work of sending request and encoding json in middleware

## Technologies used

- Vue.js for frontend, Bulman for CSS framework, Vercel for frontend deployment
- FastAPI for backend deployed using Uvicorn (should've used Gunicorn) being run behind a CDN (Cloudflare) for protection against DDOS attacks
- Deployed using Docker on a DigitalOcean server and we have our API url from Namecheap
