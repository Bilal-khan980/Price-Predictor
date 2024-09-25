pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                // Pulling the code from the repository
                git 'https://github.com/your-repo/ml-project.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Installing project dependencies
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                // Running tests to ensure everything works
                sh 'python -m unittest discover tests'
            }
        }
        stage('Build Model') {
            steps {
                // Train the model (if training is part of deployment)
                sh 'python train_model.py'
            }
        }
        stage('Deploy to Production') {
            steps {
                // Deploy your project (e.g., API, frontend) to the production server
                // Example using Docker or Flask API
                sh 'docker build -t ml-app .'
                sh 'docker run -d -p 5000:5000 ml-app'
            }
        }
    }
}
