pipeline {
    agent any

    environment {
        DOCKER_IMAGE = '<your-dockerhub-username>/my-python-app:latest' // Replace with your Docker Hub username
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/MounikaRangisetty/app.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $DOCKER_IMAGE .'
            }
        }

        stage('Push Docker Image') {
            steps {
                sh 'docker push $DOCKER_IMAGE'
            }
        }

        stage('Sync with ArgoCD') {
            steps {
                sh 'argocd app sync app'
            }
        }
    }

    post {
        always {
            cleanWs() // Cleans up the workspace after the job is done
        }
    }
}
