pipeline {
  agent any
  stages {
    stage('Checkout') { steps { checkout scm } }
    stage('Build')    { steps { echo "build" } }
    stage('Test')     { steps { echo "test" } }
  }
}
