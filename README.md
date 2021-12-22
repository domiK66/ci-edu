# CI.Edu – Continues Integration in Education
Szenario: [Jenkins](https://www.jenkins.io/) Countinous Integration + Github (public/private Repo)

## Aufgabenstellung:
Schon jetzt wird in der Informatik- bzw. Programmierausbildung am Studiengang IMA mit Jupyter/Nbgrader eine Tool-Chain zur automatisierten Beurteilung von Hausarbeiten verwendet. Sobald man aber die Jupyter-Umgebung verlässt, wird eine automatische Beurteilung deutlich schwieriger.
All dies kann mittels Bash-Script automatisiert werden!

In diesem BÜPA Projekt geht es nun darum, das Validieren der Abgaben mittels klassischer CI-Pipeline zu ersetzen. 
- Das heißt am Ende des Abgabefensters wird ein automatisierter CI-Build gestartet, dessen Ergebnis zur Beurteilung einer Heimarbeit führt. 
- Wichtiger Aspekt ist die Erstellung von Zugriffsberechtigungen (Hausübungen sollen nur für die betroffenen Studierenden bzw. Studierendenteams sowie Lehrende zugänglich sein).
- Ebenso soll es nicht möglich sein, vorgegebene Tests abzuändern (in der CI-Pipline werden die originalen Tests verwendet).

Zu evalieren: Database Support, Language Support, Integration Test ...

## Lösungsweg:
- Installation von [Jenkins](https://www.jenkins.io/) im "https://pimakub06.fh-joanneum.at/" [Kubernetes](https://kubernetes.io/) Cluster
- Jenkins IP: http://10.25.2.215:32234
- Bash Script Pipelines für verschiedene Technologien & Programmiersprachen
- Builden und Testen der Studenten-Projekte in einzelnen Pods im [Kubernetes](https://kubernetes.io/) 
- Generieren von [JUnit](https://junit.org/junit5/) XML reports über die Testergebnisse
- Zusammenführen aller reports der Studierenen pro Hausarbeit



### Python & Django
Bei Python und Django Projekten wird das testing tool [pytest](https://docs.pytest.org/en/6.2.x/) zum generieren von XML reports verwendet.
- [swengs-exercise1](https://github.com/domiK66/swengs-exercise1)
- [swengs-exercise2](https://github.com/domiK66/swengs-exercise2)
- [swengs-exercise3](https://github.com/domiK66/swengs-exercise3) ✓ 
- [swengs-exercise4](https://github.com/domiK66/swengs-exercise4)

### Angular

### Java Enterprise

- [swenga-calculator](https://github.com/domiK66/swenga-calculator)
- [swenga-guestbook](https://github.com/domiK66/swenga-guestbook)

### Spring Boot

- [swenga-springboot-employee-manager](https://github.com/domiK66/swenga-springboot-employee-manager)

