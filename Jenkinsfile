pipeline {
    agent any

    stages {

        stage('Check Environment') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pip install -r requirements.txt'
            }
        }

        stage('Run Automated Tests') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" -m pytest -v'
            }
        }

        stage('Run Application') {
            steps {
                bat '"C:\\Users\\lenovo\\AppData\\Local\\Programs\\Python\\Python311\\python.exe" hello.py'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully.'
        }

        failure {
            echo 'FAILED: Check the Console Output for errors.'
        }
    }
}
