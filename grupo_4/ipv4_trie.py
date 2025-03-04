class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
        self.prefix_str = None

class IPv4Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, prefix, prefix_len, prefix_str):
        current = self.root
        for i in range(prefix_len):
            bit = prefix[i]
            if bit not in current.children:
                current.children[bit] = TrieNode()
            current = current.children[bit]
        current.is_end = True
        current.prefix_str = prefix_str

    def longest_prefix_match(self, ip_bits):
        current = self.root
        longest_match = None
        for bit in ip_bits:
            if bit in current.children:
                current = current.children[bit]
                if current.is_end:
                    longest_match = current.prefix_str
            else:
                break
        return longest_match

def ipv4_to_binary(ip_str):
    parts = ip_str.split(".")
    return "".join(f"{int(part):08b}" for part in parts)

def prefix_to_binary(prefix_str):
    addr, length = prefix_str.split("/")
    length = int(length)
    bin_ip = ipv4_to_binary(addr)
    return bin_ip[:length], length

if __name__ == "__main__":
    trie = IPv4Trie()
    prefixes = ["192.168.0.0/16", "192.168.1.0/24", "10.0.0.0/8"]
    for pfx in prefixes:
        bin_rep, length = prefix_to_binary(pfx)
        trie.insert(bin_rep, length, pfx)

    ip_test = "192.168.1.100"
    ip_bits = ipv4_to_binary(ip_test)
    match = trie.longest_prefix_match(ip_bits)
    print(f"Prefixo mais específico para {ip_test}: {match}")
