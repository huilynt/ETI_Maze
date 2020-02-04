pipeline {
    agent {
        dockerfile true
    }
    stages {
        stage('Test') {
            steps {
                sh 'pytest -v --cov --junitxml=results.xml'
            }
        }
    }
}