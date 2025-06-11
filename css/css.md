# CSS

CSS (Cascading Style Sheets ou "Folhas de Estilo em Cascata") é uma linguagem usada para estilizar documentos HTML. Ele controla cor, fonte, espaçamento, layout, animações, responsividade, entre outros aspectos visuais de uma página web.

A ideia principal do CSS é separar a estrutura (HTML) da apresentação (CSS), tornando o código mais organizado, reutilizável e fácil de manter.

### 📄 Exemplo básico de HTML com CSS

```html
<!DOCTYPE html>
<html>
<head>
  <title>Exemplo CSS</title>
  <style>
    body {
      background-color: #f0f0f0;
      font-family: Arial, sans-serif;
    }

    h1 {
      color: #3498db;
      text-align: center;
    }

    p {
      color: #555;
      max-width: 600px;
      margin: 0 auto;
      line-height: 1.5;
    }
  </style>
</head>
<body>
  <h1>Bem-vindo ao CSS!</h1>
  <p>Este é um exemplo básico de como aplicar estilos em uma página HTML usando CSS.</p>
</body>
</html>
```

## 🧩 Como usar CSS
Existem três formas principais de aplicar CSS em um documento HTML:

1. Inline (dentro da tag)

```html
<p style="color: red;">Texto em vermelho</p>
```

2. Interno (no \<style\> dentro do HTML)

```html
<style>
  p { color: red; }
</style>
```

3. Externo (arquivo .css separado)

HTML:

```html
<link rel="stylesheet" href="estilos.css">
```

estilos.css:

```css
p {
  color: red;
}
```

## 🔎 Conceitos principais

### Seletores

Selecionam elementos HTML para aplicar estilos.

```css
h1 { color: blue; }           /* seletor de elemento */
#cabecalho { font-size: 2em; } /* seletor por ID */
.destaque { background: yellow; } /* seletor por classe */
```

### Propriedades e valores

Definem os estilos aplicados.

```css
p {
  color: #333;
  font-size: 16px;
  margin: 10px 0;
}
```

### Cascata e Especificidade

Regras com maior especificidade ou que aparecem por último têm prioridade. Exemplo:

```css
p { color: black; }
#paragrafo1 { color: red; } /* Este estilo prevalece */
```

## 📐 Layout moderno com Flexbox e Grid

### Flexbox (alinhamento em linha ou coluna)

```css
.container {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
```

### CSS Grid (distribuição em linhas e colunas)

```css
.grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
}
```

## 📱 Responsividade com Media Queries

Permite adaptar o layout a diferentes tamanhos de tela:

```css
@media (max-width: 768px) {
  body {
    background-color: lightblue;
  }
}
```

## 🎨 Animações e transições

### Transição simples:

```css
button {
  transition: background-color 0.3s ease;
}

button:hover {
  background-color: #3498db;
}
```

### Animação com @keyframes:

```css

@keyframes desvanecer {
  from { opacity: 0; }
  to { opacity: 1; }
}

div {
  animation: desvanecer 1s ease-in;
}
```

## 🧠 Recursos avançados

### Variáveis CSS:

```css
:root {
  --cor-primaria: #4CAF50;
}

h1 {
  color: var(--cor-primaria);
}
```

### Pseudo-classes e pseudo-elementos:

```css
a:hover { text-decoration: underline; } /* quando o mouse passa */
p::first-letter { font-size: 200%; }     /* primeira letra de um parágrafo */
```
