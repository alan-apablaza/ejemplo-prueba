# productos = {codigo: [tipo, nombre, sabor, tamano, vegano], ...}

productos = {
    'TRT01': ['Torta',   'Selva Negra',    'Chocolate',   'Grande',     'No'],
    'TRT02': ['Torta',   'Tres Leches',    'Vainilla',    'Mediana',    'No'],
    'GAL01': ['Galleta', 'Chips de Choco', 'Chocolate',   'Individual', 'No'],
    'GAL02': ['Galleta', 'Avena y Pasas',  'Avena',       'Individual', 'Si'],
    'PAN01': ['Pan',     'Baguette',       'Natural',     'Grande',     'Si'],
    'PAN02': ['Pan',     'Croissant',      'Mantequilla', 'Individual', 'No'],
    'BEB01': ['Bebida',  'Cafe Latte',     'Cafe',        'Mediano',    'No'],
    'BEB02': ['Bebida',  'Jugo Natural',   'Naranja',     'Grande',     'Si'],
}
for producto in productos:  
    print(producto)