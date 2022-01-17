exerciseName = "swenga-springboot-employee-manager"

studentList = [
    ['Dominik Kainz','https://github.com/domiK66/swenga-springboot-employee-manager '],
    ['Nico Raffling','https://github.com/domiK66/swenga-springboot-employee-manager ']
]

podTemplate(containers: [
    containerTemplate(name: 'gradle', image: 'gradle:6.8-jdk15', command: 'sleep', args: '99d'),
    containerTemplate(name: 'python', image: 'python:latest', command: 'sleep', args: '99d'),
    containerTemplate(name: 'mysql', image: 'mysql:5.7', command: 'sleep', args: '99d', )
]) {
    for(int i = 0; i < studentList.size(); i++) {
        node(POD_LABEL) {
            stage("${studentList[i][0]} github") {
                sh 'mkdir -p student'
                dir("student"){
                    git url: "${studentList[i][1]}", branch: 'main'
                }
            }
            stage('teacher github') {
                sh 'mkdir -p teacher'
                dir("teacher"){
                    git url: 'https://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@github.com/domiK66/ci-edu', branch: 'main'
                }
            }
            stage('cp testfiles') {
                sh "cp teacher/${exerciseName}/EmployeeManagerApplicationTests.kt student/src/test/kotlin/at/fhj/ima/employee/employeemanager/"
            }
            stage('mysql setup') {
                container('mysql') {
                    sh script: '''
                        #!/bin/bash
                        
                        /etc/init.d/mysql start
                        mysql -u root -e "CREATE USER 'swenga'@'127.0.0.1' IDENTIFIED BY 'swenga';"
                        mysql -u root -e "CREATE DATABASE IF NOT EXISTS swenga;"
                        mysql -u root -e "GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, CREATE TEMPORARY TABLES, DROP, INDEX, ALTER, LOCK TABLES ON swenga.* TO 'swenga'@'127.0.0.1';"
                    '''
                }
            }
            stage('gradle test') {
                container('gradle') {
                    dir("student") {
                        sh 'chmod +x gradlew'
                        // sh 'gradle -v'
                        sh 'gradle test'
                        sh 'cat build/test-results/test/TEST-at.fhj.ima.employee.employeemanager.EmployeeManagerApplicationTests.xml'
                    }
                }
            }
            stage('grading.py') {
                container('python') {
                    sh "python teacher/grading2.py student/build/test-results/test/TEST-at.fhj.ima.employee.employeemanager.EmployeeManagerApplicationTests.xml -e teacher/${exerciseName}/${exerciseName} -s \"${studentList[i][0]}\""
                }
            }
            stage('commit results') {
                sh script:'''
                    #!/bin/bash
                    
                    cd teacher
                    git config --global user.email "dominik.kainz@edu.fh-joanneaum.at"
                    git config --global user.name "Jenkins"
                    git add .
                    git commit -m "grading"
                    git push origin main
                '''
            }
        }
    }
}