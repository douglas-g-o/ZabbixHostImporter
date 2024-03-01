from pyzabbix import ZabbixAPI

# Substitua pelas suas credenciais e URL do Zabbix
zabbix_url = "http://your-domain.com/zabbix"
zabbix_user = "Admin"
zabbix_password = "zabbix"

zapi = ZabbixAPI(zabbix_url)
zapi.login(zabbix_user, zabbix_password)

# Nome do proxy que você está buscando
nome_do_proxy = "colocar nome"

proxies = zapi.proxy.get(filter={"host": nome_do_proxy}, output="extend")

if proxies:
    proxy_id = proxies[0]['proxyid']
    print(f"ID do Proxy '{nome_do_proxy}': {proxy_id}")
else:
    print(f"Proxy '{nome_do_proxy}' não encontrado.")