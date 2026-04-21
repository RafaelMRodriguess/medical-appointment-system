
horarios_cardiologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_neurologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_dermatologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_ortopedista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_oftalmologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_otorrinolaringologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_gastroenterologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']
horarios_endocrinologista = ['08:00', '09:00', '10:00', '11:00', '13:00', '14:00', '15:00', '16:00']


while True:
    nome = input('Digite seu nome completo, por favor: ')
    print(f'\nOlá, {nome}. Tudo bem? Qual tipo de especialidade médica você procura?\n')
    print('\n[1] Cardiologista\n[2] Neurologista\n[3] Dermatologista\n[4] Ortopedista\n[5] Oftalmologista\n[6] Otorrinolaringologista\n[7] Gastroenterologista\n[8] Endocrinologista\n[9] Não sei qual médico procurar\n[0] Sair\n')

    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print('\nEspecialidade selecionada: Cardiologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_cardiologista, start=1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha o horário para agendar sua consulta: '))
        horarios_cardiologista.pop(horario_selecionado -1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 2:
        print('\nEspecialidade selecionada: Neurologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_neurologista, start=1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha o horário para agendar sua consulta: '))
        horarios_neurologista.pop(horario_selecionado -1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 3:
        print('\nEspecialidade selecionada: Dermatologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_dermatologista, start= 1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha o horário para agendar sua consulta: '))
        horarios_dermatologista.pop(horario_selecionado - 1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 4:
        print('\nEspecialidade selecionada: Ortopedista')
        print('\nConsultas disponíveis para hoje: ')
        for i, item in enumerate(horarios_ortopedista, start=1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha um horário para agendar sua consulta: '))
        horarios_ortopedista.pop(horario_selecionado - 1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 5:
        print('\nEspecialidade selecionada: Oftalmologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_oftalmologista, start=1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha um horário para agendar sua consulta: '))
        horarios_oftalmologista.pop(horario_selecionado - 1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 6:
        print('\nEspecialidade selecionada: Otorrinolaringologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_otorrinolaringologista, start=1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha um horário para agendar sua consulta: '))
        horarios_otorrinolaringologista.pop(horario_selecionado - 1)
        print('\nConsulta agendada com sucesso!')

    elif opcao == 7:
        print('\nEspecialidade selecionada: Gastroenterologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_gastroenterologista, start= 1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha um horário para agendar sua consulta: '))
        horarios_gastroenterologista.pop(horario_selecionado - 1)
        print('Consulta agendada com sucesso!')

    elif opcao == 8:
        print('\nEspecialidade selecionada: Endocrinologista')
        print('\nConsultas disponíveis para hoje:')
        for i, item in enumerate(horarios_endocrinologista, start= 1):
            print(f'{i} - {item}')
        horario_selecionado = int(input('Escolha um horário para agendar sua consulta: '))
        horarios_endocrinologista.pop(horario_selecionado - 1)
        print('Consulta agendada com sucesso!')

    elif opcao == 9:
        print('\nOnde está o problema?\n[1] Coração\n[2] Cérebro ou sistema nervoso\n[3] Pele\n[4] Ossos, articulações ou músculos\n[5] Olhos\n[6] Ouvido, nariz ou garganta\n[7] Estômago ou intestino\n[8] Hormônios ou glândulas\n')
        problema = int(input('Escolha uma opção: '))


        if problema == 1:
            print('\nPara casos de problemas no coração, sugerimos atendimento com um médico cardiologista.\n')
            print('O que trata o cardiologista? O cardiologista trata o coração e a circulação.')
            print('\nSintomas comuns:\n- Dor no peito\n- Palpitações\n- Falta de ar\n- Pressão alta\n- Cansaço excessivo\n')
            print('Quando procurar esse especialista? Quando esses sintomas forem frequentes ou estiverem preocupando.\n')
            print('Sinais de alerta (urgência):')
            print('Se houver dor intensa no peito, falta de ar forte ou suspeita de infarto, procurar emergência imediatamente.\n')
            print('Exames comuns solicitados:\n- Eletrocardiograma\n- Ecocardiograma\n- Teste ergométrico')
            print('\nOrientação para a consulta:\nLeve exames anteriores e anote seus sintomas.')
            print('\nRecomendação final:\nAgendar avaliação com cardiologista.')
        
        elif problema == 2:
            print('\nPara casos relacionados ao cérebro ou sistema nervoso, sugerimos atendimento com um médico neurologista.\n')
            print('O que trata o neurologista? O neurologista trata doenças do cérebro, nervos e sistema nervoso.')
            print('\nSintomas comuns:\n- Dor de cabeça frequente\n- Tontura\n- Formigamentos\n- Convulsões\n- Falhas de memória\n')
            print('Quando procurar esse especialista? Quando esses sintomas forem recorrentes ou preocupantes.\n')
            print('Sinais de alerta (urgência):')
            print('Fraqueza súbita, dificuldade para falar ou suspeita de AVC exigem emergência imediata.\n')
            print('Exames comuns solicitados:\n- Ressonância magnética\n- Tomografia\n- Eletroencefalograma')
            print('\nOrientação para a consulta:\nAnote quando os sintomas começaram e sua frequência.')
            print('\nRecomendação final:\nAgendar avaliação com neurologista.')


        elif problema == 3:
            print('\nPara casos relacionados à pele, sugerimos atendimento com um médico dermatologista.\n')
            print('O que trata o dermatologista? O dermatologista cuida da pele, cabelo e unhas.')
            print('\nSintomas comuns:\n- Manchas\n- Coceira\n- Acne\n- Queda de cabelo\n- Lesões na pele\n')
            print('Quando procurar esse especialista? Quando os sintomas persistirem ou piorarem.\n')
            print('Sinais de alerta (urgência):')
            print('Lesões que crescem rápido ou mudam de aparência merecem avaliação rápida.\n')
            print('Exames comuns solicitados:\n- Dermatoscopia\n- Biópsia\n- Exames laboratoriais')
            print('\nOrientação para a consulta:\nSe possível, registre mudanças nas lesões.')
            print('\nRecomendação final:\nAgendar avaliação com dermatologista.')


        elif problema == 4:
            print('\nPara casos relacionados a ossos, articulações ou músculos, sugerimos um ortopedista.\n')
            print('O que trata o ortopedista? O ortopedista trata problemas nos ossos, músculos e articulações.')
            print('\nSintomas comuns:\n- Dor nas articulações\n- Dor muscular\n- Inchaço\n- Dificuldade para andar\n- Lesões\n')
            print('Quando procurar esse especialista? Quando houver dor persistente ou limitação de movimentos.\n')
            print('Sinais de alerta (urgência):')
            print('Fraturas ou dor intensa após trauma podem exigir urgência.\n')
            print('Exames comuns solicitados:\n- Raio-X\n- Ressonância\n- Ultrassom')
            print('\nOrientação para a consulta:\nInforme se houve queda, trauma ou lesão.')
            print('\nRecomendação final:\nAgendar avaliação com ortopedista.')


        elif problema == 5:
            print('\nPara casos relacionados aos olhos, sugerimos um oftalmologista.\n')
            print('O que trata o oftalmologista? O oftalmologista cuida da saúde dos olhos e visão.')
            print('\nSintomas comuns:\n- Visão embaçada\n- Dor nos olhos\n- Ardência\n- Vermelhidão\n- Dificuldade para enxergar\n')
            print('Quando procurar esse especialista? Quando houver alterações na visão ou desconforto.\n')
            print('Sinais de alerta (urgência):')
            print('Perda súbita de visão exige atendimento imediato.\n')
            print('Exames comuns solicitados:\n- Exame de refração\n- Fundo de olho\n- Tonometria')
            print('\nOrientação para a consulta:\nLeve receitas antigas de óculos, se tiver.')
            print('\nRecomendação final:\nAgendar avaliação com oftalmologista.')


        elif problema == 6:
            print('\nPara casos relacionados a ouvido, nariz ou garganta, sugerimos um otorrinolaringologista.\n')
            print('O que trata esse especialista? Trata problemas de ouvido, nariz e garganta.')
            print('\nSintomas comuns:\n- Dor de garganta\n- Sinusite\n- Dor de ouvido\n- Zumbido\n- Nariz entupido\n')
            print('Quando procurar esse especialista? Quando os sintomas persistirem ou forem frequentes.\n')
            print('Sinais de alerta (urgência):')
            print('Dificuldade para respirar ou infecções graves exigem atenção rápida.\n')
            print('Exames comuns solicitados:\n- Endoscopia nasal\n- Audiometria\n- Exame clínico')
            print('\nOrientação para a consulta:\nInforme há quanto tempo os sintomas começaram.')
            print('\nRecomendação final:\nAgendar avaliação com otorrinolaringologista.')


        elif problema == 7:
            print('\nPara casos relacionados ao estômago ou intestino, sugerimos um gastroenterologista.\n')
            print('O que trata o gastroenterologista? Trata problemas do sistema digestivo.')
            print('\nSintomas comuns:\n- Dor abdominal\n- Azia\n- Refluxo\n- Diarreia\n- Constipação\n')
            print('Quando procurar esse especialista? Quando os sintomas forem recorrentes.\n')
            print('Sinais de alerta (urgência):')
            print('Dor intensa ou sangue nas fezes merecem atenção imediata.\n')
            print('Exames comuns solicitados:\n- Endoscopia\n- Colonoscopia\n- Ultrassom')
            print('\nOrientação para a consulta:\nAnote alimentos que pioram os sintomas.')
            print('\nRecomendação final:\nAgendar avaliação com gastroenterologista.')


        elif problema == 8:
            print('\nPara casos relacionados a hormônios ou glândulas, sugerimos um endocrinologista.\n')
            print('O que trata o endocrinologista? Trata alterações hormonais e metabólicas.')
            print('\nSintomas comuns:\n- Cansaço excessivo\n- Alterações de peso\n- Queda de cabelo\n- Sede excessiva\n- Alterações hormonais\n')
            print('Quando procurar esse especialista? Quando houver sintomas persistentes ou suspeita hormonal.\n')
            print('Sinais de alerta (urgência):')
            print('Alterações graves de glicose podem exigir urgência.\n')
            print('Exames comuns solicitados:\n- Exames hormonais\n- Glicemia\n- Exames da tireoide')
            print('\nOrientação para a consulta:\nLeve exames recentes, se tiver.')
            print('\nRecomendação final:\nAgendar avaliação com endocrinologista.')
        
        else:
            print('\nOpção inválida!')
    
    elif opcao == 0:
        break 

    else:
        print('\nOpção inválida!')

print('\nPrograma encerrado.')
