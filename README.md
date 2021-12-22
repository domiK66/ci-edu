# CI.Edu – Continues Integration in Education
- Szenario: Jenkins CI + Github (public/private Repo)

Schon jetzt wird in der Informatik- bzw. Programmierausbildung am Studiengang IMA mit Jupyter/Nbgrader eine Tool-Chain zur automatisierten Beurteilung von Hausarbeiten verwendet.

Sobald man aber die Jupyter-Umgebung verlässt, wird eine automatische Beurteilung deutlich schwieriger.

In manchen Kursen gelingt dies über zur Verfügung gestellte Unit-Tests, die in den, aus dem lokalen Git (gitima) ausgecheckten, Studierendenprojekten ausgeführt werden.

All dies kann mittels Bash-Script automatisiert werden.

In diesem BÜPA Projekt geht es nun darum, dieses „improvisierte“ Validieren der Abgaben mittels klassischer CI-Pipeline zu ersetzen.

Das heißt am Ende des Abgabefensters wird ein automatisierter CI-Build gestartet, dessen Ergebnis zur Beurteilung einer Heimarbeit führt. 

Wichtiger Aspekt ist die Erstellung von Zugriffsberechtigungen (Hausübungen sollen nur für die betroffenen Studierenden bzw. Studierendenteams sowie Lehrende zugänglich sein).

Ebenso soll es nicht möglich sein, vorgegebene Tests abzuändern (in der CI-Pipline werden die originalen Tests verwendet).
