<h1 align="center">
  Mentra
</h1>

<h2 align="center">
  An AI-powered journal chatbot for your personal well being - Mentor meets mantra.
</h2>

Try it out here: https://mentra.onrender.com/
<br>
Devpost link: https://devpost.com/software/mentra

<p align="center">
  <img src="screenshots/mentra.png" alt="logo" width="800"/>
</p>

<br>

## Contributors
- Drue Nooyen
- Andrea Fung
- Jianding Bai
- Stephanie Xue
  
<br>

## Inspiration
Journaling has always been a powerful tool for self-expression, reflection, and personal growth. It allows us to process our thoughts, navigate challenges, and track our journey over time. Inspired by this timeless practice, we wanted to create something that not only preserves these experiences but also enhances them with meaningful, intelligent feedback. Our goal was to transform journaling into an interactive, insightful, and uplifting experience. Through Mentra, we hope to empower individuals to better understand themselves, gain clarity, and improve their well-being.

<br>

## What it does
Our application revolutionizes the traditional journaling experience by integrating intelligent insights and advice tailored to the user's needs. It allows users to log their thoughts, emotions, and experiences while receiving thoughtful, insightful, and actionable responses that support self-reflection and encourage personal growth and well-being.

<br>

## Features

- Landing and login page to welcome the user and allow them to login to their account
![Login](./screenshots/login.png?raw=true "Login")

- Registration page for users to register for a new account
![Register](./screenshots/register.png?raw=true "Register")

- Chat page allows the users to select their desired category of journal responses and input their journal entry
![Chat](./screenshots/chat.png?raw=true "Chat")

![Response](./screenshots/response.png?raw=true "Response")

![History Selection](./screenshots/history_category.png?raw=true "History Selection")

![History](./screenshots/history.png?raw=true "History")

<br>

## How we built it
- Front-end: The frontend was built with HTML5, CSS3, and JavaScript to provide a smooth and responsive user experience. 
- Back-end & database: We developed this application using Django and Python3 for the backend, leveraging SQLite as our database to store journal entries, categories of entries, and user data. 
- API: We integrated Google's Gemini 2.0 Flash generative AI API
- Deployment: We deployed the application on Render,  ensuring seamless accessibility for users.

<br>

## How to Run Locally
- Install the latest version of node.js (JavaScript runtime server)
- Install the latest version of npm (JavaScript package manager)
- cd into the project folder and run 'npm install'
- The web application can be run on your local server by typing in the command line 'npm run dev'

<br>

## Challenges we ran into
Some challenges we ran into include figuring out how to link separate accounts for different users. We also encountered issues with integrating the Gemini 2.0 Flash API into our system. Additionally, it was also challenging trying to figure out how to implement the API key into an environment variable for security and safety. We also faced the challenge of deploying our application on Render using our defined environment variables.

<br>

## Accomplishments that we're proud of
One of our biggest achievements was successfully integrating the Gemini 2.0 Flash API into our application. For many of us, this was our first experience working with an AI-powered API, and it was rewarding to see how it could enhance the user experience. This project also reinforced our ability to work collaboratively, problem-solve, and bring an idea to life.

<br>

## What we learned
We gained valuable insights into both technical development and teamwork. We deepened our understanding of backend development with Django, Python3 and SQLite while also improving our frontend skills with HTML5, CSS3, and JavaScript. Integrating the Gemini 2.0 Flash API was a new challenge, and through trial and error, we learned how to effectively handle API authentication and ensure successful communication between our application and the AI model.

<br>

## What's next for Mentra
For Mentra, we want to expand and add more features and functions that can help users improve their wellbeing. This can include chat-lines, additional categories, levels of response depth, goals tracking and/or progress summary. It would be great to add more accessibility features such as text to speech and speech to text in the future as well. Full Mentra ahead!
