import ipaddress

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.prefix_str = None

class IPv6Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, bin_addr, prefix_len, original_prefix):
        current = self.root
        for i in range(prefix_len):
            bit = bin_addr[i]
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]
        current.is_end = True
        current.prefix_str = original_prefix

    def longest_prefix_match(self, bin_ip):
        current = self.root
        longest = None
        for bit in bin_ip:
            if bit in current.children:
                current = current.children[bit]
                if current.is_end:
                    longest = current.prefix_str
            else:
                break
        return longest

def ipv6_to_binary(ip_str):
    ip_obj = ipaddress.ip_address(ip_str)
    return bin(int(ip_obj))[2:].zfill(128)

def prefix_to_bin_ipv6(prefix_str):
    net = ipaddress.ip_network(prefix_str, strict=False)
    ip_int = int(net.network_address)
    prefix_len = net.prefixlen
    bin_addr = bin(ip_int)[2:].zfill(128)
    return bin_addr, prefix_len, str(net)

if __name__ == "__main__":
    trie = IPv6Trie()
    prefixes = ["2001:db8::/32", "2001:db8:1234::/48"]
    for pfx in prefixes:
        bin_rep, plen, original = prefix_to_bin_ipv6(pfx)
        trie.insert(bin_rep, plen, original)

    test_ip = "2001:db8:1234:5678::1"
    bin_test_ip = ipv6_to_binary(test_ip)
    match = trie.longest_prefix_match(bin_test_ip)
    print(f"Prefixo correspondente para {test_ip}: {match}")
