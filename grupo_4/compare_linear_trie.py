import time
import ipaddress

# Importa a Trie usada no exemplo
from ipv4_trie import IPv4Trie, ipv4_to_binary, prefix_to_binary

def linear_longest_prefix(ip_str, prefix_list):
    ip_obj = ipaddress.ip_address(ip_str)
    best_prefix = None
    best_len = -1
    for pfx in prefix_list:
        net = ipaddress.ip_network(pfx, strict=False)
        if ip_obj in net and net.prefixlen > best_len:
            best_len = net.prefixlen
            best_prefix = pfx
    return best_prefix

if __name__ == "__main__":
    # Gera apenas 256 prefixos válidos: 192.168.X.0/24 com X de 0 a 255
    prefix_list = [f"192.168.{i}.0/24" for i in range(256)]

    # Constrói a Trie
    trie = IPv4Trie()
    for pfx in prefix_list:
        bits, length = prefix_to_binary(pfx)
        trie.insert(bits, length, pfx)

    ip_test = "192.168.1.55"

    # Busca Linear
    start = time.time()
    linear_result = linear_longest_prefix(ip_test, prefix_list)
    linear_time = time.time() - start

    # Busca via Trie
    bits_test = ipv4_to_binary(ip_test)
    start = time.time()
    trie_result = trie.longest_prefix_match(bits_test)
    trie_time = time.time() - start

    print(f"Busca Linear: {linear_result}, Tempo: {linear_time:.6f} s")
    print(f"Busca Trie:   {trie_result}, Tempo: {trie_time:.6f} s")
