def myImage
pipeline {
  agent any
  environment {
        DOCKER_REP = credentials('docker_repository')
        DOCKER_USER = credentials('docker_user')
  }

  stages {
    stage('Testing and linting') {
      agent {
        docker {
          image 'python:3.8-slim'
          reuseNode true
        }
      }
      steps{
        checkout scm

        dir('app_python'){
          script {
            sh """
            pip3 install -r requirements.txt
            pytest
            pip3 install pylama
            pylama ./app_python/src
            """
          }
        }
      }
    }

    stage("Build image"){
      agent any
      steps{
          checkout scm
          dir('app_python'){
              script{
                  myImage = docker.build('$DOCKER_USER/$DOCKER_REP', "--target build .")
              }
          }
      }
    }

    stage("Publish image"){
      agent any
      steps{
        script{
          withDockerRegistry(credentialsId: 'docker_pair', url: '') {
            myImage.push()
          }
        }
      }
    }

  }
}
