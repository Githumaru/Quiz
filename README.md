# Quiz
A Django application for creating and managing quizzes using MongoDB

# Overview

The Quiz project is a web application built on the Django framework. It accepts POST requests in the format {"questions_num": integer}.
Upon receiving the request, the service fetches the specified number of quiz questions from a public API (English quiz questions) at https://jservice.io/api/random?count=1.
The retrieved questions are then stored in a database.

# Installation

## Clone the repository to your local machine:
```
git clone https://github.com/Githumaru/Quiz.git
```

## Navigate to the project directory:
```
cd quiz_project
```

## Run the project using Docker Compose:
```
docker-compose up
```

## Open your web browser and go to http://localhost:8000 to access the application.

# Usage

Accessing the application: Once you have launched your web application, it will be accessible at http://localhost:8000 in your web browser.

Creating quiz questions: To create new quiz questions, you can send a POST request to http://localhost:8000/quiz/create/ with the parameter questions_num, indicating the number of questions you want to add. For example, http://localhost:8000/quiz/create/5/.

Getting the latest question: To retrieve the last saved quiz question, you can send a GET request to http://localhost:8000/quiz/latest/. You will receive information about the most recent question in response.
