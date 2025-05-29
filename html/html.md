# HTML 

##### HTML (HyperText Markup Language) é a linguagem padrão usada para criar páginas da web. Ele estrutura o conteúdo usando elementos representados por tags.

## Estrutura Básica de um Documento HTML

```html
<!DOCTYPE html>
<html lang="pt-BR">
  <head>
    <meta charset="UTF-8">
    <title>Título da Página</title>
  </head>
  <body>
    <h1>Meu Primeiro Título</h1>
    <p>Este é um parágrafo.</p>
  </body>
</html>
```

## Principais Elementos

`<!DOCTYPE html>`: define o tipo do documento.

`<html>`: elemento raiz.

`<head>`: contém metadados (não visíveis).

`<title>`: título da página, mostrado na aba do navegador.

`<body>`: conteúdo visível da página.

## Elementos Comuns

### Cabeçalhos
Usados para estruturar títulos, variam de `<h1>` (mais importante) até `<h6>`.

```html
<h1>Título Principal</h1>
<h2>Subtítulo</h2>
```

### Parágrafos

Usa a tag `<p>`:

```html
<p>Este é um parágrafo de texto.</p>
```

### Links

Usa a tag `<a>` com o atributo href:

```html
<a href="https://developer.mozilla.org/">Visite o MDN</a>
```

### Imagens

Usa a tag `<img>` com os atributos src e alt:

```html
<img src="imagem.png" alt="Descrição da imagem">
```

### Listas

Ordenada (`<ol>`) e não ordenada (`<ul>`):

```html
<ul>
  <li>Item 1</li>
  <li>Item 2</li>
</ul>

<ol>
  <li>Primeiro</li>
  <li>Segundo</li>
</ol>
```

### Botões

```html
<button>Clique aqui</button>
```

### Comentários

```html
<!-- Este é um comentário -->
 ```

## Boas Práticas

- Sempre fechar as tags.

- Usar alt em imagens para acessibilidade.

- Utilizar elementos semânticos (`<header>`, `<footer>`, `<article>`, etc.) para melhor organização e SEO.

## Recursos

[Documentação oficial MDN sobre HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)