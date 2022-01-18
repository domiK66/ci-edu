# CI.Edu: Jenkins 
## Continues Integration in Education:
 
- Szenario: [Jenkins](https://www.jenkins.io/) Countinous Integration + Github (public/private Repo)
- Szenario: https://gitlab.fh-joanneum.at/
- Szenario Max

### 1.1 Installing jenkins
- Installation von [Jenkins](https://www.jenkins.io/) im "https://pimakub06.fh-joanneum.at/" [Kubernetes](https://kubernetes.io/) Cluster
- Jenkins IP: http://10.25.2.215:32234

- admin: def563d1312043b1824722a70fb7965b

- JenkinsJack VsCode https://marketplace.visualstudio.com/items?itemName=tabeyti.jenkins-jack

### 1.2 Kubernetes plugin

- config.yml kubernetes admin credenetials

- createing pods with docker images

### 1.3 Groovy sytnax + pod tempaltes
https://www.tutorialspoint.com/groovy/index.htm

todo: snippet

### 1.4 Teacher student conzept
todo:

### 1.5 How to test
todo deutsch:
- Bash Script Pipelines für verschiedene Technologien & Programmiersprachen
- Builden und Testen der Studenten-Projekte in einzelnen Pods im [Kubernetes](https://kubernetes.io/) 
- Generieren von [JUnit](https://junit.org/junit5/) XML reports über die Testergebnisse
- Zusammenführen aller reports der Studierenen pro Hausarbeit 

https://hub.docker.com/

# IMA coding projects

### Python
Bei Python und Django Projekten wird das testing tool [pytest](https://docs.pytest.org/en/6.2.x/) zum generieren von XML reports verwendet.
- [swengs-exercise1](https://github.com/domiK66/swengs-exercise1) ✓ -> for n students, simple unit test 
- [swengs-exercise2](https://github.com/domiK66/swengs-exercise2) -> n students, unit test passes, pytest - todo morgen

### Django 
- [swengs-exercise3](https://github.com/domiK66/swengs-exercise3) ✓ -> django db, django-pytest
- [swengs-exercise4](https://github.com/domiK66/swengs-exercise4) ✓ -> regression testing, django db, django-pytest

```
pytest.ini {
    [pytest]
    DJANGO_SETTINGS_MODULE = movie_site.settings
}
```



### Java Enterprise - Gradle

- [swenga-calculator](https://github.com/domiK66/swenga-calculator) ✓ -> unit test fails case, gradle test 
- [swenga-guestbook](https://github.com/domiK66/swenga-guestbook) -> n students, unit test passes, gradle test - todo morgen

```
build.gradle {
    test {
        useJUnitPlatform()
        ignoreFailures = true
    }
}
```

### Spring Boot - Gradle

- [swenga-springboot-employee-manager](https://github.com/domiK66/swenga-springboot-employee-manager) ✓ -> spring boot, integration test, mysql db, gradle

```
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
```


### Angular

https://github.com/karma-runner/karma-junit-reporter

https://testing-angular.com/angular-testing-principles/


### Grading2.py 
peter ist super

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
Zu evalieren: Database Support, Language Support, Integration Test ...
