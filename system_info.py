import platform

print("Sistema Operacional :", platform.system())
print("Versão             :", platform.release())
print("Arquitetura        :", platform.architecture()[0])
print("Máquina            :", platform.machine())
print("Processador        :", platform.processor())
print("Hostname           :", platform.node())
print("Python             :", platform.python_version())



