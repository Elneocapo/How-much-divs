# How Much Divs

Esta aplicación de escritorio cuenta cuántos elementos `<div>` hay en una página web dada por su URL.

## Descripción

La app utiliza una interfaz gráfica sencilla hecha con Tkinter. El usuario ingresa una URL y al presionar "Search", la aplicación descarga el contenido HTML de la página y cuenta cuántas etiquetas `<div>` contiene, mostrando el resultado.

## Cómo usar

1. Ejecuta el script Python.
2. Ingresa la URL de la página web que quieres analizar.
3. Haz clic en el botón "Search".
4. La app mostrará el número de `<div>` encontrados en esa página.

## Requisitos

- Python 3.x
- Biblioteca `requests`
- Biblioteca `tkinter` (generalmente incluida con Python)

## Instalación de dependencias

```bash
pip install requests
