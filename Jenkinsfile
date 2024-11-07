pipeline {
    agent any

    stages {
        stage('Test') {
            steps {
                echo "Let's Start Testing"
                bat 'pytest first_test.py --junitxml=test.xml'
            }
        }

        post {
            junit 'test.xml'
        }
    }
}
