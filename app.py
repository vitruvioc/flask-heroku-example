from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Flask Demo para Heroku Review Apps</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 40px;
                line-height: 1.6;
                color: #333;
            }
            .container {
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
                border: 1px solid #ddd;
                border-radius: 5px;
                background-color: #f9f9f9;
            }
            h1 {
                color: #2c3e50;
            }
            .app-info {
                margin-top: 20px;
                padding: 15px;
                background-color: #e8f4f8;
                border-radius: 4px;
            }
            .footer {
                margin-top: 30px;
                font-size: 0.8em;
                color: #777;
                text-align: center;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>¡Aplicación Flask de prueba para Heroku!</h1>
            <p>Esta es una aplicación Flask simple diseñada para probar el sistema de review apps de Heroku.</p>
            
            <div class="app-info">
                <h2>Información de la aplicación</h2>
                <p><strong>Entorno:</strong> Heroku</p>
                <p><strong>Framework:</strong> Flask</p>
                <p><strong>Versión de Python:</strong> 3.10.x</p>
                <p><strong>Aplicación ID:</strong> """ + os.environ.get('HEROKU_APP_ID', 'Local development') + """</p>
                <p><strong>Nombre de app:</strong> """ + os.environ.get('HEROKU_APP_NAME', 'Local development') + """</p>
            </div>
            
            <div class="footer">
                <p>Creado para probar heroku-review-apps</p>
            </div>
        </div>
    </body>
    </html>
    """

@app.route('/health')
def health():
    return {"status": "ok", "app": os.environ.get('HEROKU_APP_NAME', 'local')}

if __name__ == '__main__':
    # Obtiene el puerto del entorno o usa 5000 como predeterminado
    port = int(os.environ.get('PORT', 5000))
    # Ejecuta la app con debug=True en desarrollo, False en producción
    debug = os.environ.get('FLASK_ENV') == 'development'
    app.run(host='0.0.0.0', port=port, debug=debug)