# 🤓 Zabbix Host Importer

Este script Python foi desenvolvido para automatizar o processo de importação de hosts para o Zabbix, uma solução popular de monitoramento de redes. Utilizando a biblioteca pyzabbix, o script se conecta à API do Zabbix, lê um arquivo CSV com os detalhes dos hosts e os importa automaticamente para a plataforma de monitoramento.

Pré-requisitos
Antes de executar o script, certifique-se de ter instalado as seguintes bibliotecas Python:
pip install pyzabbix
pip install pyzabbix pandas

# Uso:

Clone o repositório ou baixe o arquivo createhost.py
Modifique o script conforme necessário, fornecendo o URL do seu servidor Zabbix, nome de usuário e senha no trecho abaixo:
zapi = ZabbixAPI("http://your-domain.com/zabbix")
zapi.login(user="seu-usuario", password="sua-senha")

# Formato do Arquivo CSV

O arquivo hosts.csv deve seguir o formato especificado abaixo para garantir a importação bem-sucedida dos hosts para o Zabbix:
nome_host,ip,grupo1;grupo2;grupo3,template
Exemplo de uma linha no arquivo CSV:
teste,192.168.0.20,Clientes/Projeto;Parceiros/Test;Cyber/SOC,Template Module ICMP Ping 5minutos.
Para associar um host a múltiplos grupos, separe os nomes dos grupos com ponto e vírgula (;). Isso permite uma categorização detalhada e precisa dentro do Zabbix.

# Notas Adicionais
Certifique-se de que o usuário fornecido tenha permissões adequadas no Zabbix para criar hosts e manipular grupos e templates.
Revise o arquivo CSV para garantir que os dados estão corretos e formatados conforme o exemplo, especialmente a separação dos grupos de hosts.