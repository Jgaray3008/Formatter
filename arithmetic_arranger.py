#EXCEPTIONS
# First rule Error: Too many problems. limit 5
# Second rule Error: Operator must be '+' or '-'.
# Third rule Error: Numbers must only contain digits.
# Fourth rule.  Error: Numbers cannot be more than four digits.


def arithmetic_arranger(problems, show=False):
    
    #Damos el problema matematico horizontal, esta funcion lo aregla vertical
    
    PrimerLinea = ''
    SegundaLinea = ''
    TercerLinea = ''
    LineaResp = ''
    x = 0

    #Leemos la primera regla de no mas de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."
        #primer regla
    while len(problems) > x:

        CadaValor = problems[x].split()
        PrimerNum = CadaValor[0]
        SegunNum = CadaValor[2]
        operador = CadaValor[1]

        if len(PrimerNum) < 5 and len(SegunNum) < 5:
            #funcion .isnumeric() permite verificar si el dato revisado es efectivamente un numero
            if PrimerNum.isnumeric() and SegunNum.isnumeric():

                if operador == '+':
                    resultado = str(int(PrimerNum) + int(SegunNum))
                elif operador == '-':
                    resultado = str(int(PrimerNum) - int(SegunNum))
                else:
                    #Segunda regla de operador solo '+' o '-'
                    return "Error: Operator must be '+' or '-'."
            else:
                #Tercer regla, solo digitos numericos
                return "Error: Numbers must only contain digits."
        else:
            #Tercera regla no mas de 4 digitos
            return "Error: Numbers cannot be more than four digits."


        #Espacion entre los problemas matematicos en el arreglo
        
        espacio = max(len(PrimerNum), len(SegunNum)) + 2

        PrimerLinea += ' ' * (espacio - len(PrimerNum)) + PrimerNum + ' ' * 4
        SegundaLinea += operador + ' ' * (espacio - len(SegunNum) - 1) + SegunNum + ' ' * 4
        TercerLinea += espacio * '-' + ' ' * 4
        LineaResp += ' ' * (espacio - len(resultado)) + resultado + ' ' * 4
        x += 1

    #Se muestra si el segundo argumento = True

    if show:
        arranged_problems = PrimerLinea.rstrip() + '\n' + SegundaLinea.rstrip() + '\n' + TercerLinea.rstrip() + '\n' + LineaResp.rstrip()
    else:
        arranged_problems = PrimerLinea.rstrip() + '\n' + SegundaLinea.rstrip() + '\n' + TercerLinea.rstrip()
    return arranged_problems


