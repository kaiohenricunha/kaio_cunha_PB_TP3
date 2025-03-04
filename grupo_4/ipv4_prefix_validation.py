import ipaddress

def validate_ipv4_in_prefix(ip_str, prefix_str):
    ip_obj = ipaddress.ip_address(ip_str)
    prefix_obj = ipaddress.ip_network(prefix_str, strict=False)
    return ip_obj in prefix_obj

if __name__ == "__main__":
    ip_to_test = "192.168.1.5"
    prefix_test = "192.168.1.0/24"
    inside = validate_ipv4_in_prefix(ip_to_test, prefix_test)
    print(f"O IP {ip_to_test} está dentro de {prefix_test}? {inside}")
