pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('test') {
            steps {
                sh 'pytest -v --cov'
            }
        }
    }
}