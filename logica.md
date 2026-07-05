1. Usuário informa a URL - feito
2. O crawler coloca a URL inicial em uma fila - feito
3. Visita a página -  feito 
4. Extrai links e scripts
5. Verifica se cada link está dentro do escopo
6. Evita visitar URL repetida
7. Continua até a profundidade configurada
8. Baixa arquivos JS encontrados
9. Procura possíveis secrets hardcoded
10. Redige os valores encontrados
11. Gera report.md e report.json