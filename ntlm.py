import hashlib

def gerar_hash_ntlm(senha):
    # NTLM usa codificação UTF-16LE
    senha_utf16 = senha.encode('utf-16le')
    hash_ntlm = hashlib.new('md4', senha_utf16).hexdigest().upper()
    return hash_ntlm

# Lista de senhas fictícias
credenciais = {
    'Administrator': 'SuperSenha123!',
    'BackupUser': 'Dump4You#2024',
    'social_master': 'TalkYourWayIn99',
    'victim_user': '123456',
    'ctf_flagger': 'FlagMeIfYouCan'
}

# Gerando hashes
for usuario, senha in credenciais.items():
    hash_gerado = gerar_hash_ntlm(senha)
    print(f'{usuario}: {hash_gerado}')
