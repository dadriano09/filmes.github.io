from flask import Flask, request, render_template

app = Flask(__name__)

# Lista de filmes para fins de exemplo
filmes = [
    {'titulo': 'Barbie Quebra Nozes', 'link': 'https://drive.google.com/file/d/1KDSMCM9RQlUsuCY_KnjeDTbwCUUOkRnx/view'},
    {'titulo': 'velozes e furiosos desafio em tóquio', 'link': 'https://drive.google.com/file/d/0B8CTXrwnkK4YekZVcGNUblZZejQ/view?resourcekey=0-DF5YHgU-RmGRbMHsZIlxUA'},
    {'titulo': 'Filme 3', 'link': 'https://pt.pornhub.com/view_video.php?viewkey=64999f307102f'},
    # Adicione mais filmes aqui
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['GET'])
def buscar():
    query = request.args.get('q', '')  # Obtém o valor do parâmetro 'q' da URL
    resultados = []
    
    if query:
        # Realize aqui a busca na lista de filmes
        query_lower = query.lower()  # Convertendo a consulta para letras minúsculas
        resultados = [filme for filme in filmes if query_lower in filme['titulo'].lower()]

    return render_template('resultado.html', query=query, resultados=resultados)

if __name__ == '__main__':
    app.run(debug=True)