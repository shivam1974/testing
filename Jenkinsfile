pipeline {
  agent any 
  stages {
    stage("Compile") {
      steps {
        //pip install requirements.txt echo "Python compile done"
        echo "hello"
      } 
    } 
    stage("Unit test") {
      steps {
        sh "python test.py" 
      }
    }
  }
}
