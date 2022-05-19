import random 
import string

char = list(string.ascii_letters)

palavras = ['estamos','estou','estrada','estrangeiro','exposto','extrato','extrema','falecer','falecido','falecimento','fazenda','fazendeiro','febre','febre','feito','feminino','feriado','ferreiro','ferrovia','feudo','fevereiro','ficar','ficheiro','fidalgo','filha','filho','filhos','floresta','fogo','foi','folha','fomos','fonte','fora','foram','forasteiro','fortaleza','francês','fraqueza','freguês','freguesia','frente','fronteira','fui','fundos','futuro','gadogenealogia','genro','gente','gota','grande','gripe','guarda','guia','hemorragia','herdeiro','hidropisia','história','hoje','honesto','hora','hospedaria','hospedeiro','idade','idioma','idoso','igreja','imigrante','impedimento','imposto','indigente','inglesa','inocente','inquilino','intestinos','inverno','irmandade','isso','isto','italiano','janeiro','jardineiro','jornal','judeu','juiz','julho','junho','junto','jurado','lago','lançamento','lar','lavrador','legal','lei','leiteiro','leste','liberto','livro','lugar','luterano','macho','madrasta','madrinha','madrugada','maio','maior','mais','mais','mais','mais','mapa','marceneiro','março','marido','marinha','marinheiro','marrano','mas','masculino','materno','mato','matriz','meia','meio','meio','membro','mendigo','menino','menonita','menor','menos','mercado','mercadoria','mesmo','mestre','metade','meu','mil','milha','milho','mina','mineiro','minha','ministro','moça','moço','moinho','molestia','montanha','monte','morada','morador','morar','morrer','morte','móveis','mudo','muitas','muito','mulato','mulher','nariz','nascido','nascimento','natimorto','natural','navio','negro','nenhum','nesta','neste','neta','neto','netos','nobre','nobreza','noite','noiva','noivado','noivados','noivo','noivos','nome','nono','nora','norte','nosso','nove','novecentos','novembro','noventa','novo','nunca','obreiro','oeste','oferta','oitavo','oitenta','oito','oitocentos','oleiro','olho','onde','ontem','onze','orelha','orfanato','ou','ouro','outono','outro','outubro','padeiro','padrasto','padre','padrinho','padrinhos','pai','pais','para','pardo','parente','parentesco','parteira','parto','passado','passageiro','pastor','paterno','pedreiro','pelo','perna','perto','pescador','peso','pesquisa','peste','pleito','pneumonia','polaco','ponte','porque','porto','portuguesa','possuir','povo','povoado','praça','prata','prazo','prece','prefeito','prefeitura','presente','preto','primavera','primeiro','primo','princesa','professor','professora','progenitor','prole','propriedade','proprietário','protestante','quadro','qual','quando','quarenta','quarto','quatorze','quatro','quarto','quatrocentos','que','quem','quinhentos','quinta','quinto','quinze','rainha','rapaz','real','receber','recebimento','recursos','registros','registros','rei','reino','retrato','riacho','rio','rosto','rua','russo','sacerdote','sagrado','sala','santo','santos','sapateiro','sarampo','secenta','segundo','seicentos','seis','semana','sempre','senhor','senhora','separado','sepultado','sepultamento','sepultura','serra','serralheiro','servente','setecentos','setenta','seu','sexo','sexto','sim','sobre','sobrenome','sobrevivente','sobrinho','sociedade','sogro','solar','soldado','solenemente','solteiro','somente','somos','sou','sua','subdistrito','sueco','sul','surdo','talvez','tarde','taxa','tecedor','temos','tempo','tenho','ter','terceiro','termo','terreno','testamenteiro','testamento','testemunha','testemunho','tia','tintureiro','tio','tosse','trabalhador','trezentos','trigo','trinta','tuberculose','tudo','tumor','tutela','vale','variola','velho','vender','velha','verde','vereador','vermelho','vermelha','vez','vila','vinha','vinhedo','vinte','viver','viva','vivo','vizinho','volume','vizinha','abcesso','abril','acordo','acre','ata','adotada','adotado','advogada','advogado','afogamento','agosto','ainda','alcunha','alfaiate','alguma','algum','ali','alma','alta','alto','altura','aluguel','amarela','amarelo','ambas','ambos','amiga','amigo','ancestral','anjo','ano','antepassada','antepassado','anterior','antes','antiga','antigo','anual','baixa','baixo','batismo','batizar','barco','batismo','batizar','bem','biblioteca','bisneta','bisneto','bisnetos','bispado','bispo','boca','boda','boieiro','boabombosque','brancabranco','cadastro','cadeia','cafezal','campo','camponesa','cana','cancro','capela','cara','carpinteiro','casa','casada','casado','casamento','castelo','catedral','cavalheiro','cedo','cega','cego','cem','censo','cento','cerca','cervejeiro','cidade','cinco','cinquenta','clero','colheita','colina','colono','comerciante','como','concelho','concernente','conde','conhecida','conhecido','consorte','conta','contra','contraente','coqueluche','cordoeiro','corrente','corte','cova','coxa','coxo','criada','cuja','cujo','cunhada','cunhado','cura','curato','tribunal','curtidor','daquele','data','declarado','dedo','defunto','dele','dente','dentro','depois','derrame','derrame','descendente','desconhecido','desde','desobriga','desquitado','desquite','desse','deste','dez','dezembro','dezenove','dezesseis','dezessete','dezoito','diarreia','digno','dignadigo','diocese','direito','direito','disenteria','dispensa','disputa','disso','distrito','dito','divorciado','documento','dois','domingo','dono','doze','duque','duquesa','duzentos','emigrante','empregada','empregado','empresa','enfermidade','engenho','enteado','enterrado','enterro','epidemia','epilepsia','escola','escravo','escrevente','esmola','espanhol','esposo','estado'"acender","afilhado","ardiloso","asterisco","basquete","caminho","champanhe","chiclete","chuveiro","coelho","contexto","desalmado","eloquente","espirro","esquerdo","fugaz","heterossexual","horrorizado","impacto","modernidade","oftalmologista","pipoca","quarentena","quimera","reportagem","sino","taciturno","visceral"]

