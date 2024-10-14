from app import create_app, db

app = create_app()

# Cria automaticamente as tabelas no banco de dados
with app.app_context():
    db.create_all()  # Isso criará todas as tabelas baseadas nos modelos definidos

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
