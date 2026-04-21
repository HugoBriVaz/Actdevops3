pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-jenkins-app"
        CONTAINER_NAME = "flask-jenkins-container"
    }

    stages {
        stage('Clonar repositorio') {
            steps {
                checkout scm
            }
        }

        stage('Construir imagen Docker') {
            steps {
                // El --no-cache asegura que Docker lea tu nuevo mensaje de app.py
                sh 'docker build --no-cache -t $IMAGE_NAME ./app'
            }
        }

        stage('Limpiar y Desplegar') {
            steps {
                // Detenemos y borramos el contenedor viejo
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
                
                // Ejecutamos el nuevo
                sh 'docker run -d --name $CONTAINER_NAME -p 5000:5000 $IMAGE_NAME'
            }
        }

        stage('Validar despliegue') {
            steps {
                sh 'docker ps'
                // Esperamos 5 segundos a que Flask termine de arrancar
                sleep 5
                // Probamos la ruta principal (/) ya que es donde tienes tu mensaje
                sh 'curl http://localhost:5000/'
            }
        }
    }

    post {
        success {
            echo '¡Despliegue automático exitoso!'
        }
        failure {
            echo 'El pipeline falló. Revisa el Console Output.'
        }
    }
}
