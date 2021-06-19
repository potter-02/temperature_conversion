#!/usr/bin/env groovy
build_dependents_repo = 'https://github.com/potter-02/temperature_conversion.git'
pipeline {
//   agent {
//     label 'Jenkins slave'
//   }
  environment {
    EMAIL_TO = 'harshamandava02@gmail.com'
  }

  stages {
    stage('cleanworkspace') {
      steps {
        cleanWs()
      }
    }

    stage('git checkout'){
    steps {
      checkout([$class: 'GitSCM', branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: '95364d96-038a-4a70-a9cb-3b34e89c3815', url: 'https://github.com/potter-02/temperature_conversion.git']]])
        }
  }
      stage('dependency installs') {
        steps {
                sh 'pip install -r requirements.txt'
        }   
    }
      stage('python build'){
      steps {
        cd $WORKSPACE
        sh 'temperature.py'
      }
    }
//  post {
//     failure {
//         emailtext body: 'build status body'
//         to: 'harshamandava02@gmail.com'
//         subject: 'Build success/failed/unstable/etc $PROJECT_NAME - $BUILD_NUMBER'
//       }
//     }
  }
}
