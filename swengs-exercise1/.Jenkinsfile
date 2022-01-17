exerciseName = "swengs-exercise1"

studentList = [
    ['Dominik Kainz','https://github.com/domiK66/swengs-exercise1'],
    ['Nico Raffling','https://github.com/domiK66/swengs-exercise1']
]

podTemplate(containers: [ 
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
            stage('cp testfiles') {
                 sh "cp teacher/${exerciseName}/test_exercise1.py student/ "
            }
            stage('pytest') {
               container('python') {
                    dir("student"){
                        sh script:'''
                            #!/bin/bash
                            pip install virtualenv
                            virtualenv newenv
                            . newenv/bin/activate
                                
                            pip install -U pytest
                            export PYTHONPATH="$PYTHONPATH:."
                            python -c "import sys;print(sys.path)"
                            pytest --junitxml=report.xml
                                
                            deactivate
                        '''
                    }
                }  
            }
            stage('grading.py') {
                container('python') {
                    sh "python teacher/grading2.py student/report.xml -e teacher/${exerciseName}/${exerciseName} -s \"${studentList[i][0]}\" >> teacher/${exerciseName}/result.txt"
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