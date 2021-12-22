studentList = [
    ['Dominik Kainz','https://github.com/domiK66/swengs-exercise3'],
    ['Nico Raffling','https://github.com/domiK66/swengs-exercise3']
]
podTemplate(
    containers: [ 
        containerTemplate(name: 'python', image: 'python:latest', command: 'sleep', args: '99d') 
    ]
) {
    for(int i = 0; i < studentList.size(); i++) {
        node(POD_LABEL) {
            stage("Checkout ${studentList[i][0]} Github") {
                sh 'mkdir -p student'
                dir("student"){
                    git url: "${studentList[i][1]}", branch: 'main'
                }
            }
            stage('Checkout Teacher Github') {
                sh 'mkdir -p teacher'
                dir("teacher"){
                    git url: 'https://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@github.com/domiK66/ci-edu', branch: 'main'
                }
            }
            container('python') {
                dir("student"){
                    stage('Venv Django Setup') {
                        sh script:'''
                            #!/bin/bash
                            pip install virtualenv
                            virtualenv newenv
                            . newenv/bin/activate
                            
                            pip install django
                            cd apps
                            cd yamod-0.5
                            pip install -e .
                            cd ..
                            cd ..
                            cd movie_site
                            python manage.py migrate
                            
                            deactivate
                        '''
                    }
                }
                stage('Copy Testfiles'){
                    sh script: '''
                        #!/bin/bash
                        
                        cp teacher/swengs-exercise3/test_exercise3.py student/movie_site/
                    '''
                }
                dir("student"){
                    stage('Test & Junit XML Reports') {
                        sh script:'''
                            #!/bin/bash
                            . newenv/bin/activate
                            
                            pip install -U pytest-django
                            cd movie_site
                            export PYTHONPATH="$PYTHONPATH:."
                            python -c "import sys; print(sys.path)"
                            
                            pytest --junitxml=report.xml
                            
                            deactivate
                        '''
                    }
                }
                stage('Commit Grading'){
                    sh script:'''
                        #!/bin/bash
                        
                        python teacher/grading.py report -d student/movie_site >> teacher/swengs-exercise3/result.txt
                        
                        cd teacher
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
}