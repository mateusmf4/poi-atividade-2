# Atividade 2 - POI

## Execução do teste de carga

Siga as instruções no link [K6](https://grafana.com/docs/k6/latest/set-up/install-k6/) para instalação da ferramenta de teste de carga.

Após a instalação, utilize o comando abaixo:

```
k6 run -e VUS=5 .\teste_carga.js
```
Obs: A variável VUS corresponde ao número de usuários que serão simulados, basta trocá-lo para realizar o teste com outras demandas

## Monitoramento da vm

Após iniciar a execução de uma das API's, resgate o PID e insira o valor do processo no [monitorar.sh](./monitorar.sh) e execute o comando abaixo:

```
chmod +x monitorar.sh
sudo ./monitorar.sh
```
Obs: O script foi configurado pensando na execução da API io-bound
