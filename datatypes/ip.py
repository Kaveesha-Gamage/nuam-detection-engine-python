from dataclasses import dataclass

@dataclass
class IP:
    src_ip: str
    dst_ip: str
    version: int
    ihl: int
    tos: int
    length: int
    id: int
    flags: int
    frag: int
    ttl: int
    proto: int
    chksum: int