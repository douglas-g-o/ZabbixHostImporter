# Importando as bibliotecas necessárias
from pyzabbix import ZabbixAPI
import pandas as pd

# Conectando ao Zabbix
zapi = ZabbixAPI("http://your-domain.com/zabbix")
zapi.login(user="Admin", password="zabbix")

df = pd.read_csv('hosts.csv', header=None, encoding='latin1')

for index, row in df.iterrows():
    try:
        values = row[0].split(',')

        if len(values) != 4:
            print(f"Erro: A linha {index} não contém quatro valores.")
            continue

        hostname, ip, host_group_names, template_name = values

        hostname_cleaned = hostname.strip().strip('"')
        template_name_cleaned = template_name.strip().rstrip('"')

        group_ids = []
        group_not_found = False
        for group_name in host_group_names.split(';'):
            host_group = zapi.hostgroup.get(filter={"name": group_name.strip()})
            if host_group:
                group_ids.append({"groupid": host_group[0]['groupid']})
            else:
                print(f"Grupo de hosts '{group_name}' não encontrado.")
                group_not_found = True
                break 

        if group_not_found:
            continue

        template = zapi.template.get(output="extend", filter={"host": template_name_cleaned})
        if template:
            template_id = template[0]['templateid']
        else:
            print(f"Template '{template_name_cleaned}' não encontrado.")
            continue  

        proxy_id = '0' # Colocar o numero do proxy pego no proxy.py
        host_created = zapi.host.create(
            host=hostname_cleaned,
            status=0,
            interfaces=[{
                "type": 2,  # SNMP, Agent 1, SNMP 2, IPMI 3, JMX 4
                "main": "1",
                "useip": 1,
                "ip": ip,
                "dns": "",
                "port": "161",
                "details": {
                    "version": 2,
                    "community": "{$SNMP_COMMUNITY}"
                }
            }],
            groups=group_ids,
            templates=[{"templateid": template_id}],
            proxy_hostid=proxy_id 
        )
        print(f"Host '{hostname_cleaned}' criado com sucesso e monitorado pelo proxy.")
    except Exception as e:
        print(f"Falha ao criar o host: {str(e)}")

# erro -32602 nome de host ja existe