# SPDX-FileCopyrightText: Copyright (C) 2025-2026 Fabrício Barros Cabral
# SPDX-License-Identifier: MIT
import socket

from random_port.pool import (
    TcpPort,
    TcpRandomPort,
    UdpPort,
    UdpRandomPort,
)


def test_tcp_random_port() -> None:
    begin = 1024
    end = 65535
    port = TcpRandomPort().value()
    assert port >= begin
    assert port <= end


def test_udp_random_port() -> None:
    begin = 1024
    end = 65535
    port = UdpRandomPort().value()
    assert port >= begin
    assert port <= end


def test_tcp_in_use() -> None:
    host = "127.0.0.1"
    begin = 12344
    end = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setblocking(False)
    server.bind((host, begin))
    port = TcpRandomPort(host, begin, end).value()
    server.close()
    assert port == end


def test_udp_in_use() -> None:
    host = "127.0.0.1"
    begin = 12344
    end = 12345
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.setblocking(False)
    server.bind((host, begin))
    port = UdpRandomPort(host, begin, end).value()
    server.close()
    assert port == end


def test_tcp_port() -> None:
    num = 12345
    port = TcpPort(num).value()
    assert port == num


def test_udp_port() -> None:
    num = 12345
    port = UdpPort(num).value()
    assert port == num
