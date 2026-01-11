import requests
import time
'''
Script para testar conectividade via proxies
'''
def teste_conexao(url, proxy_type=None, proxy_address=None, port=None, timeout=10):
    proxies = None
    if proxy_address:
        if port:
            proxy_url = f"{proxy_address}:{port}"
        else:
            proxy_url = proxy_address
            
        proxies = {
            "http": f"http://{proxy_url}",
            "https": f"https://{proxy_url}",
        }
    
    start_time = time.time()
    try:
        response = requests.get(url, proxies=proxies, timeout=timeout)
        elapsed = time.time() - start_time
        
        if response.status_code == 200:
            print(f"✓ {proxy_type or 'Conexão direta'} bem-sucedida: {response.status_code} (tempo: {elapsed:.2f}s)")
            print(f"resposta: {response.text[:100]} ")
        else:
            print(f"✗ {proxy_type or 'Conexão direta'} falhou: {response.status_code} (tempo: {elapsed:.2f}s)")
            
    except requests.exceptions.ConnectTimeout as e:
        print(f"✗ {proxy_type or 'Conexão direta'} - Timeout de conexão: {e}")
    except requests.exceptions.ProxyError as e:
        print(f"✗ {proxy_type or 'Conexão direta'} - Erro de proxy: {e}")
    except requests.exceptions.RequestException as e:
        print(f"✗ {proxy_type or 'Conexão direta'} - Erro geral: {e}")
        
def testar_proxy_simples(proxy_address, port=None):
    """Testa se o proxy está respondendo com uma requisição simples"""
    try:
        import socket

        address = (proxy_address, 44119)
            
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex(address)
        sock.close()
        
        if result == 0:
            print(f"✓ Proxy {proxy_address}:{address[1]} está acessível")
            return True
        else:
            print(f"✗ Proxy {proxy_address}:{address[1]} não está acessível")
            return False
    except Exception as e:
        print(f"✗ Erro ao testar proxy {proxy_address}: {e}")
        return False

# URL to test
url = "https://noticias.stf.jus.br/"

# Configurações de proxy
residencial = '4.142.254.253'


print("=== Testando conectividade ===")

# Teste 1: Conexão direta (sem proxy)
print("\n1. Testando conexão direta:")
teste_conexao(url)

testar_proxy_simples(residencial)
# Teste 2: Verificar com proxy

teste_conexao(url, proxy_type='Residencial', proxy_address=residencial, timeout=15)
