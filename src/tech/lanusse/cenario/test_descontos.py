import pytest
import sys
import os

# Ajustando o path para encontrar o módulo calculadora
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..')))
from tech.lanusse.calculadora.descontos import calcular_desconto

# --- CENÁRIO 1: Compras menores que R$ 100,00 (0% desconto base) ---
def test_compra_menor_100_comum():
    # 0% de desconto
    assert calcular_desconto(50, "COMUM") == 0.0

def test_compra_menor_100_vip():
    # 0% base + 5% VIP = 5%
    assert calcular_desconto(50, "VIP") == 2.50

# --- CENÁRIO 2: Compras iguais ou maiores que 100 e menores que 500 (10% desconto base) ---
def test_compra_exatos_100_comum():
    # 10% de desconto (Valida o limite inferior)
    assert calcular_desconto(100, "COMUM") == 10.0

def test_compra_intermediaria_comum():
    # 10% de desconto (Teste do Dev Jr.)
    assert calcular_desconto(300, "COMUM") == 30.0

def test_compra_100_vip_minusculo():
    # 10% base + 5% VIP = 15% (Valida case-insensitive do VIP)
    assert calcular_desconto(100, "vip") == 15.0

# --- CENÁRIO 3: Compras a partir de R$ 500,00 (20% desconto base) ---
def test_compra_exatos_500_comum():
    # 20% de desconto
    assert calcular_desconto(500, "COMUM") == 100.0

def test_compra_maior_500_vip_misto():
    # 20% base + 5% VIP = 25% (Valida case-insensitive misto)
    assert calcular_desconto(600, "ViP") == 150.0

# --- CENÁRIO 4: Regra de Teto (Máximo R$ 200,00) ---
def test_teto_maximo_comum():
    # 20% de 1200 = 240 -> Teto = 200
    assert calcular_desconto(1200, "COMUM") == 200.0

def test_teto_maximo_vip():
    # 25% de 1000 = 250 -> Teto = 200
    assert calcular_desconto(1000, "VIP") == 200.0
