pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                echo "Let's Start Testing"

                bat '''
                python -m venv venv
                source venv/bin/activate
                pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                bat '''
                source venv/bin/activate
                pytest first_test.py -v --junitxml=test.xml
                '''
            }
        }

        stage('Report') {
            steps {
                junit 'test.xml'
            }
        }
    }
}
