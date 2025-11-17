programa {
  funcao inicio() {
    
    // 1 Passo - Declarar as variaveis 
    real numero1, numero2, multiplicacao, divisao, subtracao
   
   // 2 Passo - Entrada 
   escreva("Digite o primeiro número: " )
   leia(numero1)

   escreva("Digite o segundo número: ")
   leia(numero2)

   //3 Passo - Processamento 
   multiplicacao = numero1 * numero2
   divisao = numero1 / numero2
   subtracao = numero1 - numero2

   //4 passo - Saída
   escreva ("A Multiplicação é: ", multiplicacao)
   escreva ("\nA Divisão é ", divisao)
   escreva ("\nA Subtração é ", subtracao)

  }
}
