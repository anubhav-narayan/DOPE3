import pytest
from dope3 import *


key1 = RSA.generate(3072)
key2 = RSA.generate(3072)
end_key1 = key1.publickey()
end_key2 = key2.publickey()
dopex1 = DOPE(key1, end_key2, 1024, 16441, 16, 'BLAKEx0x',
              'GCM', 'SHA256', 'XOR-BL')
dopex2 = DOPE(key2, end_key1, 1024, 16441, 16, 'BLAKEx0x',
              'CBC', 'SHA384', 'XOR-BL')


def test_and():
    assert byte_and(b'\x01\x01', b'\xff\xff') != b'\xfe\xfe'


def test_xor():
    assert byte_xor(b'\x01\x01', b'\xff\xff') != b'\x01\x01'


def test_dope():
    assert b'-----BEGIN DOPE KEY-----' == dopex1.generate_key()[:24]
    assert b'-----BEGIN DOPE KEY-----' == dopex2.generate_key()[:24]
    dopex1.fixate(dopex2.generate_key())
    dopex2.fixate(dopex1.generate_key())
    data = b'\x00\x01\x10\x11'
    encoded_data = dopex1.encode(data)
    decoded_data = dopex2.decode(encoded_data)
    assert data == decoded_data
    assert dopex1.DOPE_key != b''
    assert str(dopex1)[:5] == 'DOPE_'


def test_dope2():
    key = b'1234'
    dopex = DOPE2(key, 16441, 16, 'GCM', b'')
    data = b'I am DOPE'
    assert dopex.serialize()[:26] == b'-----BEGIN DOPE 2 KEY-----'
    assert str(dopex)[:6] == 'DOPE2_'
    dopex.fixate()
    encoded_data = dopex.encode(data)
    dopex.fixate()
    decoded_data = dopex.decode(encoded_data)
    assert data == decoded_data
    dopex = DOPE2(key, 16441, 16, 'OFB', b'')
    dopex.fixate()
    encoded_data = dopex.encode(data)
    dopex.fixate()
    decoded_data = dopex.decode(encoded_data)
    assert data == decoded_data


def test_aes_siv():
    try:
        dopex1.fixate(dopex2.generate_key())
        dopex2.fixate(dopex1.generate_key())
        data = b'\x00\x01\x10\x11'
        encoded_data = dopex1.encode(data)
        decoded_data = dopex2.decode(encoded_data)
        assert data == decoded_data
        dopex1.fixate(dopex2.generate_key())
        dopex2.fixate(dopex1.generate_key())
        encoded_data = dopex2.encode(data)
    except Exception:
        raise AssertionError
