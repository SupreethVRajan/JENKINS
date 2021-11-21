pipeline { 
agent any
    stages {
        stage('Clone Git Repository') {
            steps {
                git 'https://github.com/SupreethVRajan/JENKINS.git'
            }
        }
        stage('Run Code') {
            steps {
                sh "/usr/bin/python3 HelloWorld.py"
            }
        }
     stage('Test Code') {
            steps {
                sh "/usr/bin/python3 test.py"
            }
        }
    } 
}
