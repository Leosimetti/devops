pipeline {
  agent {docker {image 'python:3.8-slim'}}
  stages {  // Define the individual processes, or stages, of your CI pipeline
      stage('Checkout') { // Checkout (git clone ...) the projects repository
        steps {
          checkout scm
        }
      }
      stage('Setup') { // Install any dependencies you need to perform testing
        steps {
        dir('app_python'){
          script {
            sh """
            pip3 install -r requirements.txt
            """
          }
        }
        }
      }
      stage('Unit Testing') { // Perform unit testing
        steps {
        dir('app_python'){
          script {
            sh """
            pytest
            """
          }
        }
        }
      }
  }
}
