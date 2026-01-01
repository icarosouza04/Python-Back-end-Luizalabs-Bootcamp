import requests

# Parâmetros de consulta (ou query parameters) são parte de uma URL (Uniform Resource Locator) que permite que informações adicionais sejam enviadas para um servidor. 
# Eles são usados para filtrar, paginar, e ordenar dados, entre outras funções. Esses parâmetros são anexados à URL após um ponto de interrogação (?), e múltiplos parâmetros são separados por um e comercial (&).

url = "https://example.com/products"

params = {
    "category": "eletronics",
    "limit" : 10,
    "page": 1,
    "sort": "price"
}

response = requests.get(url, params = params)

print(response.json())

# Explicação do código

# 1 - Criar uma Instância do HttpClient: using (HttpClient client = new HttpClient()) cria uma instância de HttpClient para fazer a solicitação HTTP.
# 2 - Definir a URL Base e Parâmetros: string baseUrl = "https://example.com/products"; define a URL base. Em seguida, string queryString = "category=electronics&limit=10&page=1&sort=price"; cria a string com os parâmetros de consulta.
# 3 - Concatenar a URL Base com os Parâmetros: string requestUrl = $"{baseUrl}?{queryString}"; combina a URL base com a string de parâmetros de consulta para formar a URL completa para a solicitação.
# 4 - Fazer a Solicitação GET: HttpResponseMessage response = await client.GetAsync(requestUrl); faz uma solicitação GET para a URL construída.
# 5 - Verificar e Processar a Resposta: O código verifica se a resposta foi bem-sucedida e, se sim, lê e exibe o conteúdo da resposta.
# 6 - Exibir Erro: Se a resposta não for bem-sucedida, exibe uma mensagem de erro com o status da resposta.

# Funcionamento

# Filtro: Parâmetros como category=electronics permitem que você filtre os resultados para mostrar apenas os produtos da categoria "eletrônicos".
# Limite (Pagination): Parâmetros como limit=10 controlam o número de resultados retornados. Por exemplo, limit=10 significa que você só quer 10 produtos por página.
# Paginação: Parâmetros como page=1 indicam em qual página você está navegando. Se houver muitas páginas, você pode mudar para page=2, page=3, etc.
# Ordenação: Parâmetros como sort=price ordenam os resultados com base em um critério, como o preço.
