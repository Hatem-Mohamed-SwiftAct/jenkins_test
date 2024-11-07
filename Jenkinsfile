pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo "Let's Start Testing"
                bat 'pytest first_test.py --junitxml=test.xml'
            }
        }

        stage('Report') {
            steps {
                junit 'test.xml'
            }
        }
    }
}
