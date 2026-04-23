# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
import random
import socket
from abc import ABC, abstractmethod


class Port(ABC):
    @abstractmethod
    def value(self) -> int:
        pass


class TcpRandomPort(Port):
    def __init__(
        self, host: str = "127.0.0.1", begin: int = 1024, end: int = 65536
    ) -> None:
        self.__host = host
        self.__begin = begin
        self.__end = end

    def value(self) -> int:
        def is_tcp_port_in_use(host: str, port: int) -> bool:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
                try:
                    sckt.bind((host, port))
                except OSError:
                    return True
                return False

        port = random.randint(self.__begin, self.__end)
        while is_tcp_port_in_use(self.__host, port):
            port = random.randint(self.__begin, self.__end)
        return port


class UdpRandomPort(Port):
    def __init__(
        self, host: str = "127.0.0.1", begin: int = 1024, end: int = 65536
    ) -> None:
        self.__host = host
        self.__begin = begin
        self.__end = end

    def value(self) -> int:
        def is_udp_port_in_use(host: str, port: int) -> bool:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sckt:
                try:
                    sckt.bind((host, port))
                except OSError:
                    return True
                return False

        port = random.randint(self.__begin, self.__end)
        while is_udp_port_in_use(self.__host, port):
            port = random.randint(self.__begin, self.__end)
        return port


class TcpPort(Port):
    def __init__(self, num: int, host: str = "127.0.0.1") -> None:
        self.__host = host
        self.__num = num

    def value(self) -> int:
        def is_tcp_port_in_use(host: str, port: int) -> bool:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sckt:
                try:
                    sckt.bind((host, port))
                except OSError:
                    return True
                return False

        while is_tcp_port_in_use(self.__host, self.__num):
            pass
        return self.__num


class UdpPort(Port):
    def __init__(self, num: int, host: str = "127.0.0.1") -> None:
        self.__host = host
        self.__num = num

    def value(self) -> int:
        def is_udp_port_in_use(host: str, port: int) -> bool:
            with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sckt:
                try:
                    sckt.bind((host, port))
                except OSError:
                    return True
                return False

        while is_udp_port_in_use(self.__host, self.__num):
            pass
        return self.__num
