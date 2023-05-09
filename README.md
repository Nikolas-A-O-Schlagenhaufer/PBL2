# PBL2 - ANÁLISE DE COMPORTAMENTO OCULAR E CAPTAÇÃO DE SINAIS VIA ELETRODOS
Repositório criado para a segunda atividade somativa da disciplina de Biônica do 9° período do curso de Engenharia Mecatrônica da PUC-PR.
## Integrantes
- Mateus Uriel Graunke Barroso
- Nikolas Arnfried Olsson Schlagenhaufer
- Pedro Vicenzo Ceccatto
## Arquivos/Pastas
- data: pasta com os dados brutos;
  - mental: pasta com dados do teste EEG during mental arithmetic tasks;
  - motor_movement: pasta com dados do teste EEG motor movement/imaginary dataset;
- treated_data: pasta com os dados tratados;
  - mental: pasta com dados do teste EEG during mental arithmetic tasks;
  - motor_movement: pasta com dados do teste EEG motor movement/imaginary dataset;
- app.py: código principal do aplicativo desenvolvido;
- data_set: código da classe DataSet;
- decision_tree.joblib: modelo da árvore de decisão treinada;
- intervalos.py: intervalos em que os pacientes escolhidos para o treinamento estavam piscando;
- main: código principal do treinamento da IA e do tratamento dos dados;
- study.py: código da classe Study;
- subject.py: código da classe Subject;
- test.py: código da classe Test.
## Instruções para rodar o programa com a interface visual
Primeiramente, deve-se selecionar o paciente a ser testado, modificando o valor da variável pessoa no arquivo app.py, encontrada nas linhas iniciais do código.

![image](https://github.com/Nikolas-A-O-Schlagenhaufer/PBL2/assets/95252298/ed8fe9b5-0d0d-41bb-8958-c64c87b5301d)

Para rodar o programa, rodar no terminal o código app.py utilizando o comando: `python app.py`.

Depois de alguns segundo a tela já irá aparecer e o programa começará a funcionar.
