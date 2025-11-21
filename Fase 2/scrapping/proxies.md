## Proxy


### Proxy reverso


Funciona como o intermediário entre o servidor original e o cliente com objetivo de proteger, de garantir a segurança e balancear os dados. 


#### Como funciona?

1. o cliente envia sua solicitação ao invés dela cair no servidor direto ela cai no proxy reverso.
2. Lá ele decide com base com cookies e cabeçalho a origem da solicitação (incluindo se é um bot) e decide se vai enviar a solicitação pro servidor de origem ou vai usar dados do cache.
3. O proxy reverso envia para o servidor backend ( em casos de balanceamento ou alguma outra configuração é diferente), 