pipeline {
  agent any

  environment {
    IMAGE_NAME      = "python-app"
    GAR_REGISTRY    = "asia-northeast3-docker.pkg.dev"
    GCP_PROJECT_ID  = "rs-2024-00460435-456102"
    GAR_REPOSITORY  = "hwgar"

    // // Jenkins Credentials에 등록한 ID들
    // // 1) GCP 서비스 계정 키(JSON file credential) : gcp-sa-json
    // // 2) Git push용 (username/password or ssh key) : git-push-creds
    // GCP_SA_JSON_CRED = "gcp-sa-json"
    // GIT_PUSH_CRED    = "git-push-creds"  
  }

  
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        sh 'git rev-parse --short HEAD || true'
      }
    }
  
   stage('Ensure main (commit == origin/main)') {
      when { expression { env.SKIP_PIPELINE != 'true' } }
      steps {
        sh '''
          set -e
          git fetch origin main --quiet
          CUR=$(git rev-parse HEAD)
          MAIN=$(git rev-parse origin/main)
          if [ "$CUR" != "$MAIN" ]; then
            echo "ERROR: Not on origin/main. current=$CUR main=$MAIN"
            exit 1
          fi
          echo "OK: building origin/main ($CUR)"
        '''
      }
    }

  
  
    stage('Auth to GCP & Login GAR') {
        steps {
          withCredentials([file(credentialsId: 'gcp-sa-json', variable: 'GCP_KEY')]) {
          sh '''
            gcloud auth activate-service-account --key-file="$GCP_KEY"
            gcloud config set project "${GCP_PROJECT_ID}"
            gcloud auth print-access-token | docker login \
              -u oauth2accesstoken --password-stdin https://${GAR_REGISTRY}
          '''
          }
        }
    }
    
  }
}
