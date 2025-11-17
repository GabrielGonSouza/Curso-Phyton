programa {
  funcao inicio() {
    
    //1 Passo Declarar variaveis 
    real valorTotal, porcentagem, resultado 

    //2 Passo Entrada de dados 
    escreva ("Digite o valor total: R$")
    leia(valorTotal)


    escreva ("Digite a porcentagem ")
    leia(porcentagem)

    //3 passo Processamento 
    resultado = (valorTotal * porcentagem) / 100

    // 4 Passo Saída 
    escreva ("\n", porcentagem, "% de ", "R$",valorTotal, " é igual a: R$", resultado)
  }
}