nome= input("Bem vindo ao jogo da forca! Como vc se chama? ").title()
print(f"Bom, {nome}, o jogo da força basicamente envolve vc descobrir letra por letra a palavra codificada.")

def jogo():
    palavra =random.choice(palavras)
    global b
    b = 0
    letrasdapalavra = []
    global a
    a = 0
    codigo=" "
    codigo += palavra.replace(palavra[a],str(a))
    maxtentativas = len(palavra)+4
    while b in range (0,len(palavra)):
            letrasdapalavra += str(palavra[b])
            b+=1
            codigo = (codigo.replace(palavra[a],str(a)))
            a +=1
            if str(letrasdapalavra) == palavra : 
                break
            
    print(f"Eis sua palavra:{codigo}")
    tentativas = 0
    print(f"Vc tem {maxtentativas} tentativas para acertar.")

    while True:
        letra= input(f"Tentativa {tentativas+1}/{maxtentativas}: Qual letra está na palavra: ")
        if letra == palavra:
            print(f"Parabens, vc acertou, a palavra correta era {palavra}. Deseja jogar de novo?")
            replay = input("") 
            if replay == "n":
                break

        if letra in palavra:
            c = palavra.find(letra)
            tentativas += 1
            codigo = codigo.replace(codigo[c+1],letra)
            if codigo == (f" {palavra}"):
                print(f"Parabens, vc acertou, a palavra correta era {palavra}. Deseja jogar de novo?")
                replay = input("") 
                if replay == "n":
                    break
                else:
                    jogo()
            elif codigo != (f" {palavra}"):
                print(f"Parabens, a letra estava na palavra! Eis a sua palavra:{codigo}")

        else:
                print(f"A letra {letra} não estava na palavra. Tente de novo")
                tentativas += 1

        if tentativas == (maxtentativas):
            print(f"Vc excedeu o número de tentativas. A palavra era {palavra}, bom jogo. Deseja jogar de novo? ")
            replay = input("") 
            if replay == "n":
                break
            else:
                jogo()

jogo()