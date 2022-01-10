exerciseName = "swenga-calculator"

studentList = [
    ['Dominik Kainz','https://github.com/domiK66/swenga-calculator'],
    ['Nico Raffling','https://github.com/domiK66/swenga-calculator']
]

podTemplate(containers: [
    containerTemplate(name: 'tomcat', image: 'tomcat:latest', command: 'sleep', args: '99d'),
    containerTemplate(name: 'gradle', image: 'gradle:6.8.3', command: 'sleep', args: '99d'),
    
    containerTemplate(name: 'python', image: 'python:latest', command: 'sleep', args: '99d')
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
            stage('cp testfiles'){
                sh "cp teacher/${exerciseName}/CalculatorTest.kt student/src/test/kotlin/at/fhj/ima/swenga_calculator/entity"
            }
            stage('gradle test') {
                container('gradle') {
                    dir("student") {
                        sh 'chmod +x gradlew'
                        // sh 'gradle -v'
                        sh 'gradle test'
                        // sh 'cat ./build/test-results/test/TEST-at.fhj.ima.swenga_calculator.entity.CalculatorTest.xml'
                    }
                }
            }
            stage('grading.py') {
                container('python') {
                    sh "python teacher/grading.py TEST-at.fhj.ima.swenga_calculator.entity.CalculatorTest -d student/build/test-results/test >> teacher/${exerciseName}/result.txt"
                }
            }
            stage('commit results') {
                sh script:'''
                    #!/bin/bash
    
                    git config --global user.email "dominik.kainz@edu.fh-joanneaum.at"
                    git config --global user.name "Dominik Kainz"
                    git add .
                    git commit -m "grading"
                    git push origin main
                '''
            }
        }
    }
}