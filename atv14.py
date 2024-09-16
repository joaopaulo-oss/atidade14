# Crie um programa que receba três notas de um aluno e calcule a média. Informe se o aluno foi aprovado, reprovado ou se está de recuperação. Use as seguintes regras:
nota1 = float(input('digite a nota 1: '))
nota2 = float(input('digite a nota 2: '))
nota3 = float(input('digite a nota 3: '))

média = (nota1 + nota2 + nota3) / 3

print('tirando {} e {}, média do aluno é {:.1f}'. format(nota1, nota2, nota3, média))

if média >= 7: 
    print('aprovado.')

elif 5  == média and media < 7:
     print('recuperação')

elif média < 5:
     print('reprovado.')
