cpf = input("Digite o CPF: ").strip()

if cpf.isdigit() and len(cpf) == 11:
    nCpf = [cpf[:3], cpf[3:6], cpf[6:9]]

    print(f"{'.'.join(nCpf)}-{cpf[9:11]}")

    noveCPF = []
    for i in range(len(cpf)):
        if i == 3 or i == 6:
            noveCPF.append('.')
        elif i == 9:
            noveCPF.append('-')
            
        noveCPF.append(cpf[i])


    cpf_formatado = ''.join(noveCPF)
    print("CPF formatado:", cpf_formatado)       
else:
    print("Digite apenas número")



