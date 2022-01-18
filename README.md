# CI.Edu: Jenkins 
The project aims to deliver a solution for a grading system that uses a continuous integration pipeline to grade the repositories with test automation of computer science students in different software engineering courses using different server deployments and programming languages.
## 1. Intro to continues integration in education
### 1.1 Problem statement
- Deployment and configuration of software projects in software engineering courses is mainly a manual task, since applications need to be built, tested, deployed and updated frequently, after every exercise where changes are made in the source code and features are updated. 
- Since applications need dependencies, such as build tools, software development kits and web containers, testing for desired features is a time-consuming process that needs a lot of human interaction. 
- The possibility that students change unit tests to their advantage is given when tests are manually executed.

### 1.2 Solution conzept
- Supervisors of software engineering courses need pipeline automation to get the grading of these development environments, so that student's repositories can be tested and checked for completion. 
- The manual task of configuration pipelines that grade computer science students should be as coinvented as possible, so that supervisors are able to automatically grade their students programming skills.

### 1.3 Evaluated technologies
- Jenkins pipelines + Github (public/private Repo) -> http://10.25.2.215:32234
- [Gitlab](https://gitlab.fh-joanneum.at/) pipelines
- [Github Workflows](https://github.com/W0M34T/pipelines) pipelines


## 2. SwengX coding projects
Over the different software engenieering courses, sample projects with sample unit, integration and end-to-end where covered and are used in this project as sample data to test pipeline automation of the deployment. 
### 2.1 Java Enterprise - Gradle
gradle:6.8.3-jdk-15.
- [swenga-calculator](https://github.com/domiK66/swenga-calculator) ✓ -> unit test fails case, gradle test 
- [swenga-guestbook](https://github.com/domiK66/swenga-guestbook) -> n students, unit test passes, gradle test - todo morgen


```gradle
build.gradle {
    test {
        useJUnitPlatform()
        ignoreFailures = true
    }
}
// must be added to build.gralde so the pipeline does not exit on failed tests
```
### 2.2 Spring Boot - Gradle
gradle:6.8.3-jdk-15.
- [swenga-springboot-employee-manager](https://github.com/domiK66/swenga-springboot-employee-manager) ✓ -> spring boot, integration test, mysql db, gradle

```kotlin
build.gradle.kts {
    tasks.withType<Test> {
        useJUnitPlatform()
        ignoreFailures = true
        reports {
            junitXml.isEnabled = true
            html.isEnabled = false
        }
    }
}
// must be added to build.gralde so the pipeline does not exit on failed tests
```
### 2.3 Python
the testing tool [pytest](https://docs.pytest.org/en/6.2.x/) is used to generate XML reports.
- [swengs-exercise1](https://github.com/domiK66/swengs-exercise1) ✓ -> for n students, simple unit test 
- [swengs-exercise2](https://github.com/domiK66/swengs-exercise2) -> n students, unit test passes, pytest - todo morgen

### 2.4 Django 
- [swengs-exercise3](https://github.com/domiK66/swengs-exercise3) ✓ -> django db, django-pytest
- [swengs-exercise4](https://github.com/domiK66/swengs-exercise4) ✓ -> regression testing, django db, django-pytest

```py
pytest.ini {
    [pytest]
    DJANGO_SETTINGS_MODULE = movie_site.settings
}
# pytest configuration
```

### 2.5 Angular

- [swengs-ima-employees](https://github.com/domiK66/swengs-ima-employees)

https://github.com/karma-runner/karma-junit-reporter

https://testing-angular.com/angular-testing-principles/



## 3. Jenkins & Kubernetes
### 3.1 Installing jenkins
- Installation of [Jenkins](https://www.jenkins.io/) in an [Kubernetes](https://kubernetes.io/) cluster
- Jenkins namespace
- Deployment per .yaml file or HELM

- Jenkins IP: http://10.25.2.215:32234

- credentials: username: admin / pw: def563d1312043b1824722a70fb7965b


### 3.2 Kubernetes plugin

- config.yml kubernetes admin credentials

- createing pods with docker images

## 4. Pipelines

### 4.1 Groovy sytnax + pod tempaltes
https://www.tutorialspoint.com/groovy/index.htm


### 4.2 Teacher student conzept


### 4.3 How to test
- Bash Script Pipelines für verschiedene Technologien & Programmiersprachen
- Builden und Testen der Studenten-Projekte in einzelnen Pods im [Kubernetes](https://kubernetes.io/) 
- Generieren von [JUnit](https://junit.org/junit5/) XML reports über die Testergebnisse
- Zusammenführen aller reports der Studierenen pro Hausarbeit 

https://hub.docker.com/

# BÜPA 

## Aufgabenstellung:
Schon jetzt wird in der Informatik- bzw. Programmierausbildung am Studiengang IMA mit Jupyter/Nbgrader eine Tool-Chain zur automatisierten Beurteilung von Hausarbeiten verwendet. Sobald man aber die Jupyter-Umgebung verlässt, wird eine automatische Beurteilung deutlich schwieriger.
All dies kann mittels Bash-Script automatisiert werden!

In diesem BÜPA Projekt geht es nun darum, das Validieren der Abgaben mittels klassischer CI-Pipeline zu ersetzen. 
- Das heißt am Ende des Abgabefensters wird ein automatisierter CI-Build gestartet, dessen Ergebnis zur Beurteilung einer Heimarbeit führt. 
- Wichtiger Aspekt ist die Erstellung von Zugriffsberechtigungen (Hausübungen sollen nur für die betroffenen Studierenden bzw. Studierendenteams sowie Lehrende zugänglich sein).
- Ebenso soll es nicht möglich sein, vorgegebene Tests abzuändern (in der CI-Pipline werden die originalen Tests verwendet).


## Docs
#### First Meeting
to evaulate:
- Database support, 
- Access rights
- Multiple repos in pipeline
- Cost of solution,
- Language Support, 
- Integration Test ...
- public private repo
- local online