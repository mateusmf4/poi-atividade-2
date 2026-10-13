# Atividade 2 - POI

## Execução do teste de carga

Siga as instruções no link [K6](https://grafana.com/docs/k6/latest/set-up/install-k6/) para instalação da ferramenta de teste de carga.

Após a instalação, utilize o comando abaixo:

```
k6 run -e VUS=5 .\teste_carga.js
```
Obs: A variável VUS corresponde ao número de usuários que serão simulados, basta trocá-lo para realizar o teste com outras demandas
