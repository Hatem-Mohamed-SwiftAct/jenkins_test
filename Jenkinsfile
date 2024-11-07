pipeline {
    agent {label 'Test'}

    stages {
        stage('Setup') {
            steps {
                echo "Let's Start Setup"

                bat '''
                pip install pytest
                '''
            }
        }

        stage('Test') {
            steps {
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                    bat '''
                    pytest first_test.py -vs --junitxml=test.xml
                    '''
                }
            }
        }
        
        stage('Report') {
            steps {
                junit 'test.xml'
            }
        }
    }
}
