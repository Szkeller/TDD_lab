  pipeline {
  agent any
  stages {
     stage("build") {
      steps {
           echo 'build python file...'
           sh 'pip install -r requirement.txt '
      }
    }
    stage("test") {
      steps {
           echo 'test python file...'
           sh 'pytest -v'
      }
    }
  }
}
